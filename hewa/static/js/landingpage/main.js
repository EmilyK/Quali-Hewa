/*================================================================*/
/*  Custom Functions
/*================================================================*/
function loader() {
    $(".status").fadeOut(); 
    $(".preloader").delay(1000).fadeOut("slow");
}

function navScroll() {
    $('.main-navigation').onePageNav({
        scrollThreshold: 0.2, // Adjust if Navigation highlights too early or too late
    });
}

function centeredHeader() {
    var windowHeight = $(window).height();

    $(".full-screen").css('min-height', windowHeight);

    var centerContent = ($(window).height() / 2) - ($('.header-content').height());
    $('.primary-row').css('padding-top', centerContent);
}

function smoothScrollonTop() {
    var scrollAnimationTime = 1200,
    scrollAnimation = 'easeInOutExpo';

    $('a.scrollto').bind('click.smoothscroll', function (event) {
        event.preventDefault();
        var target = this.hash;
        $('html, body').stop().animate({
            'scrollTop': $(target).offset().top
        }, scrollAnimationTime, scrollAnimation, function () {
            window.location.hash = target;
        });
    });
}

function wowAnimation() {
    new WOW().init();
}

function owlInit() {
    $("#feedbacks").owlCarousel({

        navigation: false, // Show next and prev buttons
        slideSpeed: 800,
        paginationSpeed: 400,
        autoPlay: 5000,
        singleItem: true
    });

    var owl = $("#screenshots");

    owl.owlCarousel({
        items: 4, //10 items above 1000px browser width
        itemsDesktop: [1000, 4], //5 items between 1000px and 901px
        itemsDesktopSmall: [900, 2], // betweem 900px and 601px
        itemsTablet: [600, 1], //2 items between 600 and 0
        itemsMobile: false // itemsMobile disabled - inherit from itemsTablet option
    });
}

function nivoLightboxInit() {
    $('#screenshots a').nivoLightbox({
        effect: 'fadeScale',
    });
}

function ie10Fix() {
    if (navigator.userAgent.match(/IEMobile\/10\.0/)) {
      var msViewportStyle = document.createElement('style')
      msViewportStyle.appendChild(
        document.createTextNode(
          '@-ms-viewport{width:auto!important}'
        )
      )
      document.querySelector('head').appendChild(msViewportStyle)
    }
}

/*================================================================*/
/*  Let's initialize shall we?
/*================================================================*/
$(document).ready(function () {
    "use strict";

    // navScroll();
    centeredHeader();
    smoothScrollonTop();
    wowAnimation();
    owlInit();
    nivoLightboxInit();
    // subscriptionForm();
    // contactForm();
    ie10Fix();

    //$(window).bind('resize', centeredHeader);
});

$(window).load(function () {
    "use strict";

    loader();

});

$(window).scroll(function () {
    "use strict";

});

$(window).resize(function(){
    centeredHeader();
});