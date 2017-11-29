var scroll_fcn = function () {
    var headerHeight = $("header .navbar-static-top").outerHeight();
    var menu = $('#oe_main_menu_navbar').outerHeight();
    var menuHeight = menu || 0;
    if (($(this).scrollTop() > (headerHeight + menuHeight)) && ($(window).width() > 767)) {
        $("header .navbar.navbar-default")
            .removeClass('navbar-static-top')
            .addClass('navbar-fixed-top')
            .css({ 'margin-top': menuHeight + 'px', 'opacity': '.85', 'z-index': 999});
    } else {
        $("header .navbar.navbar-default")
            .removeClass('navbar-fixed-top')
            .addClass('navbar-static-top')
            .css({ 'margin-top': '0px', 'opacity': '1', 'z-index': 999});
    }
}

$(document).on('change', 'input[name="navbarstyle"]:radio', function () {
    datas = {
        'jsonrpc': '2.0',
        'method': 'call',
        'params': {
            'IsFixedTop': $('#dobtor_theme_fixedtop').hasClass("checked"),
        },
        'id': Math.floor(Math.random() * 1000 * 1000 * 1000)
    }
    $.ajax({
        type: "POST",
        url: '/dobtor_theme/fixedtop/toggle/',
        dataType: 'json',
        async: true,
        data: JSON.stringify(datas),
        contentType: "application/json; charset=utf-8",
    }).done(function (data) {
        if (!$('table[name="navbar"] > tbody > tr > td > label').eq(0).hasClass("checked")) {
            $(window).on('scroll', scroll_fcn);
        } else {
            $("header .navbar.navbar-default")
                .removeClass('navbar-fixed-top')
                .addClass('navbar-static-top')
                .css({ 'margin-top': '0px', 'opacity': '1', 'z-index': 999 });
            $(window).off("scroll", scroll_fcn);
        }
    });
})

$(function() {
    $.ajax({
        type: "POST",
        url: '/dobtor_theme/fixedtop/read/',
        dataType: 'json',
        async: true,
        data: JSON.stringify({}),
        contentType: "application/json; charset=utf-8",
    }).done(function(data) {
        var jsondata = JSON.parse(data.result)
        if (jsondata.IsFixedTop) {
            $(window).on('scroll', scroll_fcn);
        } else {
            $("header .navbar.navbar-default")
                .removeClass('navbar-fixed-top')
                .addClass('navbar-static-top')
                .css({ 'margin-top': '0px', 'opacity': '1', 'z-index': 999 });
            $(window).off("scroll", scroll_fcn);
        }
    });
    
})
