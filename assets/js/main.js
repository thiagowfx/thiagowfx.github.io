function setTheme(theme) {
  if (theme === "auto") {
    document.documentElement.removeAttribute("data-theme");
    localStorage.removeItem("theme");
  } else {
    document.documentElement.setAttribute("data-theme", theme);
    localStorage.setItem("theme", theme);
  }
  updateThemeIcon();
}

function getCurrentThemeState() {
  return localStorage.getItem("theme") || "auto";
}

function updateThemeIcon() {
  const state = getCurrentThemeState();
  const icons = { auto: "🌓", dark: "🌙", light: "☀️" };
  document.getElementById("theme-toggle-icon").textContent = icons[state];
}

// Initialize
const saved = localStorage.getItem("theme");
if (saved) {
  document.documentElement.setAttribute("data-theme", saved);
}
updateThemeIcon();

// Toggle between auto, light, dark
document.getElementById("theme-toggle").addEventListener("click", function () {
  const current = getCurrentThemeState();
  const cycle = { auto: "light", light: "dark", dark: "auto" };
  const next = cycle[current];
  setTheme(next);
});

// Dropdown menu functionality
const dropdownTriggers = document.querySelectorAll(".nav-dropdown-trigger");
dropdownTriggers.forEach((trigger) => {
  trigger.addEventListener("click", function (e) {
    e.preventDefault();
    const dropdown = this.closest(".nav-dropdown");
    const isOpen = dropdown.classList.contains("open");

    // Close all dropdowns
    document.querySelectorAll(".nav-dropdown.open").forEach((d) => {
      d.classList.remove("open");
    });

    // Open clicked dropdown if it wasn't open
    if (!isOpen) {
      dropdown.classList.add("open");
    }
  });
});

// Language dropdown functionality
const langToggle = document.getElementById("lang-toggle");
if (langToggle) {
  langToggle.addEventListener("click", function (e) {
    e.preventDefault();
    const dropdown = this.closest(".lang-dropdown");
    const isOpen = dropdown.classList.contains("open");

    // Close all dropdowns
    document.querySelectorAll(".lang-dropdown.open").forEach((d) => {
      d.classList.remove("open");
    });

    // Open clicked dropdown if it wasn't open
    if (!isOpen) {
      dropdown.classList.add("open");
    }
  });
}

// Close dropdown when clicking outside
document.addEventListener("click", function (e) {
  if (
    !e.target.closest(".nav-dropdown") &&
    !e.target.closest(".lang-dropdown")
  ) {
    document.querySelectorAll(".nav-dropdown.open").forEach((d) => {
      d.classList.remove("open");
    });
    document.querySelectorAll(".lang-dropdown.open").forEach((d) => {
      d.classList.remove("open");
    });
  }
});

document.addEventListener("click", function (event) {
  if (!event.target.matches("[data-copy-code]")) {
    return;
  }
  const button = event.target;
  const container = button.closest(".codeblock");
  if (!container) {
    return;
  }
  const code = container.querySelector("pre code");
  if (!code) {
    return;
  }
  const text = code.innerText;
  if (!navigator.clipboard || !navigator.clipboard.writeText) {
    return;
  }
  navigator.clipboard
    .writeText(text)
    .then(function () {
      button.dataset.originalLabel = button.textContent;
      button.textContent = "Copied!";
      setTimeout(function () {
        button.textContent = button.dataset.originalLabel || "Copy";
      }, 1500);
    })
    .catch(function () {
      button.textContent = "Failed";
      setTimeout(function () {
        button.textContent = button.dataset.originalLabel || "Copy";
      }, 1500);
    });
});

// Fullscreen mode functionality
const fullscreenBtn = document.getElementById("fullscreen-btn");
const fullscreenIcon = document.getElementById("fullscreen-icon");

if (fullscreenBtn) {
  // Check for fullscreen parameter in URL or localStorage
  const urlParams = new URLSearchParams(window.location.search);
  const isFullscreenParam = urlParams.has("fullscreen");
  const isFullscreenLocal = localStorage.getItem("fullscreen-mode") === "true";

  if (isFullscreenParam || isFullscreenLocal) {
    document.body.classList.add("fullscreen-mode");
    fullscreenIcon.textContent = "✕";
  }

  fullscreenBtn.addEventListener("click", function () {
    document.body.classList.toggle("fullscreen-mode");
    const isFullscreen = document.body.classList.contains("fullscreen-mode");
    fullscreenIcon.textContent = isFullscreen ? "✕" : "⛶";
    localStorage.setItem("fullscreen-mode", isFullscreen);

    // Update URL with fullscreen parameter
    const url = new URL(window.location);
    if (isFullscreen) {
      url.searchParams.set("fullscreen", "true");
    } else {
      url.searchParams.delete("fullscreen");
    }
    window.history.replaceState({}, "", url);
  });

  // Keyboard shortcut (f key)
  document.addEventListener("keydown", function (event) {
    if (
      event.key === "f" &&
      !event.ctrlKey &&
      !event.metaKey &&
      !event.altKey
    ) {
      // Only trigger if not typing in an input or textarea
      if (!event.target.closest('input:not([type="hidden"]), textarea')) {
        event.preventDefault();
        fullscreenBtn.click();
      }
    }
  });
}
