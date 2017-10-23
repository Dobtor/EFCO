$(function() {
    var efco_sreen_height = $(window).height();
    var efco_main = $('main').outerHeight();
    var efco_footer = $('footer').outerHeight();
    var efco_header = $('header').outerHeight();
    var menuHeight = $('#oe_main_menu_navbar').outerHeight() || 0;
    var sum = efco_main + efco_footer + efco_header + menuHeight
    if (efco_sreen_height - sum > 0) {
        $('main').css('min-height', efco_sreen_height - efco_footer - efco_header - menuHeight)
    }
})