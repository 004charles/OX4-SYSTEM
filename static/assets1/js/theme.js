(function($){
	"use-strict";
	var windowOn = $(window);

	$(document).ready(function () {

	// Image reveal animation

	function revealAnimation(selector, axis, percent, scale) {
		gsap.utils.toArray(selector).forEach(function (revealItem) {
			// Check if the revealItem contains an image
			var image = revealItem.querySelector("img");
			if (!image) {
				console.warn("No image found in", revealItem);
				return;
			}

			var tl = gsap.timeline({
				scrollTrigger: {
					trigger: revealItem,
					toggleActions: "play none none reverse",
				},
			});

			// Set initial state
			tl.set(revealItem, { autoAlpha: 1 })
				.from(revealItem, {
					duration: 1.5, // Specify duration directly
					[axis + "Percent"]: -percent, // Use axis + "Percent" for dynamic property names
					ease: "power2.out", // Use string for ease function
				})
				.from(image, {
					duration: 1.5, // Specify duration directly
					[axis + "Percent"]: percent, // Use axis + "Percent" for dynamic property names
					scale: scale,
					delay: -1.5, // Delay for image animation
					ease: "power2.out", // Use string for ease function
				});
		});
	}

	// Call the function with your selectors
	revealAnimation(".reveal-left", "x", 100, 1.3);
	revealAnimation(".reveal-bottom", "y", 100, 1.3);

});

// Counterup
$('.counter').counterUp({});

// Wow Js
if ($('.wow').length) {
	var wow = new WOW({
		boxClass: 'wow', // animated element css class (default is wow)
		animateClass: 'animated', // animation css class (default is animated)
		offset: 0, // distance to the element when triggering the animation (default is 0)
		mobile: false, // trigger animations on mobile devices (default is true)
		live: true // act on asynchronously loaded content (default is true)
	});
	wow.init();
}

// Header Search
if($('.search-box-outer').length) {
	$('.search-box-outer').on('click', function() {
		$('body').addClass('search-active');
	});
	$('.close-search').on('click', function() {
		$('body').removeClass('search-active');
});}


/* Text Effect Animation */
if ($('.text-anime-style-3').length) {		
	let	animatedTextElements = document.querySelectorAll('.text-anime-style-3');
	
	animatedTextElements.forEach((element) => {
		//Reset if needed
		if (element.animation) {
			element.animation.progress(1).kill();
			element.split.revert();
		}

		element.split = new SplitText(element, {
			type: "lines,words,chars",
			linesClass: "split-line",
		});
		gsap.set(element, { perspective: 400 });

		gsap.set(element.split.chars, {
			opacity: 0,
			x: "5",
		});

		element.animation = gsap.to(element.split.chars, {
			scrollTrigger: { trigger: element,	start: "top 90%" },
			x: "0",
			y: "0",
			rotateX: "0",
			opacity: 1,
			duration: 1,
			ease: Back.easeOut,
			stagger: 0.02,
		});
	});		
}


// Progress-Area
	let progressBars = $(".progress-area");
	let observer = new IntersectionObserver(function (progressBars) {
		progressBars.forEach(function (entry, index) {
			if (entry.isIntersecting) {
				let width = $(entry.target)
					.find(".progress-bar")
					.attr("aria-valuenow");
				let count = 0;
				let time = 1000 / width;
				let progressValue = $(entry.target).find(".progress-value");
				setInterval(() => {
					if (count == width) {
						clearInterval();
					} else {
						count += 1;
						$(progressValue).text(count + "%");
					}
				}, time);
				$(entry.target)
					.find(".progress-bar")
					.css({ width: width + "%", transition: "width 1s linear" });
			} else {
				$(entry.target)
					.find(".progress-bar")
					.css({ width: "0%", transition: "width 1s linear" });
			}
		});
	});
	progressBars.each(function () {
		observer.observe(this);
	});
	$(window).on("unload", function () {
		observer.disconnect();
	});
	//End

// Header Stikcy

$(window).scroll(function () {
    if ($(this).scrollTop() > 250) {
      $("#header-sticky").addClass("si-sticky");
    } else {
      $("#header-sticky").removeClass("si-sticky");
    }
  });

// Offcanvas Bar

jQuery,
jQuery(document).ready(function (o) {
	0 < o(".offset-side-bar").length &&
		o(".offset-side-bar").on("click", function (e) {
			e.preventDefault(), e.stopPropagation(), o(".cart-group").addClass("isActive");
		}),
		0 < o(".close").length &&
			o(".close").on("click", function (e) {
				e.preventDefault(), o(".cart-group").removeClass("isActive");
			}),
		0 < o(".navSidebar-button").length &&
			o(".navSidebar-button").on("click", function (e) {
				e.preventDefault(), e.stopPropagation(), o(".info-group").addClass("isActive");
			}),
		0 < o(".close").length &&
			o(".close").on("click", function (e) {
				e.preventDefault(), o(".info-group").removeClass("isActive");
			}),
		o("body").on("click", function (e) {
			o(".info-group").removeClass("isActive"), o(".cart-group").removeClass("isActive");
		}),
		o(".dt-sidebar-widget").on("click", function (e) {
			e.stopPropagation();
		}),
		0 < o(".xs-modal-popup").length &&
			o(".xs-modal-popup").magnificPopup({
				type: "inline",
				fixedContentPos: !1,
				fixedBgPos: !0,
				overflowX: "auto",
				closeBtnInside: !1,
				callbacks: {
					beforeOpen: function () {
						this.st.mainClass = "my-mfp-slide-bottom xs-promo-popup";
					},
				},
			});
});

// Accordion

$('.my-accordion > li:eq(0) li').addClass('active').next().slideDown();

	$('.my-accordion li').click(function() {
	var dropDown = $(this).closest('li').find('p');

	$(this).closest('.my-accordion').find('p').not(dropDown).slideUp();

	if ($(this).hasClass('active')) {
	$(this).removeClass('active');
	} else {
	$(this).closest('.my-accordion').find('li.active').removeClass('active');
	$(this).addClass('active');
	}

	dropDown.stop(false, true).slideToggle();

	j.preventDefault();
});

//   Veno Box
new VenoBox({
    selector: '.my-video-links',
});
new VenoBox({
    selector: '.my-image-links',
    numeration: true,
    infinigall: true,
    share: true,
    spinner: 'rotating-plane'
});

// PreLoader Js	
$('.preloader__logo img').addClass('logo-blink');

(function(){
    function id(v){ return document.getElementById(v); }
    function loadbar() {
        var ovrl = id("loading"),
            prog = id("st-loading-line"),
            img = document.images,
            c = 0,
            tot = img.length;
        if(tot == 0) return doneLoading();
    
        function imgLoaded(){
        c += 1;
        var perc = ((100/tot*c) << 0) +"%";
        prog.style.width = perc;

        if(c===tot) return doneLoading();
        }
        function doneLoading(){
        
        setTimeout(function(){ 
            $("#loading").fadeOut(500);
        }, 100);
        }
        for(var i=0; i<tot; i++) {
        var tImg     = new Image();
        tImg.onload  = imgLoaded;
        tImg.onerror = imgLoaded;
        tImg.src     = img[i].src;
        }    
    }
    document.addEventListener('DOMContentLoaded', loadbar, false);
    }());


// Mobile Menu
$('.mobile-menu nav').meanmenu({
	meanScreenWidth: "1200",
	meanMenuContainer: ".mobile-menu",
	onePage: false,
}); 

// Smooth Scroll
function smoothSctoll() {
	$('.title-top-content a').on('click', function (event) {
		var target = $(this.getAttribute('href'));
		if (target.length) {
			event.preventDefault();
			$('html, body').stop().animate({
				scrollTop: target.offset().top - 0
			}, 100);
		}
	});
}
smoothSctoll();

// Services 
var swiper = new Swiper(".card-services", {
	slidesPerView: 4,
	spaceBetween: 30,
	loop: true,
	navigation: {
	  prevEl: ".si-button-prev",
	  nextEl: ".si-button-next",
	},
	breakpoints: {
	1920: {
		slidesPerView: 4,
		},
	  1400: {
		slidesPerView: 4,
	  },
	  992: {
		slidesPerView: 3,
	  },
	  768: {
		slidesPerView: 2,
	  },
	  0: {
		slidesPerView: 1,
	  },
	},
  });

// Team
var swiper = new Swiper(".card-team", {
	slidesPerView: 4,
	spaceBetween: 30,
	scrollbar: {
        el: ".si-swiper-scrollbar",
      },
	navigation: {
	  prevEl: ".si-button-prev",
	  nextEl: ".si-button-next",
	},
	breakpoints: {
	1920: {
		slidesPerView: 3,
		},
	  1400: {
		slidesPerView: 3,
	  },	  
	  992: {
		slidesPerView: 2,
	  },
	  768: {
		slidesPerView: 2,
	  },
	  0: {
		slidesPerView: 1,
	  },
	},
});

var swiper = new Swiper(".card-team2", {
	slidesPerView: 4,
	spaceBetween: 30,
	scrollbar: {
        el: ".si-swiper-scrollbar",
      },
	breakpoints: {
	1920: {
		slidesPerView: 3,
		},
	  1400: {
		slidesPerView: 3,
	  },	  
	  992: {
		slidesPerView: 2,
	  },
	  768: {
		slidesPerView: 2,
	  },
	  0: {
		slidesPerView: 1,
	  },
	},
});


// Brand
var brandswiper = new Swiper(".card-brand", {
	slidesPerView: 4,
	spaceBetween: 30,
	loop: true,
	speed:4000,
	autoplay: {
		delay: 0,
		disableOnInteraction: false,
	},
	allowTouchMove: false,
	breakpoints: {
	1920: {
		slidesPerView: 5,
		},
	  1400: {
		slidesPerView: 4,
	  },	  
	  992: {
		slidesPerView: 4,
	  },
	  768: {
		slidesPerView: 3,
	  }, 
	  0: {
		slidesPerView: 1,
	  },
	},
  });

// Testimonial
var swiper = new Swiper(".card-testimonial", {
	slidesPerView: 4,
	spaceBetween: 0,
	loop: true,
	navigation: {
	  prevEl: ".si-button-prev",
	  nextEl: ".si-button-next",
	},
	breakpoints: {
	1920: {
		slidesPerView: 2,
		},
	  1400: {
		slidesPerView: 2,
	  },
	  992: {
		slidesPerView: 2,
	  },
	  768: {
		slidesPerView: 1,
	  },
	  0: {
		slidesPerView: 1,
	  },
	},
  });


// Testimonial Two
var swiper = new Swiper(".card-testimonial-two", {
	slidesPerView: 4,
	spaceBetween: 30,
	loop: true,
	navigation: {
	  prevEl: ".si-button-prev",
	  nextEl: ".si-button-next",
	},
	breakpoints: {
	1920: {
		slidesPerView: 1,
		},
	  1400: {
		slidesPerView: 1,
	  },
	  992: {
		slidesPerView: 1,
	  },
	  768: {
		slidesPerView: 1,
	  },
	  0: {
		slidesPerView: 1,
	  },
	},
  });

// Testimonial Two
var swiper = new Swiper(".card-brand-one", {
	slidesPerView: 4,
	spaceBetween: 30,
	loop: true,
	navigation: {
	  prevEl: ".si-button-prev",
	  nextEl: ".si-button-next",
	},
	breakpoints: {
	1920: {
		slidesPerView: 5,
		},
	  1400: {
		slidesPerView: 5,
	  },
	  992: {
		slidesPerView: 5,
	  },
	  768: {
		slidesPerView: 4,
	  },
	  0: {
		slidesPerView: 2,
	  },
	},
  });
// Testimonial Two
var swiper = new Swiper(".card-testimonial", {
	slidesPerView: 4,
	spaceBetween: 30,
	loop: true,
	navigation: {
	  prevEl: ".si-button-prev",
	  nextEl: ".si-button-next",
	},
	breakpoints: {
	1920: {
		slidesPerView: 2,
		},
	  1400: {
		slidesPerView: 2,
	  },
	  992: {
		slidesPerView: 2,
	  },
	  768: {
		slidesPerView: 2,
	  },
	  0: {
		slidesPerView: 2,
	  },
	},
  });
// Testimonial Two
var swiper = new Swiper(".card-testimonial-one", {
	slidesPerView: 4,
	spaceBetween: 30,
	loop: true,
	navigation: {
	  prevEl: ".si-button-prev",
	  nextEl: ".si-button-next",
	},
	breakpoints: {
	1920: {
		slidesPerView: 1,
		},
	  1400: {
		slidesPerView: 1,
	  },
	  992: {
		slidesPerView: 1,
	  },
	  768: {
		slidesPerView: 1,
	  },
	  0: {
		slidesPerView: 1,
	  },
	},
  });

// Blogs Two
var swiper = new Swiper(".card-blog", {
	slidesPerView: 4,
	spaceBetween: 30,
	loop: true,
	navigation: {
	  prevEl: ".si-button-prev",
	  nextEl: ".si-button-next",
	},
	breakpoints: {
	1920: {
		slidesPerView: 3,
		},
	  1400: {
		slidesPerView: 3,
	  },
	  992: {
		slidesPerView: 3,
	  },
	  768: {
		slidesPerView: 2,
	  },
	  0: {
		slidesPerView: 1,
	  },
	},
  });


    // Page Scroll Percentage
    function scrollTopPercentage() {
        const scrollPercentage = () => {
            const scrollTopPos = document.documentElement.scrollTop;
            const calcHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
            const scrollValue = Math.round((scrollTopPos / calcHeight) * 100);
            const scrollElementWrap = $("#scroll-percentage");

            scrollElementWrap.css("background", `conic-gradient( var(--si-theme-color) ${scrollValue}%, var(--si-theme-rgba) ${scrollValue}%)`);
            
            // ScrollProgress
            if ( scrollTopPos > 100 ) {
                scrollElementWrap.addClass("active");
            } else {
                scrollElementWrap.removeClass("active");
            }

            if( scrollValue < 96 ) {
                $("#scroll-percentage-value").text(`${scrollValue}%`);
            } else {
                $("#scroll-percentage-value").html('<i class="fa-sharp fa-regular fa-arrow-up-long"></i>');
            }
        }
        window.onscroll = scrollPercentage;
        window.onload = scrollPercentage;

        // Back to Top
        function scrollToTop() {
            document.documentElement.scrollTo({
                top: 0,
                behavior: "smooth"
            });
        }
        
        $("#scroll-percentage").on("click", scrollToTop);
    }

    scrollTopPercentage();
    
/* Portfolio Isotope  */
	$('.image_load').imagesLoaded(function() {

		if ($.fn.isotope) {

			var $portfolio = $('.image_load');

			$portfolio.isotope({

				itemSelector: '.grid-item',

				filter: '*',

				resizesContainer: true,

				layoutMode: 'masonry',

				transitionDuration: '0.8s'

			});
			$('.si__gallery__menu li').on('click', function() {

				$('.si__gallery__menu li').removeClass('active');

				$(this).addClass('active');

				var selector = $(this).attr('data-filter');

				$portfolio.isotope({

					filter: selector,

				});
			});
		};
	});
/* Portfolio Isotope  */
	$('.image_load').imagesLoaded(function() {

		if ($.fn.isotope) {

			var $portfolio = $('.image_load');

			$portfolio.isotope({

				itemSelector: '.grid-item',

				filter: '*',

				resizesContainer: true,

				layoutMode: 'masonry',

				transitionDuration: '0.8s'

			});
			$('.si__gallery__three__menu li').on('click', function() {

				$('.si__gallery__three__menu li').removeClass('active');

				$(this).addClass('active');

				var selector = $(this).attr('data-filter');

				$portfolio.isotope({

					filter: selector,

				});
			});
		};
	});


})(jQuery);