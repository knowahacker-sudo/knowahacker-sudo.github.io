// ...existing script...

// Add loader animation
document.addEventListener('DOMContentLoaded', function() {
    const loader = document.createElement('div');
    loader.className = 'loader';
    loader.innerHTML = '<div class="spinner"></div>';
    document.body.appendChild(loader);
    
    // Hide loader after page load
    window.addEventListener('load', function() {
        loader.style.opacity = '0';
        setTimeout(() => loader.remove(), 500);
    });
});

// Add ripple effect to buttons
document.addEventListener('click', function(e) {
    if (e.target.matches('.ripple')) {
        const ripple = document.createElement('span');
        ripple.className = 'ripple';
        e.target.appendChild(ripple);
        
        setTimeout(() => ripple.remove(), 600);
    }
});

// Add smooth scrolling
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});
