/** @odoo-module **/

document.addEventListener('DOMContentLoaded', () => {

    // ── Navbar scroll state ──────────────────────────────────────────────────

    const navbar = document.getElementById('top');

    if (navbar) {
        const SCROLL_THRESHOLD = 10;

        const updateScrollState = () => {
            if (window.scrollY > SCROLL_THRESHOLD) {
                navbar.classList.add('is-scrolled');
            } else {
                navbar.classList.remove('is-scrolled');
            }
        };

        window.addEventListener('scroll', updateScrollState, { passive: true });
        updateScrollState();
    }

    // ── Hamburger animation ──────────────────────────────────────────────────
    // Bootstrap 5 handles collapse toggling natively. We just mirror the open
    // state onto .crioco-navbar so the hamburger → X CSS transition fires.

    const toggler = document.querySelector('.crioco-navbar .navbar-toggler');
    const collapse = document.querySelector('.crioco-navbar .navbar-collapse');

    if (toggler && collapse && navbar) {
        // Bootstrap fires these events on the collapse element
        collapse.addEventListener('show.bs.collapse', () => {
            navbar.classList.add('nav-open');
        });
        collapse.addEventListener('hide.bs.collapse', () => {
            navbar.classList.remove('nav-open');
        });
    }

    // ── Story image fallback ──────────────────────────────────────────────────
    // Show the CSS gradient fallback div when the placeholder image is missing.

    const storyImg = document.querySelector('.crioco-story__img');
    if (storyImg) {
        storyImg.addEventListener('error', () => {
            storyImg.style.display = 'none';
            const fallback = storyImg.nextElementSibling;
            if (fallback && fallback.classList.contains('crioco-story__img-fallback')) {
                fallback.style.display = 'block';
            }
        });
    }

    // ── Fade-in on scroll ────────────────────────────────────────────────────
    // Any element with [data-crioco-fade] fades up when it enters the viewport.
    // Usage in QWeb: <div data-crioco-fade="true">...</div>

    const fadeEls = document.querySelectorAll('[data-crioco-fade]');

    if (fadeEls.length > 0 && 'IntersectionObserver' in window) {
        const observer = new IntersectionObserver(
            (entries) => {
                entries.forEach((entry) => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('crioco-fade-in');
                        observer.unobserve(entry.target);
                    }
                });
            },
            { threshold: 0.12, rootMargin: '0px 0px -40px 0px' }
        );

        fadeEls.forEach((el) => observer.observe(el));
    } else {
        // No IntersectionObserver (old browser) — show everything immediately
        fadeEls.forEach((el) => el.classList.add('crioco-fade-in'));
    }

});
