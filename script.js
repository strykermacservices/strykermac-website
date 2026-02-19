// Nav scroll effect
const nav = document.getElementById('nav');
window.addEventListener('scroll', () => {
    nav.classList.toggle('scrolled', window.scrollY > 20);
});

// Hamburger menu
const hamburger = document.getElementById('hamburger');
const navLinks = document.getElementById('navLinks');
hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('active');
    navLinks.classList.toggle('open');
});
// Close menu on link click
navLinks.querySelectorAll('a').forEach(a => {
    a.addEventListener('click', () => {
        hamburger.classList.remove('active');
        navLinks.classList.remove('open');
    });
});

// Fade-in on scroll
const observer = new IntersectionObserver((entries) => {
    entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('visible'); observer.unobserve(e.target); } });
}, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });
document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));

// FAQ accordion
document.querySelectorAll('.faq-question').forEach(btn => {
    btn.addEventListener('click', () => {
        const item = btn.parentElement;
        const wasActive = item.classList.contains('active');
        document.querySelectorAll('.faq-item.active').forEach(i => i.classList.remove('active'));
        if (!wasActive) item.classList.add('active');
    });
});
