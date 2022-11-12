//* Project specific Javascript goes here. */

function toggleMobileNav(evt) {
  const mobileNav = document.getElementById("mobileNav");
  if (mobileNav) {
    if (mobileNav.dataset.state === "open") {
      // Open -> Close
      mobileNav.classList.remove(
        "duration-150",
        "ease-out",
        "opacity-100",
        "scale-100"
      );
      mobileNav.classList.add(
        "transition",
        "duration-100",
        "ease-in",
        "opacity-0",
        "scale-95"
      );
      mobileNav.dataset.state = "closed";
    } else {
      // Close -> Open
      mobileNav.classList.remove(
        "duration-100",
        "ease-in",
        "opacity-0",
        "scale-95"
      );
      mobileNav.classList.add(
        "transition",
        "duration-150",
        "ease-out",
        "opacity-100",
        "scale-100"
      );
      mobileNav.dataset.state = "open";
    }
  }
}
