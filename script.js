"use strict";

// Keep the year accurate without maintaining it separately in each page.
// The portfolio intentionally has no decorative animations or UI dependencies.
document.querySelectorAll("[data-year]").forEach((node) => {
  node.textContent = String(new Date().getFullYear());
});

// Track the section in view so the quiet navigation remains useful on longer pages.
// IntersectionObserver avoids running layout checks on every scroll event.
const sectionLinks = [...document.querySelectorAll('.nav a[href^="#"]')];
const sectionTargets = sectionLinks
  .map((link) => document.querySelector(link.getAttribute("href")))
  .filter(Boolean);

if (sectionTargets.length && "IntersectionObserver" in window) {
  const observer = new IntersectionObserver((entries) => {
    for (const entry of entries) {
      if (!entry.isIntersecting) continue;
      sectionLinks.forEach((link) => {
        if (link.getAttribute("href") === "#" + entry.target.id) {
          link.setAttribute("aria-current", "location");
        } else {
          link.removeAttribute("aria-current");
        }
      });
    }
  }, { rootMargin: "-18% 0px -65% 0px" });
  sectionTargets.forEach((section) => observer.observe(section));
  // Hash links also work when visitors arrive directly from an external profile.
  window.addEventListener("hashchange", () => {
    const current = window.location.hash;
    sectionLinks.forEach((link) => {
      if (link.getAttribute("href") === current) link.setAttribute("aria-current", "location");
      else link.removeAttribute("aria-current");
    });
  });

  // Clear the section highlight when the visitor returns to the introduction.
  const introduction = document.querySelector("#top");
  if (introduction) {
    const introObserver = new IntersectionObserver(([entry]) => {
      if (entry.isIntersecting) {
        sectionLinks.forEach((link) => link.removeAttribute("aria-current"));
      }
    }, { threshold: 0.45 });
    introObserver.observe(introduction);
  }
}
