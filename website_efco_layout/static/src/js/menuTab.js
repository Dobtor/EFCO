$(function () {
    $(".li-mega-menu a").css('cursor', 'pointer');
    $(".li-mega-menu>a,.li-mega-menu>ul").on('mouseover', function () {
        if (!$(this).closest('.li-mega-menu').hasClass('clickopen'))
            $(this).closest('.li-mega-menu').addClass('open');
    });
    $(".li-mega-menu>a,.li-mega-menu>ul").on('mouseout', function () {
        if (!$(this).closest('.li-mega-menu').hasClass('clickopen'))
            $(this).closest('.li-mega-menu').removeClass('open');
    });
    $(".li-mega-menu>a").on('click', function () {
        if ($(this).closest('.li-mega-menu').hasClass('open')) {
            $(this).closest('.li-mega-menu').addClass('clickopen');
            $(this).closest('.li-mega-menu').removeClass('open');
        }
    });
    $(".li-mega-menu>a").on('focusout', function () {
        if ($(this).closest('.li-mega-menu').hasClass('clickopen'))
            $(this).closest('.li-mega-menu').removeClass('clickopen');
    });


    $("#top_menu>.dropdown>a,#top_menu>.dropdown>ul").on('mouseover', function () {
        if (!$(this).closest('.dropdown').hasClass('clickopen'))
            $(this).closest('.dropdown').addClass('open');
    });
    $("#top_menu>.dropdown>a,#top_menu>.dropdown>ul").on('mouseout', function () {
        if (!$(this).closest('.dropdown').hasClass('clickopen'))
            $(this).closest('.dropdown').removeClass('open');
    });
    $("#top_menu>.dropdown>a").on('click', function () {
        $(this).closest('.dropdown').addClass('clickopen');
    });
    $("#top_menu>.dropdown>a").on('focusout', function () {
        if ($(this).closest('.dropdown').hasClass('clickopen'))
            $(this).closest('.dropdown').removeClass('clickopen');
    });
});