/* KY Accountancy — menu, open-now status, HMRC deadlines, company date calculator, contact form */
(function () {
  var T = window.KY || {};
  var LANG = document.documentElement.lang || "en-GB";
  var LOCALE = LANG.indexOf("zh") === 0 ? "zh-CN" : LANG.indexOf("ko") === 0 ? "ko-KR" : "en-GB";

  // ---- mobile menu
  var btn = document.querySelector(".menu-btn");
  var nav = document.getElementById("main-nav");
  if (btn && nav) {
    btn.addEventListener("click", function () {
      var open = btn.getAttribute("aria-expanded") === "true";
      btn.setAttribute("aria-expanded", String(!open));
      nav.classList.toggle("is-open", !open);
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.classList.contains("is-open")) { btn.click(); btn.focus(); }
    });
  }

  document.querySelectorAll("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });

  // ---- London time helpers
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

  // ---- open now (Mon–Fri 9:00–17:30)
  var now = londonNow();
  var mins = now.h * 60 + now.min;
  document.querySelectorAll("[data-open-status]").forEach(function (el) {
    var text = el.querySelector("[data-status-text]");
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

  // ---- dates
  function utc(y, m, d) { return new Date(Date.UTC(y, m - 1, d)); }
  var today = utc(now.y, now.m, now.d);
  function fmt(date, opts) {
    return new Intl.DateTimeFormat(LOCALE, Object.assign({ timeZone: "UTC" }, opts)).format(date);
  }
  function longDate(date) { return fmt(date, { day: "numeric", month: "long", year: "numeric" }); }
  function ty(start) { return start + "/" + String(start + 1).slice(2); }
  function daysUntil(date) { return Math.round((date - today) / 864e5); }
  function inText(n) {
    if (n === 0) return T.today;
    if (n === 1) return T.tomorrow;
    return (T.inDays || "").replace("{n}", n);
  }

  function upcomingDeadlines(count) {
    var list = [];
    for (var y = now.y - 1; y <= now.y + 2; y++) {
      list.push({ date: utc(y, 1, 31), key: "jan", ty: ty(y - 2) });
      list.push({ date: utc(y, 7, 31), key: "jul", ty: ty(y - 1) });
      list.push({ date: utc(y, 10, 5), key: "oct5", ty: ty(y - 1) });
      list.push({ date: utc(y, 10, 31), key: "oct31", ty: ty(y - 1) });
    }
    return list.filter(function (d) { return d.date >= today; })
      .sort(function (a, b) { return a.date - b.date; }).slice(0, count);
  }

  if (T.dl) {
    var upcoming = upcomingDeadlines(4);
    document.querySelectorAll("[data-next-deadline]").forEach(function (el) {
      var d = upcoming[0];
      el.querySelector("[data-dl-date]").textContent = longDate(d.date);
      el.querySelector("[data-dl-label]").textContent = T.dl[d.key].replace("{ty}", d.ty);
      el.querySelector("[data-dl-in]").textContent = inText(daysUntil(d.date));
      el.hidden = false;
    });
    document.querySelectorAll("[data-deadlines]").forEach(function (ol) {
      ol.innerHTML = "";
      upcoming.forEach(function (d) {
        var li = document.createElement("li");
        li.innerHTML = '<span class="dl-date"><b></b><small></small></span><span class="dl-label"></span><span class="dl-in"></span>';
        li.querySelector("b").textContent = d.date.getUTCDate();
        li.querySelector("small").textContent = fmt(d.date, { month: "short", year: "numeric" });
        li.querySelector(".dl-label").textContent = T.dl[d.key].replace("{ty}", d.ty);
        li.querySelector(".dl-in").textContent = inText(daysUntil(d.date));
        ol.appendChild(li);
      });
    });
  }

  // ---- company deadline calculator
  function addMonths(date, n) {
    var y = date.getUTCFullYear(), m = date.getUTCMonth(), d = date.getUTCDate();
    var lastOfMonth = d === new Date(Date.UTC(y, m + 1, 0)).getUTCDate();
    var targetLast = new Date(Date.UTC(y, m + n + 1, 0)).getUTCDate();
    return new Date(Date.UTC(y, m + n, lastOfMonth ? targetLast : Math.min(d, targetLast)));
  }
  var calc = document.querySelector("[data-ct-calc]");
  var out = document.querySelector("[data-ct-out]");
  if (calc && out && T.calc) {
    var input = calc.querySelector("input");
    // default to the most recent 31 March before today
    var defYear = now.m > 3 ? now.y : now.y - 1;
    input.value = defYear + "-03-31";
    function render() {
      var v = input.value.split("-");
      if (v.length !== 3) { out.innerHTML = ""; return; }
      var ye = utc(+v[0], +v[1], +v[2]);
      var accounts = addMonths(ye, 9);
      var pay = addMonths(ye, 9); pay = new Date(pay.getTime() + 864e5);
      var ct600 = addMonths(ye, 12);
      out.innerHTML = "";
      [["accounts", accounts], ["ctpay", pay], ["ct600", ct600]].forEach(function (row) {
        var div = document.createElement("div");
        div.innerHTML = "<dt></dt><dd></dd>";
        div.querySelector("dt").textContent = T.calc[row[0]];
        div.querySelector("dd").textContent = longDate(row[1]);
        out.appendChild(div);
      });
    }
    input.addEventListener("change", render);
    input.addEventListener("input", render);
    calc.addEventListener("submit", function (e) { e.preventDefault(); });
    render();
  }

  // ---- services table of contents highlight
  var tocLinks = document.querySelectorAll(".toc a[href^='#']");
  if (tocLinks.length && "IntersectionObserver" in window) {
    var byId = {};
    tocLinks.forEach(function (a) { byId[a.getAttribute("href").slice(1)] = a; });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          tocLinks.forEach(function (a) { a.classList.remove("is-active"); });
          var a = byId[en.target.id];
          if (a) {
            a.classList.add("is-active");
            if (a.scrollIntoView && window.innerWidth <= 960) {
              var ul = a.closest("ul");
              ul.scrollTo({ left: a.offsetLeft - 16, behavior: "smooth" });
            }
          }
        }
      });
    }, { rootMargin: "-30% 0px -60% 0px" });
    document.querySelectorAll(".svc-section").forEach(function (s) { io.observe(s); });
  }

  // ---- contact form → email app
  var form = document.querySelector("[data-contact-form]");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var f = form.elements;
      var ok = true;
      ["name", "email", "message"].forEach(function (k) {
        var bad = !f[k].value.trim() || (k === "email" && !/^\S+@\S+\.\S+$/.test(f[k].value));
        f[k].setAttribute("aria-invalid", bad ? "true" : "false");
        if (bad) ok = false;
      });
      form.querySelector("[data-form-error]").hidden = ok;
      if (!ok) return;
      var body = [
        f.message.value.trim(), "",
        "—",
        T.mailName + ": " + f.name.value.trim(),
        "Email: " + f.email.value.trim(),
        f.phone.value.trim() ? T.mailPhone + ": " + f.phone.value.trim() : "",
        T.mailService + ": " + f.service.value,
        T.mailLang + ": " + f.lang.value
      ].filter(function (l, i) { return l !== "" || i === 1; }).join("\n");
      var subject = T.mailSubject + " — " + f.service.value + " — " + f.name.value.trim();
      window.location.href = "mailto:info@kyaccountancy.com?subject=" + encodeURIComponent(subject) +
        "&body=" + encodeURIComponent(body);
    });
  }

  // ---- gentle reveal on scroll
  if ("IntersectionObserver" in window && !matchMedia("(prefers-reduced-motion: reduce)").matches) {
    var targets = document.querySelectorAll(".svc-card, .steps li, .panel, .values li, .news-item, .svc-section, .qr");
    var rio = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("is-in"); rio.unobserve(en.target); }
      });
    }, { rootMargin: "0px 0px -8% 0px" });
    targets.forEach(function (t) {
      if (t.getBoundingClientRect().top > window.innerHeight) { t.classList.add("reveal"); rio.observe(t); }
    });
  }
})();
