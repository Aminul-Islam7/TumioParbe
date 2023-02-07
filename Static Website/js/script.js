AOS.init({
  disable: true,
  // Settings that can be overridden on per-element basis, by `data-aos-*` attributes:
  offset: 100, // offset (in px) from the original trigger point
  delay: 100, // values from 0 to 3000, with step 50ms
  duration: 600, // values from 0 to 3000, with step 50ms
  easing: "ease-in", // default easing for AOS animations
  once: false, // whether animation should happen only once - while scrolling down
  mirror: true, // whether elements should animate out while scrolling past them
  anchorPlacement: "top-bottom", // defines which position of the element regarding to window should trigger the animation
});

document
  .querySelectorAll("img")
  .forEach((img) => img.addEventListener("load", () => AOS.refresh()));

$(document).ready(function () {
  let section = document.querySelectorAll("section");
  let navLinks = document.querySelectorAll("nav li");

  window.onscroll = () => {
    section.forEach((sec) => {
      let top = window.scrollY;
      let offset = sec.offsetTop - 300;
      let height = sec.offsetHeight;
      let id = sec.getAttribute("id");

      if (top >= offset && top < offset + height) {
        navLinks.forEach((links) => {
          links.classList.remove("active");
          document
            .querySelector("nav li a[href*=" + id + "]")
            .parentElement.classList.add("active");
        });
      }
    });
  };
});

// $(document).ready(function () {
//   $(".nav-item").click(function () {
//     $(".nav-item").removeClass("active");
//     // $(".nav-item .icon i").removeClass("fa-solid");
//     // $(".nav-item .icon i").addClass("fa-light");
//     $(this).addClass("active");
//     // $(this).find(".icon i").addClass("fa-solid");
//   });
// });

$(document).ready(function () {
  var $obj = lc_lightbox(".resource-files a", {
    slideshow_time: 4000,
    skin: "minimal",
    fullscreen: true,
    gallery: false,
    img_zoom: true,
    download: true,
  });
});

$(".award-slider").slick({
  infinite: true,
  arrows: false,
  dots: true,
  speed: 500,
  autoplay: true,
  autoplaySpeed: 1000,
  easing: "swing",
  swipeToSlide: true,
  touchThreshold: 100,
  edgeFriction: 0.1,
  lazyLoad: "ondemand",
  accessibility: true,
  pauseOnFocus: false,
  pauseOnHover: false,
  variableWidth: true,
  responsive: [
    {
      breakpoint: 576,
      settings: {
        slidesToShow: 1,
        variableWidth: false,
        adaptiveHeight: true,
      },
    },
    {
      breakpoint: 768,
      settings: {
        slidesToShow: 2,
      },
    },
    {
      breakpoint: 992,
      settings: {
        slidesToShow: 2,
      },
    },
    {
      breakpoint: 1200,
      settings: {
        slidesToShow: 3,
      },
    },
  ],
});

$(document).ready(function () {
  var $obj = lc_lightbox(".award-slider a");

  if ($("#navbar").attr("hide") == "no") {
    $("#navbar").addClass("move-up");
  }
  if ($("#logo-bar").attr("hide") == "no") {
    $("#logo-bar").show();
  }
});

$(window).scroll(function () {
  let height = $(window).scrollTop();
  if (height > 100 || $("#navbar").attr("hide") == "no") {
    $("#navbar").addClass("move-up");
    $("#logo-bar").fadeIn();
  } else {
    $("#navbar").removeClass("move-up");
    $("#logo-bar").fadeOut();
  }

  var scrollHeight = $(document).height();
  var scrollPosition = $(window).height() + $(window).scrollTop();
  if ((scrollHeight - scrollPosition) / scrollHeight === 0) {
    $("#logo-bar").fadeOut();
  }

  $("a[class='eapps-link").hide();
  $(
    "a[href='https://elfsight.com/youtube-channel-plugin-yottie/?utm_source=websites&utm_medium=clients&utm_content=yottie&utm_term=%website_domain%&utm_campaign=free-widget']"
  ).hide();
});
