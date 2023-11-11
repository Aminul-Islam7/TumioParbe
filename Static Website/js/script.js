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

// function addDarkmodeWidget() {
// 	new Darkmode().showWidget();
// }
// window.addEventListener("load", addDarkmodeWidget);

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
	speed: 3000,
	autoplay: true,
	autoplaySpeed: 0,
	easing: "swing",
	swipeToSlide: true,
	touchThreshold: 100,
	edgeFriction: 0.1,
	lazyLoad: "ondemand",
	accessibility: true,
	pauseOnFocus: false,
	pauseOnHover: true,
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
	$(".eapps-link").hide();
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

	$(".eapps-link").addClass();
	$("a[class='eapps-link").hide();
	$(
		"a[href='https://elfsight.com/youtube-channel-plugin-yottie/?utm_source=websites&utm_medium=clients&utm_content=yottie&utm_term=%website_domain%&utm_campaign=free-widget']"
	).hide();
});

document.addEventListener("DOMContentLoaded", function () {
	// Check for the link periodically (every 100 milliseconds in this example)
	var intervalId = setInterval(function () {
		var elfsightLink = document.querySelector(
			'a[href^="https://elfsight.com/youtube-channel-plugin-yottie/"]'
		);

		if (elfsightLink) {
			elfsightLink.parentNode.removeChild(elfsightLink);
			clearInterval(intervalId); // Stop checking once the link is removed
		}
	}, 100);
});

const particlesConfig = {
	particles: {
		number: {
			value: 8,
			density: {
				enable: true,
				value_area: 481.0236182596568,
			},
		},
		color: {
			value: ["#BD10E0", "#B8E986", "#50E3C2", "#FFD300", "#E86363"],
		},
		shape: {
			type: "circle",
			stroke: {
				width: 0,
				color: "#000000",
			},
		},
		opacity: {
			value: 1,
			random: true,
			anim: {
				enable: false,
				speed: 1,
				opacity_min: 0,
				sync: false,
			},
		},
		size: {
			value: 100,
			random: true,
			anim: {
				enable: false,
				speed: 4,
				size_min: 0.3,
				sync: false,
			},
		},
		line_linked: {
			enable: false,
			distance: 150,
			color: "#ffffff",
			opacity: 0.4,
			width: 1,
		},
		move: {
			enable: true,
			speed: 3,
			direction: "none",
			random: true,
			straight: false,
			out_mode: "out",
			bounce: false,
			attract: {
				enable: false,
				rotateX: 600,
				rotateY: 600,
			},
		},
	},
	interactivity: {
		detect_on: "window",
		events: {
			onhover: {
				enable: true,
				mode: "bubble",
			},
			onclick: {
				enable: true,
				mode: "remove",
			},
			resize: true,
		},
		modes: {
			grab: {
				distance: 400,
				line_linked: {
					opacity: 1,
				},
			},
			bubble: {
				distance: 450,
				size: 0,
				duration: 2,
				opacity: 0.5,
				speed: 3,
			},
			repulse: {
				distance: 400,
				duration: 0.4,
			},
			push: {
				particles_nb: 4,
			},
			remove: {
				particles_nb: 2,
			},
		},
	},
	retina_detect: true,
};

particlesJS("particles", particlesConfig);

// Dark Mode
document.addEventListener("DOMContentLoaded", function () {
	// Function to detect system preference and set initial mode
	function setInitialMode() {
		const prefersDarkMode =
			window.matchMedia &&
			window.matchMedia("(prefers-color-scheme: dark)").matches;
		const userPreference = localStorage.getItem("darkMode");

		// Set initial mode based on user preference or system preference
		const isDarkMode =
			userPreference === "true" ||
			(prefersDarkMode && userPreference !== "false");
		document.body.classList.toggle("dark-mode", isDarkMode);

		const icon = document.querySelector(".color-theme-icon");
		icon.classList.toggle("fa-sun", !isDarkMode);
		icon.classList.toggle("fa-moon", isDarkMode);
	}

	// Function to toggle dark mode and save state to local storage
	// Function to toggle dark mode and save state to local storage
	function toggleDarkMode() {
		const body = document.body;
		const icon = document.querySelector(".color-theme-icon");

		// Toggle the dark mode class on the body
		body.classList.toggle("dark-mode");

		// Update the icon class based on dark mode state
		const isDarkMode = body.classList.contains("dark-mode");
		icon.classList.toggle("fa-sun", !isDarkMode);
		icon.classList.toggle("fa-moon", isDarkMode);

		// Save the toggled state to local storage
		localStorage.setItem("darkMode", isDarkMode);

		// Refresh AOS animations
		AOS.refresh();

		// Destroy and reinitialize particles
		particlesJS("particles", particlesConfig);
	}

	// Event listener for the dark mode toggle button
	const darkModeToggle = document.getElementById("dark-mode-toggle");
	darkModeToggle.addEventListener("click", toggleDarkMode);

	// Set the initial mode when the page loads
	setInitialMode();
});
