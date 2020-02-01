jQuery(document).ready(function ($) {

	//Cycles
	///////////////////////////////////////////////////////////////////
	$(function() {
        $('#cycles').cycle({ fx: 'fade', speed: '500', timeout: '6000', pager: '#pager', pagerAnchorBuilder: pagerLinks, cleartypeNoBg:true });
        $('#cycles2').cycle({ fx: 'scrollHorz', speed: '500', timeout: '5000', next: '#video-slider .next', prev: '#video-slider .prev', cleartypeNoBg:true });
        
        function pagerLinks(ind, el) { return '<a href="#"></a>'; }
	});

	//Colorbox
	///////////////////////////////////////////////////////////////////
	$(function() {	
        $(".cb-image").colorbox({ opacity: 0.6 });
        $(".cb-slide").colorbox({ opacity: .5, slideshow: true, slideshowAuto: false, slideshowStart: "Start", slideshowStop: "Pause", previous: "Prev", next: "Next", close: "Close", current: "{current} of {total}" });
        $(".cb-form").colorbox({ iframe: true, innerWidth: 720, innerHeight: 700, opacity: 0.6 });
        $(".gallery .gallery-item a").colorbox({ opacity: .5, slideshow: true, slideshowAuto: false, slideshowStart: "Start", slideshowStop: "Pause", previous: "Prev", next: "Next", close: "Close", current: "{current} of {total}" }); 	 
    });

    //Placeholder
    ///////////////////////////////////////////////////////////////////
    $(function() {
        $('input, textarea').placeholder();
    });

	//WP Gallery
	///////////////////////////////////////////////////////////////////
	$(function() {              
        $.each($('#gallery .gallery'), function(index, value) {
          $(this).find('.gallery-item a').attr('rel','gallery-' + index);  
          var title = $(this).find('.gallery-item:first a').attr('title');  
          $('#gallerynav').append('<a class="filter">' + title + '</a>');
        }); 
        
        if($('#gallerynav a').length > 1) {                         
            $('.gallery').wrap('<div class="filter-content" />');           
            $('#gallerynav a:first-child').addClass('selected');            
        }

        //Caption
        if (!$.support.transition) { $.fn.transition = $.fn.animate; }

        $('.gallery .gallery-item').hover(
            function () {
                $(this).transition({ opacity: 1 }, 100, 'easeInOutQuad');         
                $(this).find('.gallery-caption').transition({ 'top': ($(this).height() - $(this).find('.gallery-caption').outerHeight()) + 'px' }, 100, 'easeInOutQuad');
            },
            function () {
                $(this).transition({ opacity: .8 }, 100, 'easeInOutQuad');
                $(this).find('.gallery-caption').transition({ 'top': $(this).height() }, 100, 'easeInOutQuad');
            }
        );
	});     

	//Filter
	///////////////////////////////////////////////////////////////////
	$(function () {
        var filtersArr = $('.filter');
        var filtersContentArr = $('.fill');

        if (filtersContentArr != null) { $(filtersContentArr[0]).show(); }
        if (!$.support.transition) { $.fn.transition = $.fn.animate; }

        $(".filter").click(function () {

            $(".fill").hide();
            $(".fill").transition({ opacity: 0 }, 0, 'easeInOutQuad');
            $(".filter").removeClass("selected");

            for (i = 0; i < filtersArr.length; i++) {
                if (this == filtersArr[i]) {
                    $(this).addClass("selected");
                    $(filtersContentArr[i]).show();
                    $(filtersContentArr[i]).transition({ opacity: 1 }, 100, 'easeInOutQuad');
                }
            }
        });
    });

}); 

