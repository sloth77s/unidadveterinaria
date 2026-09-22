// UCIVET - Shared UI Components
// Mobile menu, dropdown navigation, cookie banner

(function() {
  'use strict';

  // ========== Mobile Menu ==========
  function initMobileMenu() {
    const mobileMenuBtn = document.getElementById('mobileMenuBtn');
    const mobileMenu = document.getElementById('mobileMenu');
    if (mobileMenuBtn && mobileMenu) {
      mobileMenuBtn.addEventListener('click', () => {
        mobileMenu.classList.toggle('hidden');
      });
    }

    // Mobile specialties submenu
    const mobileSpecBtn = document.getElementById('mobileSpecBtn');
    const mobileSpecList = document.getElementById('mobileSpecList');
    const mobileSpecArrow = document.getElementById('mobileSpecArrow');
    if (mobileSpecBtn && mobileSpecList) {
      mobileSpecBtn.addEventListener('click', () => {
        mobileSpecList.classList.toggle('hidden');
        if (mobileSpecArrow) {
          mobileSpecArrow.classList.toggle('rotate-180');
        }
      });
    }
  }

  // ========== Desktop Dropdown ==========
  function initDesktopDropdown() {
    const dropdownToggles = document.querySelectorAll('.relative.group > button');
    dropdownToggles.forEach(function(toggle) {
      toggle.addEventListener('click', function(e) {
        const parent = this.closest('.relative.group');
        const isOpen = parent.classList.contains('open');

        // Close all other dropdowns
        document.querySelectorAll('.relative.group.open').forEach(function(dd) {
          if (dd !== parent) dd.classList.remove('open');
        });

        parent.classList.toggle('open', !isOpen);
        e.preventDefault();
      });
    });

    // Close dropdowns on outside click
    document.addEventListener('click', function(e) {
      if (!e.target.closest('.relative.group')) {
        document.querySelectorAll('.relative.group.open').forEach(function(dd) {
          dd.classList.remove('open');
        });
      }
    });
  }

  // ========== Cookie Banner (GDPR) ==========
  function initCookieBanner() {
    const cookieBanner = document.getElementById('cookieBanner');
    const cookieAccept = document.getElementById('cookieAccept');
    const cookieReject = document.getElementById('cookieReject');

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
      cookieAccept.addEventListener('click', function() { hideCookieBanner('accepted'); });
    }
    if (cookieReject) {
      cookieReject.addEventListener('click', function() { hideCookieBanner('rejected'); });
    }
  }

  // ========== FAQ Accordion ==========
  function initFAQAccordion() {
    const faqItems = document.querySelectorAll('.faq-item');
    faqItems.forEach(function(item) {
      const btn = item.querySelector('.faq-question');
      const answer = item.querySelector('.faq-answer');
      const icon = item.querySelector('.faq-icon');

      if (!btn) return;

      btn.addEventListener('click', function() {
        const isOpen = item.classList.contains('open');

        // Close all other items
        faqItems.forEach(function(other) {
          if (other !== item) {
            other.classList.remove('open');
            const otherAnswer = other.querySelector('.faq-answer');
            if (otherAnswer) otherAnswer.style.maxHeight = null;
            const otherIcon = other.querySelector('.faq-icon');
            if (otherIcon) otherIcon.textContent = '+';
          }
        });

        // Toggle current
        item.classList.toggle('open', !isOpen);
        if (answer) {
          answer.style.maxHeight = isOpen ? null : answer.scrollHeight + 'px';
        }
        if (icon) {
          icon.textContent = isOpen ? '+' : '−';
        }
      });
    });
  }

  // ========== Scroll Reveal ==========
  function initScrollReveal() {
    const revealEls = document.querySelectorAll('[data-reveal]');
    if ('IntersectionObserver' in window && revealEls.length) {
      const revealObserver = new IntersectionObserver(function(entries) {
        entries.forEach(function(entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('revealed');
            revealObserver.unobserve(entry.target);
          }
        });
      }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

      revealEls.forEach(function(el) { revealObserver.observe(el); });
    } else {
      revealEls.forEach(function(el) { el.classList.add('revealed'); });
    }
  }

  // ========== Counter Animation ==========
  function initCounters() {
    const counters = document.querySelectorAll('[data-count]');
    if (counters.length) {
      function animateCounter(el) {
        const target = parseInt(el.getAttribute('data-count'), 10);
        const duration = 1800;
        let startTime = null;

        function step(ts) {
          if (!startTime) startTime = ts;
          const progress = Math.min((ts - startTime) / duration, 1);
          const eased = 1 - Math.pow(1 - progress, 3);
          el.textContent = Math.floor(eased * target);
          if (progress < 1) requestAnimationFrame(step);
        }
        requestAnimationFrame(step);
      }

      const counterObserver = new IntersectionObserver(function(entries) {
        entries.forEach(function(entry) {
          if (entry.isIntersecting) {
            animateCounter(entry.target);
            counterObserver.unobserve(entry.target);
          }
        });
      }, { threshold: 0.5 });

      counters.forEach(function(el) { counterObserver.observe(el); });
    }
  }

  // ========== Back to Top ==========
  function initBackToTop() {
    const backToTop = document.getElementById('backToTop');
    if (backToTop) {
      window.addEventListener('scroll', function() {
        backToTop.classList.toggle('visible', window.pageYOffset > 600);
      }, { passive: true });

      backToTop.addEventListener('click', function() {
        window.scrollTo({ top: 0, behavior: 'smooth' });
      });
    }
  }

  // ========== Smooth Scroll for Anchor Links ==========
  function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(function(link) {
      link.addEventListener('click', function(e) {
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
          e.preventDefault();
          target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      });
    });
  }

  // ========== Active Nav on Scroll ==========
  function initActiveNav() {
    const sections = document.querySelectorAll('section[id]');
    if (sections.length) {
      const sectionObserver = new IntersectionObserver(function(entries) {
        entries.forEach(function(entry) {
          if (entry.isIntersecting) {
            const id = entry.target.getAttribute('id');
            document.querySelectorAll('.nav__links a').forEach(function(a) {
              a.classList.toggle('active', a.getAttribute('href') === '#' + id);
            });
          }
        });
      }, { threshold: 0.35 });

      sections.forEach(function(s) { sectionObserver.observe(s); });
    }
  }

  // ========== Header Scroll Effect ==========
  function initHeaderScroll() {
    const header = document.querySelector('.site-header, header.sticky');
    if (header) {
      window.addEventListener('scroll', function() {
        const st = window.pageYOffset || document.documentElement.scrollTop;
        header.classList.toggle('scrolled', st > 80);
      }, { passive: true });
    }
  }

  // ========== Initialize All ==========
  function init() {
    initMobileMenu();
    initDesktopDropdown();
    initCookieBanner();
    initFAQAccordion();
    initScrollReveal();
    initCounters();
    initBackToTop();
    initSmoothScroll();
    initActiveNav();
    initHeaderScroll();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  // Export for manual initialization if needed
  window.UCIVET = {
    initMobileMenu,
    initDesktopDropdown,
    initCookieBanner,
    initFAQAccordion,
    initScrollReveal,
    initCounters,
    initBackToTop,
    initSmoothScroll,
    initActiveNav,
    initHeaderScroll
  };
})();