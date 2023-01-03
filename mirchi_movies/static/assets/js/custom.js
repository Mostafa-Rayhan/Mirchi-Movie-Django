// swiper slider js (carousel-slider-sec)
var swiper = new Swiper(".popularImageBox", {
        effect: "coverflow",
        grabCursor: true,
        centeredSlides: true,
        slidesPerView: "auto",
        coverflowEffect: {
              rotate: 50,
              stretch: 0,
              depth: 100,
              modifier: 1,
              slideShadows: true
        },
        pagination: {
              el: ".swiper-pagination"
        }
});

// owl carousel starts (carousel-slider-sec)
$(document).ready(function() {
  $('.owl-carousel').owlCarousel({

        margin:20,
        nav:true,
        dots:false,
        autoplay:true,
        responsive:{
            0:{
                items:1,
                nav:false,
                dots:true
            },
            600:{
                items:2
            },
            1000:{
                items:4
            }
        }
    });
});
