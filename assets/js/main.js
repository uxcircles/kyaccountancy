/* KY Accountancy — motion, menu, open-now status, HMRC deadlines, company date calculator, contact form */
(function () {
  var T = window.KY || {};
  var doc = document.documentElement;
  var LANG = doc.lang || "en-GB";
  var LOCALE = LANG.indexOf("zh") === 0 ? "zh-CN" : LANG.indexOf("ko") === 0 ? "ko-KR" : "en-GB";
  var reduced = matchMedia("(prefers-reduced-motion: reduce)").matches;
  var finePointer = matchMedia("(hover: hover) and (pointer: fine)").matches;
  var $ = function (s, el) { return (el || document).querySelector(s); };
  var $$ = function (s, el) { return Array.prototype.slice.call((el || document).querySelectorAll(s)); };
  function store(k, v) {
    try { if (v === undefined) return sessionStorage.getItem(k); if (v === null) sessionStorage.removeItem(k); else sessionStorage.setItem(k, v); }
    catch (e) { return null; }
  }

  // ---------------------------------------------------------------- page transition
  var curtain = $(".curtain");
  if (!reduced && store("ky-nav")) { document.body.classList.add("is-entering"); }
  store("ky-nav", null);
  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest("a[href]");
    if (!a || reduced || e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
    if (a.target === "_blank" || a.hasAttribute("download")) return;
    var url = new URL(a.href, location.href);
    if (url.origin !== location.origin || !/^https?:$/.test(url.protocol)) return;
    if (url.pathname === location.pathname && url.hash) return;
    e.preventDefault();
    store("ky-nav", "1");
    curtain.classList.add("is-leaving");
    setTimeout(function () { location.href = url.href; }, 560);
  });
  window.addEventListener("pageshow", function (e) {
    if (e.persisted) { curtain.classList.remove("is-leaving"); document.body.classList.remove("is-entering"); }
  });

  // ---------------------------------------------------------------- header & menu
  var header = $("[data-header]");
  var lastY = window.scrollY;
  function onHeader() {
    var y = window.scrollY;
    header.classList.toggle("is-scrolled", y > 40);
    header.classList.toggle("is-hidden", y > 480 && y > lastY && !document.body.classList.contains("menu-open"));
    lastY = y;
  }
  var btn = $(".menu-btn");
  var menu = $("#menu");
  function setMenu(open) {
    btn.setAttribute("aria-expanded", String(open));
    document.body.classList.toggle("menu-open", open);
    document.body.style.overflow = open ? "hidden" : "";
    if (open) { menu.hidden = false; requestAnimationFrame(function () { menu.classList.add("is-open"); }); }
    else { menu.classList.remove("is-open"); setTimeout(function () { if (!menu.classList.contains("is-open")) menu.hidden = true; }, 800); }
  }
  if (btn && menu) {
    btn.addEventListener("click", function () { setMenu(btn.getAttribute("aria-expanded") !== "true"); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape" && menu.classList.contains("is-open")) { setMenu(false); btn.focus(); } });
  }
  $$("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });

  // ---------------------------------------------------------------- reveals
  var revealables = $$(".split, .reveal-up");
  if ("IntersectionObserver" in window && !reduced) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("is-in"); io.unobserve(en.target); } });
    }, { rootMargin: "0px 0px -10% 0px" });
    var delay = document.body.classList.contains("is-entering") ? 450 : 80;
    setTimeout(function () { revealables.forEach(function (el) { io.observe(el); }); }, delay);
  } else {
    revealables.forEach(function (el) { el.classList.add("is-in"); });
  }

  // ---------------------------------------------------------------- rotating language word
  $$(".rotator").forEach(function (el) {
    var words = (el.getAttribute("data-words") || "").split("|");
    var span = el.firstElementChild;
    var i = 0;
    if (words.length < 2) return;
    setInterval(function () {
      if (document.hidden) return;
      i = (i + 1) % words.length;
      if (reduced) { span.textContent = words[i]; return; }
      el.classList.add("is-out");
      setTimeout(function () {
        span.textContent = words[i];
        el.classList.remove("is-out");
        el.classList.add("is-pre");
        void span.offsetWidth;
        el.classList.remove("is-pre");
      }, 420);
    }, 2800);
  });

  // ---------------------------------------------------------------- statement: words light up on scroll
  var scrubs = $$("[data-scrub]");
  scrubs.forEach(function (p) {
    var cjk = /zh/.test(LANG);
    var text = p.textContent;
    var parts = cjk ? Array.from(text) : text.split(/(\s+)/);
    p.textContent = "";
    var sr = document.createElement("span");
    sr.className = "sr"; sr.textContent = text;
    p.appendChild(sr);
    parts.forEach(function (w) {
      if (/^\s+$/.test(w)) { p.appendChild(document.createTextNode(w)); return; }
      var s = document.createElement("span");
      s.className = "w"; s.textContent = w; s.setAttribute("aria-hidden", "true");
      p.appendChild(s);
    });
    p._words = $$(".w", p);
  });

  // ---------------------------------------------------------------- count-up stats
  var londonYear = +new Intl.DateTimeFormat("en-GB", { timeZone: "Europe/London", year: "numeric" }).format(new Date());
  $$("[data-since]").forEach(function (el) { el.setAttribute("data-count", londonYear - +el.getAttribute("data-since")); el.textContent = el.getAttribute("data-count"); });
  var counters = $$("[data-count]");
  if ("IntersectionObserver" in window && !reduced) {
    var cio = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        cio.unobserve(en.target);
        var el = en.target, end = +el.getAttribute("data-count"), t0 = performance.now();
        (function tick(t) {
          var k = Math.min(1, (t - t0) / 1600), e = 1 - Math.pow(1 - k, 4);
          el.textContent = Math.round(end * e);
          if (k < 1) requestAnimationFrame(tick);
        })(t0);
      });
    }, { threshold: .6 });
    counters.forEach(function (el) { el.textContent = "0"; cio.observe(el); });
  }

  // ---------------------------------------------------------------- scroll-linked effects
  var diamonds = $$("[data-parallax] .diamond");
  var steps = $("[data-progress]");
  var ticking = false;
  function progress(el, start, end) {
    var r = el.getBoundingClientRect(), vh = window.innerHeight;
    var p = (vh * start - r.top) / (r.height + vh * (start - end));
    return Math.max(0, Math.min(1, p));
  }
  function onScroll() {
    ticking = false;
    onHeader();
    var sp = window.scrollY / window.innerHeight;
    diamonds.forEach(function (d) { d.style.setProperty("--sp", sp.toFixed(3)); });
    scrubs.forEach(function (p) {
      var k = reduced ? 1 : progress(p, .85, .45);
      var n = Math.round(k * p._words.length);
      p._words.forEach(function (w, i) { w.classList.toggle("on", i < n); });
    });
    if (steps) steps.style.setProperty("--p", progress(steps, .7, .5).toFixed(3));
  }
  window.addEventListener("scroll", function () { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
  window.addEventListener("resize", onScroll);
  onScroll();

  // ---------------------------------------------------------------- pointer: parallax, magnetic, cursor
  if (finePointer && !reduced) {
    doc.classList.add("has-cursor");
    var cursor = $(".cursor"), cx = innerWidth / 2, cy = innerHeight / 2, ptx = cx, pty = cy;
    cursor.classList.add("is-hidden");
    window.addEventListener("pointermove", function (e) {
      ptx = e.clientX; pty = e.clientY;
      var nx = e.clientX / innerWidth - .5, ny = e.clientY / innerHeight - .5;
      diamonds.forEach(function (d) { d.style.setProperty("--mx", (nx * -40).toFixed(1) + "px"); d.style.setProperty("--my", (ny * -40).toFixed(1) + "px"); });
      var t = e.target.closest ? e.target.closest("a, button, input, select, textarea, label") : null;
      cursor.classList.toggle("is-link", !!t && !t.closest("[data-cursor='go']"));
      cursor.classList.toggle("is-go", !!(e.target.closest && e.target.closest("[data-cursor='go']")));
      cursor.classList.toggle("is-hidden", !!t && /INPUT|SELECT|TEXTAREA/.test(t.tagName));
    });
    document.addEventListener("pointerleave", function () { cursor.classList.add("is-hidden"); });
    document.addEventListener("pointerenter", function () { cursor.classList.remove("is-hidden"); });
    (function loop() {
      cx += (ptx - cx) * .2; cy += (pty - cy) * .2;
      cursor.style.transform = "translate3d(" + cx.toFixed(1) + "px," + cy.toFixed(1) + "px,0)";
      requestAnimationFrame(loop);
    })();
    $$("[data-magnetic]").forEach(function (el) {
      el.addEventListener("pointermove", function (e) {
        var r = el.getBoundingClientRect();
        var x = e.clientX - r.left - r.width / 2, y = e.clientY - r.top - r.height / 2;
        el.style.transform = "translate(" + (x * .25).toFixed(1) + "px," + (y * .35).toFixed(1) + "px)";
      });
      el.addEventListener("pointerleave", function () {
        el.style.transition = "transform .7s cubic-bezier(.16,1,.3,1), color .5s";
        el.style.transform = "";
        setTimeout(function () { el.style.transition = ""; }, 700);
      });
    });
  }

  // ---------------------------------------------------------------- London time & open status
  function londonNow() {
    var parts = new Intl.DateTimeFormat("en-GB", {
      timeZone: "Europe/London", year: "numeric", month: "2-digit", day: "2-digit",
      hour: "2-digit", minute: "2-digit", weekday: "short", hour12: false
    }).formatToParts(new Date());
    var o = {};
    parts.forEach(function (p) { o[p.type] = p.value; });
    var days = { Sun: 0, Mon: 1, Tue: 2, Wed: 3, Thu: 4, Fri: 5, Sat: 6 };
    return { y: +o.year, m: +o.month, d: +o.day, h: +o.hour % 24, min: +o.minute, dow: days[o.weekday] };
  }
  var now = londonNow();
  var mins = now.h * 60 + now.min;
  $$("[data-open-status]").forEach(function (el) {
    var text = $("[data-status-text]", el);
    var weekday = now.dow >= 1 && now.dow <= 5;
    var open = weekday && mins >= 540 && mins < 1050;
    var msg;
    if (open) msg = T.open + " · " + T.closes;
    else if (weekday && mins < 540) msg = T.closed + " · " + T.opensToday;
    else if (now.dow >= 1 && now.dow <= 4) msg = T.closed + " · " + T.opensTomorrow;
    else msg = T.closed + " · " + T.opensMonday;
    el.classList.add(open ? "is-open" : "is-closed");
    if (text && T.open) text.textContent = msg;
  });

  // ---------------------------------------------------------------- HMRC deadlines
  function utc(y, m, d) { return new Date(Date.UTC(y, m - 1, d)); }
  var today = utc(now.y, now.m, now.d);
  function fmt(date, opts) { return new Intl.DateTimeFormat(LOCALE, Object.assign({ timeZone: "UTC" }, opts)).format(date); }
  function longDate(date) { return fmt(date, { day: "numeric", month: "long", year: "numeric" }); }
  function shortDate(date) { return fmt(date, { day: "numeric", month: "short", year: "numeric" }); }
  function ty(start) { return start + "/" + String(start + 1).slice(2); }
  function daysUntil(date) { return Math.round((date - today) / 864e5); }
  function inText(n) { return n === 0 ? T.today : n === 1 ? T.tomorrow : (T.inDays || "").replace("{n}", n); }
  function upcomingDeadlines(count) {
    var list = [];
    for (var y = now.y - 1; y <= now.y + 2; y++) {
      list.push({ date: utc(y, 1, 31), key: "jan", ty: ty(y - 2) });
      list.push({ date: utc(y, 7, 31), key: "jul", ty: ty(y - 1) });
      list.push({ date: utc(y, 10, 5), key: "oct5", ty: ty(y - 1) });
      list.push({ date: utc(y, 10, 31), key: "oct31", ty: ty(y - 1) });
    }
    return list.filter(function (d) { return d.date >= today; }).sort(function (a, b) { return a.date - b.date; }).slice(0, count);
  }
  if (T.dl) {
    var up = upcomingDeadlines(5);
    var label = function (d) { return T.dl[d.key].replace("{ty}", d.ty); };
    $$("[data-next-deadline]").forEach(function (el) {
      $("[data-dl-date]", el).textContent = longDate(up[0].date);
      $("[data-dl-in]", el).textContent = inText(daysUntil(up[0].date));
      el.title = label(up[0]);
      el.hidden = false;
    });
    var cd = $("[data-countdown]");
    if (cd) {
      var n = daysUntil(up[0].date);
      var nEl = $("[data-cd-days]", cd);
      nEl.setAttribute("data-count", n);
      nEl.textContent = n;
      if (!reduced && "IntersectionObserver" in window) { nEl.textContent = "0"; cio.observe(nEl); }
      $("[data-cd-unit]", cd).textContent = n === 1 ? T.day : T.days;
      $("[data-cd-until]", cd).textContent = (T.until || "{date}").replace("{date}", longDate(up[0].date));
      $("[data-cd-what]", cd).textContent = label(up[0]);
      var ol = $("[data-deadlines]", cd);
      ol.innerHTML = "";
      up.slice(1).forEach(function (d) {
        var li = document.createElement("li");
        li.innerHTML = '<span class="dl-d"></span><span class="dl-l"></span><span class="dl-in"></span>';
        $(".dl-d", li).textContent = shortDate(d.date);
        $(".dl-l", li).textContent = label(d);
        $(".dl-in", li).textContent = inText(daysUntil(d.date));
        ol.appendChild(li);
      });
    }
  }

  // ---------------------------------------------------------------- company deadline calculator
  function addMonths(date, k) {
    var y = date.getUTCFullYear(), m = date.getUTCMonth(), d = date.getUTCDate();
    var lastOfMonth = d === new Date(Date.UTC(y, m + 1, 0)).getUTCDate();
    var targetLast = new Date(Date.UTC(y, m + k + 1, 0)).getUTCDate();
    return new Date(Date.UTC(y, m + k, lastOfMonth ? targetLast : Math.min(d, targetLast)));
  }
  var calc = $("[data-ct-calc]"), out = $("[data-ct-out]");
  if (calc && out && T.calc) {
    var input = $("input", calc);
    input.value = (now.m > 3 ? now.y : now.y - 1) + "-03-31";
    var render = function () {
      var v = input.value.split("-");
      out.innerHTML = "";
      if (v.length !== 3) return;
      var ye = utc(+v[0], +v[1], +v[2]);
      var pay = new Date(addMonths(ye, 9).getTime() + 864e5);
      [["accounts", addMonths(ye, 9)], ["ctpay", pay], ["ct600", addMonths(ye, 12)]].forEach(function (row) {
        var div = document.createElement("div");
        div.innerHTML = "<dt></dt><dd></dd>";
        $("dt", div).textContent = T.calc[row[0]];
        $("dd", div).textContent = longDate(row[1]);
        out.appendChild(div);
      });
    };
    input.addEventListener("change", render);
    input.addEventListener("input", render);
    calc.addEventListener("submit", function (e) { e.preventDefault(); });
    render();
  }

  // ---------------------------------------------------------------- services table of contents
  var tocLinks = $$(".toc a[href^='#']");
  if (tocLinks.length && "IntersectionObserver" in window) {
    var byId = {};
    tocLinks.forEach(function (a) { byId[a.getAttribute("href").slice(1)] = a; });
    var tio = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        tocLinks.forEach(function (a) { a.classList.remove("is-active"); });
        var a = byId[en.target.id];
        if (!a) return;
        a.classList.add("is-active");
        if (window.innerWidth <= 900) a.closest("ul").scrollTo({ left: a.offsetLeft - 24, behavior: reduced ? "auto" : "smooth" });
      });
    }, { rootMargin: "-35% 0px -55% 0px" });
    $$(".svc-section").forEach(function (s) { tio.observe(s); });
  }

  // ---------------------------------------------------------------- contact form → email app
  var form = $("[data-contact-form]");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var f = form.elements, ok = true;
      ["name", "email", "message"].forEach(function (k) {
        var bad = !f[k].value.trim() || (k === "email" && !/^\S+@\S+\.\S+$/.test(f[k].value));
        f[k].setAttribute("aria-invalid", bad ? "true" : "false");
        if (bad) ok = false;
      });
      $("[data-form-error]", form).hidden = ok;
      if (!ok) return;
      var body = [
        f.message.value.trim(), "", "—",
        T.mailName + ": " + f.name.value.trim(),
        "Email: " + f.email.value.trim(),
        f.phone.value.trim() ? T.mailPhone + ": " + f.phone.value.trim() : null,
        T.mailService + ": " + f.service.value,
        T.mailLang + ": " + f.lang.value
      ].filter(function (l) { return l !== null; }).join("\n");
      var subject = T.mailSubject + " — " + f.service.value + " — " + f.name.value.trim();
      window.location.href = "mailto:info@kyaccountancy.com?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(body);
    });
  }
})();
