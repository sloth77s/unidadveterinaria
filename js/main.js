/* ================================================
   UCIVET — main.js
   Vanilla JS, no dependencies
   ================================================ */

(function () {
  'use strict';

  /* ── DOM refs ─────────────────────────────────── */
  const header      = document.querySelector('.header');
  const nav         = document.querySelector('.nav__links');
  const toggle      = document.querySelector('.nav__toggle');
  const menuOverlay = document.querySelector('.menu-overlay');
  const cookieBanner = document.querySelector('.cookie-banner');
  const cookieAccept = document.querySelector('.cookie-accept');
  const cookieReject = document.querySelector('.cookie-reject');
  const dropdownToggles = document.querySelectorAll('.has-dropdown > a');
  const faqItems    = document.querySelectorAll('.faq-item');
  const revealEls   = document.querySelectorAll('[data-reveal]');
  const counters    = document.querySelectorAll('[data-count]');
  const yearSpan    = document.getElementById('year');
  const backToTop   = document.getElementById('backToTop');

  /* ── Current year ─────────────────────────────── */
  if (yearSpan) yearSpan.textContent = new Date().getFullYear();

  /* ── Mobile menu ──────────────────────────────── */
  function openMenu() {
    nav.classList.add('active');
    toggle.classList.add('active');
    if (menuOverlay) menuOverlay.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeMenu() {
    nav.classList.remove('active');
    toggle.classList.remove('active');
    if (menuOverlay) menuOverlay.classList.remove('active');
    document.body.style.overflow = '';
  }

  if (toggle) {
    toggle.addEventListener('click', function () {
      nav.classList.contains('active') ? closeMenu() : openMenu();
    });
  }

  if (menuOverlay) {
    menuOverlay.addEventListener('click', closeMenu);
  }

  /* close menu on nav link click */
  document.querySelectorAll('.nav__links a').forEach(function (link) {
    link.addEventListener('click', closeMenu);
  });

  /* ── Dropdown navigation ──────────────────────── */
  dropdownToggles.forEach(function (toggle) {
    toggle.addEventListener('click', function (e) {
      var parent = this.closest('.has-dropdown');
      var isOpen = parent.classList.contains('open');

      /* close all other dropdowns */
      document.querySelectorAll('.has-dropdown.open').forEach(function (dd) {
        if (dd !== parent) dd.classList.remove('open');
      });

      parent.classList.toggle('open', !isOpen);
      e.preventDefault();
    });
  });

  /* close dropdowns on outside click */
  document.addEventListener('click', function (e) {
    if (!e.target.closest('.has-dropdown')) {
      document.querySelectorAll('.has-dropdown.open').forEach(function (dd) {
        dd.classList.remove('open');
      });
    }
  });

  /* ── Scroll-based header ──────────────────────── */
  var lastScroll = 0;
  window.addEventListener('scroll', function () {
    var st = window.pageYOffset || document.documentElement.scrollTop;
    if (header) {
      header.classList.toggle('scrolled', st > 80);
    }
    lastScroll = st;
  }, { passive: true });

  /* ── FAQ accordion ────────────────────────────── */
  faqItems.forEach(function (item) {
    var btn = item.querySelector('.faq-question');
    var answer = item.querySelector('.faq-answer');
    var icon = item.querySelector('.faq-icon');

    if (!btn) return;

    btn.addEventListener('click', function () {
      var isOpen = item.classList.contains('open');

      /* close all other items */
      faqItems.forEach(function (other) {
        if (other !== item) {
          other.classList.remove('open');
          var otherAnswer = other.querySelector('.faq-answer');
          if (otherAnswer) otherAnswer.style.maxHeight = null;
          var otherIcon = other.querySelector('.faq-icon');
          if (otherIcon) otherIcon.textContent = '+';
        }
      });

      /* toggle current */
      item.classList.toggle('open', !isOpen);
      if (answer) {
        answer.style.maxHeight = isOpen ? null : answer.scrollHeight + 'px';
      }
      if (icon) {
        icon.textContent = isOpen ? '+' : '−';
      }
    });
  });

  /* ── Cookie banner V3 ─────────────────────────── */
  if (cookieBanner && !localStorage.getItem('ucivet_cookie_consent')) {
    setTimeout(function() {
      cookieBanner.classList.remove('hidden', 'opacity-0');
      cookieBanner.classList.add('opacity-100');
    }, 500);
  }

  function hideCookieBanner(consent) {
    if (cookieBanner) {
      localStorage.setItem('ucivet_cookie_consent', consent);
      cookieBanner.classList.remove('opacity-100');
      cookieBanner.classList.add('opacity-0');
      setTimeout(function() {
        cookieBanner.classList.add('hidden');
      }, 300);
    }
  }

  if (cookieAccept) {
    cookieAccept.addEventListener('click', function () { hideCookieBanner('accepted'); });
  }

  if (cookieReject) {
    cookieReject.addEventListener('click', function () { hideCookieBanner('rejected'); });
  }

  /* ── IntersectionObserver — scroll reveal ──────── */
  if ('IntersectionObserver' in window && revealEls.length) {
    var revealObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('revealed');
          revealObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

    revealEls.forEach(function (el) { revealObserver.observe(el); });
  } else {
    /* fallback: show everything immediately */
    revealEls.forEach(function (el) { el.classList.add('revealed'); });
  }

  /* ── Counter animation ────────────────────────── */
  if (counters.length) {
    function animateCounter(el) {
      var target = parseInt(el.getAttribute('data-count'), 10);
      var duration = 1800;
      var start = 0;
      var startTime = null;

      function step(ts) {
        if (!startTime) startTime = ts;
        var progress = Math.min((ts - startTime) / duration, 1);
        var eased = 1 - Math.pow(1 - progress, 3);          /* ease-out cubic */
        el.textContent = Math.floor(eased * target);
        if (progress < 1) requestAnimationFrame(step);
      }
      requestAnimationFrame(step);
    }

    var counterObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          animateCounter(entry.target);
          counterObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.5 });

    counters.forEach(function (el) { counterObserver.observe(el); });
  }

  /* ── Back to top ──────────────────────────────── */
  if (backToTop) {
    window.addEventListener('scroll', function () {
      backToTop.classList.toggle('visible', window.pageYOffset > 600);
    }, { passive: true });

    backToTop.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  /* ── Smooth scroll for anchor links ───────────── */
  document.querySelectorAll('a[href^="#"]').forEach(function (link) {
    link.addEventListener('click', function (e) {
      var target = document.querySelector(this.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

  /* ── Active nav highlight on scroll ───────────── */
  var sections = document.querySelectorAll('section[id]');
  if (sections.length) {
    var sectionObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          var id = entry.target.getAttribute('id');
          document.querySelectorAll('.nav__links a').forEach(function (a) {
            a.classList.toggle('active', a.getAttribute('href') === '#' + id);
          });
        }
      });
    }, { threshold: 0.35 });

    sections.forEach(function (s) { sectionObserver.observe(s); });
  }

})();
