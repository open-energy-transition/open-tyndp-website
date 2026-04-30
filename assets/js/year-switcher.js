// SPDX-FileCopyrightText: Contributors to Open-TYNDP <https://github.com/open-energy-transition/open-tyndp-site>
//
// SPDX-License-Identifier: MIT

document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('.year-btn').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var frameId = this.dataset.frame;
      var year = this.dataset.year;
      var frame = document.getElementById(frameId);
      if (!frame) return;

      // Update iframe src — replace the year part of the filename
      frame.src = frame.src.replace(/_\d{4}-/, '_' + year + '-');

      // Update active button state within this switcher group
      var switcher = this.closest('.year-switcher');
      switcher.querySelectorAll('.year-btn').forEach(function (b) {
        b.classList.remove('active');
      });
      this.classList.add('active');
    });
  });
});
