// Animations init
new WOW().init();





// Smooth Scrolling
$("#main-nav a").on('click', function (event) {
  if (this.hash !== "") {
    event.preventDefault();

    const hash = this.hash;

    $('html, body').animate({
      scrollTop: $(hash).offset().top
    }, 800, function () {

      window.location.hash = hash;
    });
  }
});






// Init Scrollspy
$('body').scrollspy({ target: '#main-nav' });




$('.navbar-nav>li>a').on('click', function () {
  $('.navbar-collapse').collapse('hide');
});





// Option 2
$('.showcase .main-btn').on('click', function (e) {
  if (this.hash !== '') {
    e.preventDefault();

    const hash = this.hash;

    $('html, body').animate(
      {
        scrollTop: $(hash).offset().top
      },
      800
    );
  }
});






$('.navbar-brand').on('click', function () {
  $('.navbar-collapse').collapse('hide');
});