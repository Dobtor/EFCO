$(function() {
    $(".li-mega-menu .nav-tabs a").css('cursor','pointer');
    $(".li-mega-menu .nav-tabs a").on('mouseover',function(){
        $(this).tab('show');
    });

    $(".li-mega-menu .nav-tabs a").on('click',function(){
        window.location.href = $(this).attr('data-fake-href');
    });

    //$(".li-mega-menu").on('mouseover', function () {
    //    $(this).addClass('open');
    //    $(this).attr('aria-expanded', 'true');
    //});


});