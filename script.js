"use strict";

// Keep the year accurate without maintaining it separately in each page.
// The portfolio intentionally has no decorative animations or UI dependencies.
document.querySelectorAll("[data-year]").forEach((node) => {
  node.textContent = String(new Date().getFullYear());
});
