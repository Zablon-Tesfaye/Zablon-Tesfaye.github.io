"use strict";

// Built the car motion around page scroll progress, not a timed video.
// Scrolling down advances the vehicle up the road; scrolling back reverses it.
(() => {
  const rail = document.querySelector("[data-drive-rail]");
  const car = document.querySelector("[data-drive-vehicle]");
  if (!rail || !car) return;

  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  let scheduled = false;
  const desktop = window.matchMedia("(min-width: 1200px)");

  function draw() {
    scheduled = false;
    // Skip layout calculations while the road is hidden on smaller screens.
    if (!desktop.matches) return;
    // Use the available document travel so the vehicle reaches the top at the footer.
    const maxScroll = Math.max(0, document.documentElement.scrollHeight - window.innerHeight);
    const progress = maxScroll ? Math.min(1, Math.max(0, window.scrollY / maxScroll)) : 0;
    const maxTravel = Math.max(0, rail.clientHeight - car.offsetHeight - 47);

    // Keep the car fixed in the reduced-motion setting rather than reacting to scrolling.
    const offset = reducedMotion.matches ? maxTravel : maxTravel * (1 - progress);
    rail.style.setProperty("--drive-offset", offset.toFixed(1) + "px");
    rail.style.setProperty("--drive-progress", (reducedMotion.matches ? 0 : progress).toFixed(4));
  }

  function schedule() {
    if (!scheduled) {
      scheduled = true;
      window.requestAnimationFrame(draw);
    }
  }

  window.addEventListener("scroll", schedule, { passive: true });
  window.addEventListener("resize", schedule, { passive: true });
  window.addEventListener("load", schedule, { once: true });
  if (reducedMotion.addEventListener) reducedMotion.addEventListener("change", schedule);
  if (desktop.addEventListener) desktop.addEventListener("change", schedule);
  schedule();
})();
