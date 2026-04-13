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

  const h2Headings = [...main.querySelectorAll("h2")];
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

  h2Headings.forEach((h2) => {
    const li = document.createElement("li");
    const row = document.createElement("div");
    row.className = "outline-item-row";
    const a = document.createElement("a");
    const h2Id = ensureId(h2);
    a.href = `#${h2Id}`;
    a.textContent = h2.textContent || "Section";
    row.appendChild(a);

    headings.push(h2);
    links.set(h2Id, a);

    const section = h2.closest("section");
    const h3s = section ? [...section.querySelectorAll("h3")] : [];
    if (h3s.length > 0) {
      const toggle = document.createElement("button");
      toggle.type = "button";
      toggle.className = "outline-toggle";
      toggle.setAttribute("aria-label", `Toggle ${a.textContent || "section"} subsections`);
      toggle.setAttribute("aria-expanded", "true");
      toggle.textContent = "▾";
      row.insertBefore(toggle, a);

      const sub = document.createElement("ul");
      sub.className = "outline-list outline-sublist";
      h3s.forEach((h3) => {
        const subLi = document.createElement("li");
        const subA = document.createElement("a");
        const h3Id = ensureId(h3);
        subA.href = `#${h3Id}`;
        subA.textContent = h3.textContent || "Subsection";
        subLi.appendChild(subA);
        sub.appendChild(subLi);
        headings.push(h3);
        links.set(h3Id, subA);
      });
      toggle.addEventListener("click", () => {
        const expanded = toggle.getAttribute("aria-expanded") === "true";
        const nextExpanded = !expanded;
        toggle.setAttribute("aria-expanded", String(nextExpanded));
        toggle.textContent = nextExpanded ? "▾" : "▸";
        sub.hidden = !nextExpanded;
      });
      li.appendChild(row);
      li.appendChild(sub);
    } else {
      li.appendChild(row);
    }

    list.appendChild(li);
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
