$(document).ready(function() {
	resizePanel();
	var carousel_change = $(".generic-slider-change");
	carousel_change.owlCarousel({
	loop:true,
	items : 1,
	singleItem:true,
	autoplay: true,
	autoplayTimeout: 5000,
	autoplaySpeed: 1000,
	nav:true,
	navText:['<i class="fa fa-angle-left"></i>','<i class="fa fa-angle-right"></i>'],
});

$('.slider_service').owlCarousel({
	loop:true,
	items : 1,
	autoplay: true,
	autoplayTimeout: 5000,
	autoplaySpeed: 1000,
	nav:true,
	navText:['<i class="fa fa-chevron-left"></i>','<i class="fa fa-chevron-right"></i>'],
});

$('.slider_logo').owlCarousel({
	loop:true,
	items : 5,
	autoplay: true,
	autoplayTimeout: 5000,
	autoplaySpeed: 1000,
	nav:true,
	dots: false,
	navText:['<i class="fa fa-chevron-left"></i>','<i class="fa fa-chevron-right"></i>'],
	responsive: {
		0: {
			items: 3,
		},
		480: {
			items: 3,
		},
		768: {
			items: 5,
		}
	}
});

$('.left_slider_logo').owlCarousel({
	loop:true,
	items : 5,
	autoplay: true,
	autoplayTimeout: 5000,
	autoplaySpeed: 1000,
	nav:true,
	dots: false,
	navText:['<i class="fa fa-chevron-left"></i>','<i class="fa fa-chevron-right"></i>'],
	responsive: {
		0: {
			items: 3,
		},
		480: {
			items: 3,
		},
		768: {
			items: 2,
		}
	}
});

/*
carousel_change.owlCarousel({
singleItem:true,
items : 1,
navigation:true,
navigationText: false,
pagination:true,
rewindNav:true,
rewindSpeed:1,
theme:"owl-ref",
autoPlay: 3000,
afterInit: function(elem){
var posindex = elem.attr('data-jumpto');
elem.trigger('owl.jumpTo', parseInt(posindex));
}
});
$(".next").click(function(){
carousel_change.trigger('owl.next');
})
$(".prev").click(function(){
carousel_change.trigger('owl.prev');
})
//$('.owl-carousel .owl-item .active').css('background', '#eee top center no-repeat fixed');
*/
});
$(window).resize(function() {
resizePanel();
});
/**
*
*/
function resizePanel() {
var w = $(window).width();
var h = $(window).height();
var dynamic_h = w*0.438;
$('.slider_panel').css('height', dynamic_h+'px');
}
