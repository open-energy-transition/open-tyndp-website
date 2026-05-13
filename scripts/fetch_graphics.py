#!/usr/bin/env python3
# SPDX-FileCopyrightText: Contributors to Open-TYNDP <https://github.com/open-energy-transition/open-tyndp-site>
#
# SPDX-License-Identifier: MIT

"""Download website assets/graphics from Google Cloud Storage."""

from __future__ import annotations

import json
import logging
import os
import shutil
import sys
import tempfile
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode
from urllib.request import urlopen

DEFAULT_BUCKET = "open-tyndp-data-store"
DEFAULT_PREFIX = "website/assets"
DEFAULT_TARGET = "assets"
DEFAULT_VERSION = "latest"
LIST_API_TEMPLATE = "https://storage.googleapis.com/storage/v1/b/{bucket}/o?{query}"
DOWNLOAD_URL_TEMPLATE = "https://storage.googleapis.com/{bucket}/{object_name}"
REMOTE_SUBDIR_PREFIXES = ("maps/", "plots/")

logger = logging.getLogger(__name__)


def _load_gcs_json(bucket: str, params: dict[str, str]) -> dict:
    """Fetch Google Cloud Storage JSON API response.

    If the request fails, the function raises an error."""
    url = LIST_API_TEMPLATE.format(bucket=bucket, query=urlencode(params))
    try:
        with urlopen(url) as response:
            return json.load(response)
    except HTTPError as exc:
        raise RuntimeError(f"HTTP {exc.code} for {url}") from exc
    except URLError as exc:
        raise RuntimeError(str(exc.reason)) from exc


def list_objects(bucket: str, prefix: str, delimiter: str | None = None) -> dict:
    """List GCS objects (paginated) under a bucket prefix."""
    items: list[str] = []
    prefixes: list[str] = []
    page_token = None

    while True:
        params: dict[str, str] = {"prefix": prefix}
        if delimiter:
            params["delimiter"] = delimiter
        if page_token:
            params["pageToken"] = page_token

        payload = _load_gcs_json(bucket, params)
        items.extend(
            item["name"]
            for item in payload.get("items", [])
            if not item["name"].endswith("/")
        )
        prefixes.extend(payload.get("prefixes", []))

        page_token = payload.get("nextPageToken")
        if not page_token:
            return {"items": items, "prefixes": prefixes}


def download_objects(bucket: str, prefix: str, target_dir: Path) -> int:
    """Download managed objects from GCS.

    Parameters
    ----------
    bucket : str
        Google Cloud Storage bucket name.
    prefix : str
        Object prefix to download from.
    target_dir : Path
        Local directory for downloaded files.

    Returns
    -------
    int
        Number of downloaded files.
    """
    object_names = list_objects(bucket, prefix)["items"]
    count = 0
    for object_name in object_names:
        relative_name = object_name.removeprefix(prefix)
        if Path(relative_name).name == ".DS_Store" or not relative_name.startswith(
            REMOTE_SUBDIR_PREFIXES
        ):
            continue

        destination = target_dir / relative_name
        destination.parent.mkdir(parents=True, exist_ok=True)
        object_url = DOWNLOAD_URL_TEMPLATE.format(
            bucket=bucket, object_name=quote(object_name, safe="/")
        )

        try:
            with urlopen(object_url) as response, destination.open("wb") as handle:
                shutil.copyfileobj(response, handle)
        except HTTPError as exc:
            raise RuntimeError(
                f"Failed to download gs://{bucket}/{object_name}: HTTP {exc.code}"
            ) from exc
        except URLError as exc:
            raise RuntimeError(
                f"Failed to download gs://{bucket}/{object_name}: {exc.reason}"
            ) from exc

        count += 1
        logger.info("Downloaded %s", relative_name)

    return count


def sync_assets(staged_dir: Path, target_dir: Path) -> None:
    """Copy remote assets into local ``assets/`` tree.

    The ``maps/`` and ``plots/`` directories are replaced wholesale so removed
    remote files do not persist locally.

    Parameters
    ----------
    staged_dir : Path
        Directory containing freshly downloaded remote assets.
    target_dir : Path
        Local ``assets/`` directory to update.
    """
    for source in staged_dir.rglob("*"):
        if source.is_dir():
            continue
        destination = target_dir / source.relative_to(staged_dir)
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)

    for managed_dir in ("maps", "plots"):
        source_dir = staged_dir / managed_dir
        if not source_dir.exists():
            continue
        destination_dir = target_dir / managed_dir
        if destination_dir.exists():
            shutil.rmtree(destination_dir)
        shutil.copytree(source_dir, destination_dir)


def main() -> int:
    """Download and sync versioned website assets.

    Bucket, prefix, version, and target are provided via environment
    variables:
    - ``OPEN_TYNDP_SITE_ASSETS_BUCKET``
    - ``OPEN_TYNDP_SITE_ASSETS_PREFIX``
    - ``ASSETS_VERSION`` (or legacy ``OPEN_TYNDP_SITE_ASSETS_VERSION``)
    - ``OPEN_TYNDP_SITE_ASSETS_TARGET``

    Returns
    -------
    int
        ``0`` if successful, ``1`` if failed.
    """
    bucket = os.environ.get("OPEN_TYNDP_SITE_ASSETS_BUCKET", DEFAULT_BUCKET)
    base_prefix = os.environ.get("OPEN_TYNDP_SITE_ASSETS_PREFIX", DEFAULT_PREFIX).strip(
        "/"
    )
    version = os.environ.get(
        "ASSETS_VERSION",
        os.environ.get("OPEN_TYNDP_SITE_ASSETS_VERSION", DEFAULT_VERSION),
    )
    target_dir = Path(os.environ.get("OPEN_TYNDP_SITE_ASSETS_TARGET", DEFAULT_TARGET))

    temp_root = Path(tempfile.mkdtemp(prefix="open-tyndp-site-assets-"))
    staged_assets_dir = temp_root / "remote-assets"

    try:
        # get requested version or resolve "latest" to the most recent version directory
        requested = version.strip().strip("/")
        if requested == "latest":
            versions = [
                p.removeprefix(f"{base_prefix}/").removesuffix("/")
                for p in list_objects(bucket, f"{base_prefix}/", delimiter="/")[
                    "prefixes"
                ]
            ]
            if not versions:
                raise RuntimeError(
                    f"No version directories found under gs://{bucket}/{base_prefix}/."
                )
            requested = max(versions)

        prefix = f"{base_prefix}/{requested}/"
        downloaded = download_objects(bucket, prefix, staged_assets_dir)
        sync_assets(staged_assets_dir, target_dir)
        logger.info(
            "Updated %s files from gs://%s/%s into %s/ (version=%s).",
            downloaded,
            bucket,
            prefix,
            target_dir,
            requested,
        )
    except Exception as exc:
        logger.error("%s", exc)
        return 1
    finally:
        shutil.rmtree(temp_root, ignore_errors=True)

    return 0


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s", stream=sys.stdout)
    raise SystemExit(main())
