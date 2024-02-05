document.addEventListener('DOMContentLoaded', function () {
    const menuToggle = document.querySelector('.menu-toggle');
    const nav = document.querySelector('nav');

    menuToggle.addEventListener('click', function () {
      nav.classList.toggle('active');
    });

    $('.carousel').slick({
        autoplay: true,
        autoplaySpeed: 2000,
        arrows: false,
        dots: true,
    });    
  });