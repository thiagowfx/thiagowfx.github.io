function setTheme(theme) {
  if (theme === "auto") {
    document.documentElement.style.colorScheme = "light dark";
    localStorage.removeItem("theme");
  } else {
    document.documentElement.style.colorScheme = theme;
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
  document.documentElement.style.colorScheme = saved;
} else {
  document.documentElement.style.colorScheme = "light dark";
}
updateThemeIcon();

// Toggle between auto, light, dark
document.getElementById("theme-toggle").addEventListener("click", function () {
  const current = getCurrentThemeState();
  const cycle = { auto: "light", light: "dark", dark: "auto" };
  const next = cycle[current];
  setTheme(next);

  // Animate the icon
  const button = this;
  button.classList.add("spinning");
  setTimeout(() => button.classList.remove("spinning"), 600);
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
  const button = event.target.closest("[data-copy-code]");
  if (!button) {
    return;
  }
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
      button.dataset.originalHtml = button.innerHTML;
      button.innerHTML =
        '<svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" height="1em" width="1em"><polyline points="20 6 9 17 4 12"></polyline></svg>';
      setTimeout(function () {
        button.innerHTML = button.dataset.originalHtml;
      }, 1500);
    })
    .catch(function () {
      setTimeout(function () {
        button.innerHTML = button.dataset.originalHtml;
      }, 1500);
    });
});

// Reading progress indicator
const readingProgress = document.getElementById("reading-progress");
if (readingProgress) {
  window.addEventListener("scroll", function () {
    const scrollTop = document.documentElement.scrollTop;
    const scrollHeight =
      document.documentElement.scrollHeight -
      document.documentElement.clientHeight;
    const progress = scrollHeight > 0 ? (scrollTop / scrollHeight) * 100 : 0;
    readingProgress.style.width = progress + "%";
  });
}

// Fullscreen mode functionality
const fullscreenBtn = document.getElementById("fullscreen-btn");
const fullscreenIcon = document.getElementById("fullscreen-icon");

if (fullscreenBtn) {
  // Check for fullscreen parameter in URL or localStorage and keep them in sync
  const urlParams = new URLSearchParams(window.location.search);
  const isFullscreenParam = urlParams.has("fullscreen");
  const isFullscreenLocal = localStorage.getItem("fullscreen-mode") === "true";

  if (isFullscreenParam || isFullscreenLocal) {
    document.body.classList.add("fullscreen-mode");
    fullscreenIcon.textContent = "✕";

    // Sync URL param → localStorage
    if (isFullscreenParam && !isFullscreenLocal) {
      localStorage.setItem("fullscreen-mode", true);
    }
    // Sync localStorage → URL param
    if (isFullscreenLocal && !isFullscreenParam) {
      const url = new URL(window.location);
      url.searchParams.set("fullscreen", "true");
      window.history.replaceState({}, "", url);
    }
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
