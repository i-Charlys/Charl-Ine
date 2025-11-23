document.addEventListener("DOMContentLoaded", function() {
  const observerOptions = {
    root: null,
    rootMargin: "0px",
    threshold: 0.1
  };

  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
        observer.unobserve(entry.target); // Only animate once
      }
    });
  }, observerOptions);

  // Target main content elements
  const elements = document.querySelectorAll("article h1, article h2, article p, article ul, article ol, article .admonition");
  elements.forEach(el => {
    el.classList.add("fade-in-section");
    observer.observe(el);
  });
});
