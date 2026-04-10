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

  const headings = [...main.querySelectorAll("h2")];
  const list = document.createElement("ul");
  list.className = "outline-list";

  const slugify = (text) =>
    text
      .toLowerCase()
      .replace(/[^a-z0-9]+/g, "-")
      .replace(/(^-|-$)/g, "")
      .slice(0, 64) || "section";

  const links = new Map();
  headings.forEach((heading) => {
    if (!heading.id) heading.id = slugify(heading.textContent || "section");
    const li = document.createElement("li");
    const a = document.createElement("a");
    a.href = `#${heading.id}`;
    a.textContent = heading.textContent || "Section";
    li.appendChild(a);
    list.appendChild(li);
    links.set(heading.id, a);
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
  const print = document.getElementById("print-page-btn");
  if (!print) return;
  print.addEventListener("click", () => window.print());
})();
