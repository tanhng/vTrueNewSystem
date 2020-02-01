
//Goto Top
jQuery(".backtotop").addClass("hidden-top");
jQuery(window).scroll(function () {
	if (jQuery(this).scrollTop() === 0) {
		jQuery(".backtotop").addClass("hidden-top")
	} else {
		jQuery(".backtotop").removeClass("hidden-top")
	}
});

jQuery('.backtotop').click(function () {
	jQuery('body,html').animate({
		scrollTop: 0
	}, 1200);
	return false;
});



jQuery(function($) {
  $('.radio').asCheck();
});