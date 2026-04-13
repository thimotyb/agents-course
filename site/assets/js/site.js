(() => {
  const themeSelect = document.getElementById("theme-select");
  const KEY = "course_theme";
  const THEMES = new Set(["light", "dark"]);

  const getTheme = () => {
    const saved = localStorage.getItem(KEY);
    return THEMES.has(saved || "") ? saved : "light";
  };

  const applyTheme = (theme) => {
    const safeTheme = THEMES.has(theme) ? theme : "light";
    document.body.setAttribute("data-theme", safeTheme);
    localStorage.setItem(KEY, safeTheme);
    if (themeSelect) themeSelect.value = safeTheme;
  };

  applyTheme(getTheme());
  if (themeSelect) {
    themeSelect.addEventListener("change", () => applyTheme(themeSelect.value));
  }
})();

(() => {
  const select = document.getElementById("lang-select");

  const setGoogTransCookie = (lang) => {
    const value = lang === "it" ? "/en/it" : "/en/en";
    document.cookie = `googtrans=${value};path=/`;
    document.cookie = `googtrans=${value};path=/;domain=${location.hostname}`;
    localStorage.setItem("course_lang", lang);
  };

  const getCurrentLang = () => {
    const saved = localStorage.getItem("course_lang");
    if (saved === "it" || saved === "en") return saved;
    return "en";
  };

  const applyLanguage = (lang) => {
    setGoogTransCookie(lang);
    if (lang === "en") {
      location.reload();
      return;
    }

    const trySelectGoogleLanguage = () => {
      const gtSelect = document.querySelector(".goog-te-combo");
      if (!gtSelect) return false;
      gtSelect.value = "it";
      gtSelect.dispatchEvent(new Event("change"));
      return true;
    };

    if (!trySelectGoogleLanguage()) {
      window.setTimeout(trySelectGoogleLanguage, 900);
    }
  };

  window.googleTranslateElementInit = () => {
    if (!window.google || !window.google.translate) return;
    new window.google.translate.TranslateElement(
      {
        pageLanguage: "en",
        includedLanguages: "en,it",
        autoDisplay: false,
      },
      "google_translate_element"
    );

    const initialLang = getCurrentLang();
    if (select) select.value = initialLang;
    if (initialLang === "it") {
      window.setTimeout(() => applyLanguage("it"), 250);
    }
  };

  if (select) {
    select.value = getCurrentLang();
    select.addEventListener("change", () => {
      applyLanguage(select.value);
    });
  }
})();

(() => {
  const root = document.getElementById("outline-nav");
  const main = document.querySelector(".module-main");
  if (!root || !main) return;

  const allHeadings = [...main.querySelectorAll("h2, h3")];
  const list = document.createElement("ul");
  list.className = "outline-list";

  const slugify = (text) =>
    text
      .toLowerCase()
      .replace(/[^a-z0-9]+/g, "-")
      .replace(/(^-|-$)/g, "")
      .slice(0, 64) || "section";

  const ensureId = (heading) => {
    if (heading.id) return heading.id;
    const base = slugify(heading.textContent || "section");
    let candidate = base;
    let index = 2;
    while (document.getElementById(candidate)) {
      candidate = `${base}-${index++}`;
    }
    heading.id = candidate;
    return candidate;
  };

  const headings = [];
  const links = new Map();

  let currentLi = null;
  let currentSubList = null;
  let currentToggle = null;

  allHeadings.forEach((heading) => {
    const isH2 = heading.tagName.toLowerCase() === "h2";
    const id = ensureId(heading);
    const a = document.createElement("a");
    a.href = `#${id}`;
    a.textContent = heading.textContent || "Section";
    headings.push(heading);
    links.set(id, a);

    if (isH2) {
      currentLi = document.createElement("li");
      const row = document.createElement("div");
      row.className = "outline-item-row";
      row.appendChild(a);
      currentLi.appendChild(row);
      list.appendChild(currentLi);
      
      currentSubList = null;
      currentToggle = null;
    } else if (currentLi) {
      // Se è un h3, aggiungilo alla sottolista dell'ultimo h2 incontrato
      if (!currentSubList) {
        currentSubList = document.createElement("ul");
        currentSubList.className = "outline-list outline-sublist";
        currentLi.appendChild(currentSubList);

        // Aggiungi il toggle all'h2 se non esiste ancora
        const row = currentLi.querySelector(".outline-item-row");
        currentToggle = document.createElement("button");
        currentToggle.type = "button";
        currentToggle.className = "outline-toggle";
        currentToggle.setAttribute("aria-expanded", "true");
        currentToggle.textContent = "▾";
        row.insertBefore(currentToggle, row.firstChild);

        currentToggle.addEventListener("click", () => {
          const expanded = currentToggle.getAttribute("aria-expanded") === "true";
          currentToggle.setAttribute("aria-expanded", String(!expanded));
          currentToggle.textContent = !expanded ? "▾" : "▸";
          currentSubList.hidden = expanded;
        });
      }
      const subLi = document.createElement("li");
      subLi.appendChild(a);
      currentSubList.appendChild(subLi);
    }
  });

  root.replaceChildren(list);

  const markActive = () => {
    let active = headings[0];
    for (const heading of headings) {
      if (heading.getBoundingClientRect().top <= 130) active = heading;
      else break;
    }
    links.forEach((a) => a.classList.remove("active"));
    const activeLink = links.get(active.id);
    if (activeLink) activeLink.classList.add("active");
  };

  window.addEventListener("scroll", markActive, { passive: true });
  window.addEventListener("hashchange", markActive);
  markActive();
})();

(() => {
  const triggers = [...document.querySelectorAll("[data-print], #print-page-btn")];
  if (triggers.length === 0) return;

  const seen = new Set();
  triggers.forEach((trigger) => {
    if (seen.has(trigger)) return;
    seen.add(trigger);
    trigger.addEventListener("click", () => window.print());
  });
})();

(() => {
  const figures = [...document.querySelectorAll("figure[data-zoomable] img")];
  if (figures.length === 0) return;

  const lightbox = document.createElement("div");
  lightbox.className = "figure-lightbox";
  lightbox.hidden = true;
  lightbox.setAttribute("role", "dialog");
  lightbox.setAttribute("aria-modal", "true");
  lightbox.setAttribute("aria-label", "Image viewer");
  lightbox.innerHTML = `
    <div class="figure-lightbox-inner">
      <img class="figure-lightbox-image" alt="">
      <p class="figure-lightbox-caption"></p>
    </div>
  `;
  document.body.appendChild(lightbox);

  const lightboxImg = lightbox.querySelector(".figure-lightbox-image");
  const lightboxCaption = lightbox.querySelector(".figure-lightbox-caption");

  const closeLightbox = () => {
    lightbox.hidden = true;
    document.body.style.overflow = "";
  };

  const openLightbox = (img) => {
    const caption = img.closest("figure")?.querySelector("figcaption")?.textContent || "";
    lightboxImg.src = img.currentSrc || img.src;
    lightboxImg.alt = img.alt || "";
    lightboxCaption.textContent = caption;
    lightbox.hidden = false;
    document.body.style.overflow = "hidden";
  };

  figures.forEach((img) => {
    img.addEventListener("click", () => openLightbox(img));
  });

  lightbox.addEventListener("click", (event) => {
    if (event.target === lightbox || event.target === lightboxImg) closeLightbox();
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && !lightbox.hidden) closeLightbox();
  });
})();
