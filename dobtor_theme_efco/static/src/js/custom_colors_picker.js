$(function () {

    body_backgroung = function (arg) {
        $('body').css({ 'background-color': arg });
        
        $('.panel-default>.panel-heading').css({ 'background-color': arg, 'border-color': arg });
        $('.theme-home-slider .item1, .theme-home-slider.item2').css({ 'background-color': arg });
    }

    body_font = function (arg) {
        $('body').css({ color: arg });
        
        
        $('.panel-default>.panel-heading').css({ color: arg });
        // $('a').css({ color: arg });
        $('.separator-2').css({'background-color': arg});
        $('.separator').css({ 'background-color': arg, 'border': '1px solid ' + arg});

    }

    Background_Color_fcn = function () {
        $('#CustomBackgroundColor').colorpicker().on('changeColor', function (e) {
            body_backgroung(e.color.toString('rgba') + ' !important');
        });
    }

    Element_Color = function (arg) {
        // nav
        $('.nav-tabs>li.active>a, .nav-tabs>li.active>a:hover, .nav-tabs>li.active>a:focus')
            .css({ color: arg });
        // table
        $('.table>thead>tr>th, .table>thead>tr>td').css({ color: arg });
        $('.table-hover tbody tr:hover').css({ color: arg });
        // btn
        $('.btn-default').css({ color: arg });
        $('.btn-default:hover, .btn-default:focus').css({ color: arg });
        $('.btn-default:active, .btn -default.active').css({ color: arg });

        $('.btn-primary').css({ color: arg });
        $('.btn-primary:hover, .btn-primary:focus').css({ color: arg });
        $('.btn-primary:active, .btn-primary.active').css({ color: arg });
        // font
        // $('font').css({ color: arg });

    }

    Element_Background_Color = function (arg) {
        // nav
        $('.nav-tabs>li.active>a, .nav-tabs>li.active>a:hover, .nav-tabs>li.active>a:focus')
            .css({ 'background-color': arg });
        // table
        $('.table>thead>tr>th, .table>thead>tr>td').css({ 'background-color': arg});
        $('.table-hover tbody tr:hover').css({ 'background-color': arg });
        // btn
        $('.btn-default').css({ 'background-color': arg, 'border-color': arg });
        $('.btn-default:hover, .btn-default:focus').css({ 'background-color': arg, 'border-color': arg });
        $('.btn-default:active, .btn -default.active').css({ 'background-color': arg, 'border-color': arg});

        $('.btn-primary').css({ 'background-color': arg, 'border-color': arg });
        $('.btn-primary:hover, .btn-primary:focus').css({ 'background-color': arg, 'border-color': arg});
        $('.btn-primary:active, .btn-primary.active').css({ 'background-color': arg, 'border-color': arg});
        // font
        // $('font').css({ 'background-color': arg  });
    }

    panel_background_color = function (arg) {
        // snippets s_banner
        $('.s_banner div.carousel-content.col-md-6.mt64').css({ 'background-color': arg });
        // s_big_message
        $('.jumbotron').css({ 'background-color': arg });
        $('.panel-body, .panel-footer, .list-group-item').css({ 'background-color': arg });
        $('.s_comparisons .panel-primary').css({ 'background-color': arg });
        $('.s_comparisons .panel-primary>.panel-heading').css({ 'background-color': arg, 'border-color': arg });

        $('.s_comparisons .list-group-item.active').hover(function(e){
            $(this).css({ 'background-color': arg, 'border-color': arg });
        });
        $('.s_comparisons .panel-info').css({ 'border-color': arg });
        $('.s_comparisons .panel-info>.panel-heading').css({ 'background-color': arg, 'border-color': arg });
    }

    panel_font_color = function (arg) {
        // s_big_message
        $('.jumbotron h1, .jumbotron p').css({ color: arg });
        $('.s_comparisons .panel-primary>.panel-heading').css({ color: arg });

        $('.s_comparisons .list-group-item.active, .s_comparisons .list-group-item.active:hover, .s_comparisons .list-group-item.active:focus').css({ color: arg });
        $('.s_comparisons .panel-info>.panel-heading').css({ color: arg });
        
    }

    Layout_Font_Color = function(arg) {
        // footer
        $('footer').css({ color: arg });
        $('#top_menu>li>a>span, #top_menu>li>a>b').css({ color: arg });

        $('header .breadcrumb li, header .breadcrumb>li::before, header .breadcrumb > li.active::before').css('color', arg + ' !important');
        //$('header .breadcrumb > li').
        $('#top_menu ul.dropdown-menu li a').css({ color: arg })
    }

    Layout_Hover_Color = function(arg) {
        $('footer a').css({ color: arg });
        $('#top_menu>li.active>a').css('border-bottom-color', arg );
        
        $('#top_menu>li>a').hover(function(e) {
            var org = 'white';//$('#top_menu>li:not(.active) > a > span').css('color');
            // var fontColor = $('#LayoutFontColor input').val();
            if (!$(this).parent().hasClass('active')) {
                $(this).css({ 'border-bottom-color': e.type === "mouseenter" ? arg : 'transparent' });
                $(this).find('span').css({ color: e.type === "mouseenter" ? arg : org });
                $(this).find('b').css({ color: e.type === "mouseenter" ? arg : org });
            }
        })
        // .focus(function() {
        //     $(this).css({ 'border-bottom': '3.2px solid ' + arg + ' !important', color: arg });
        //     $(this).find('span').css({ color: arg });
        //     $(this).find('b').css({ color: arg });
        // })
        $('header div.navbar.navbar-default.navbar-static-top #top_menu>li.active a #top_menu>li.active a').css({ color: arg });
        $('#top_menu>li.active a span,#top_menu>li.active a b').css({ color: arg});
        // $('#top_menu ul.dropdown-menu li').hover(function() {
        //     $(this).find('a').css({ color: arg });
        // })

        // breadcrumb
        $('header .breadcrumb a').css('color', arg)
        $('#top_menu ul.dropdown-menu li a').hover(function (e) {
            var org = 'white';//$('#top_menu ul.dropdown-menu li a').css('color');
            $(this).css({ 'color': e.type === "mouseenter" ? arg : org });
        })
    }

    Layout_Background_Color = function(arg) {
        // footer
        $('footer').css({ 'background-color': arg });

        $('header').css({ 'background-color': arg });
        $('header div.navbar.navbar-default.navbar-static-top, header div.navbar.navbar-default.navbar-fixed-top').css({ 'background-color': arg });
        // breadcrumb 
        $('header .breadcrumb').css({ 'background-color': arg });
        $('#top_menu ul.dropdown-menu').css({ 'background-color': arg, 'opacity' : 0.7 });
    }

    Font_Color_Fcn = function () {
        $('#CustomFontColor').colorpicker().on('changeColor', function (e) {
            body_font(e.color.toString('rgba') + ' !important');
        });
    }

    Panel_color_fcn = function () {
        $('#CustomPanelColor').colorpicker().on('changeColor', function (e) {
            panel_background_color(e.color.toString('rgba'));
        })
    }

    Panel_Font_color_fcn = function () {
        $('#CustomPanelFontColor').colorpicker().on('changeColor', function (e) {
            panel_font_color(e.color.toString('rgba'));
        })
    }

    Element_color_fcn = function () {
        $('#CustomElementColor').colorpicker().on('changeColor', function (e) {
            Element_Background_Color(e.color.toString('rgba'))
        })
    }

    Element_Font_color_fcn = function () {
        $('#CustomElementFontColor').colorpicker().on('changeColor', function (e) {
            Element_Color(e.color.toString('rgba'))
        })
    }

    Layout_Font_Color_fcn = function() {
        $('#LayoutFontColor').colorpicker().on('changeColor', function (e) {
            Layout_Font_Color(e.color.toString('rgba'))
        })
    }

    Layout_Hover_Color_fcn = function() {
        $('#LayoutHoverColor').colorpicker().on('changeColor', function (e) {
            Layout_Hover_Color(e.color.toString('rgba') + ' !important')
        })
    }

    Layout_Background_Color_fcn = function () {
        $('#LayoutBackgroundColor').colorpicker().on('changeColor', function (e) {
            Layout_Background_Color(e.color.toString('rgba'))
        })
    }


    Customize_Color = function () {
        return $.ajax({
            type: "POST",
            url: '/dobtor_theme/customize/read/',
            dataType: 'json',
            async: true,
            data: JSON.stringify({}),
            contentType: "application/json; charset=utf-8",
        });
    }


    Upgrade_Color = function (datas) {
        return $.ajax({
            type: "POST",
            url: '/dobtor_theme/customize/write/',
            dataType: 'json',
            async: true,
            data: JSON.stringify(datas),
            contentType: "application/json; charset=utf-8",
        });
    }

    cancelAll = function () {
        body_backgroung('');
        body_font('');
        Element_Color('');
        Element_Background_Color('');
        panel_background_color('');
        panel_font_color('');
        Layout_Font_Color('');
        Layout_Hover_Color('');
        Layout_Background_Color('');
    }

    renderAll = function (jsondata) {
        if (jsondata.Customize) {
            body_backgroung(jsondata.Background_Color + ' !important');
            body_font(jsondata.Font_Color + ' !important');
            Element_Color(jsondata.Element_Font_Color);
            Element_Background_Color(jsondata.Element_Color);
            panel_background_color(jsondata.Panel_Color);
            panel_font_color(jsondata.Panel_Font_Color);
            Layout_Font_Color(jsondata.Layout_Font_Color);
            Layout_Hover_Color(jsondata.Layout_Hover_Color);
            Layout_Background_Color(jsondata.Layout_Background_Color);
        }
    }

    init = function () {
        if ($('#dobtor_theme_Customize').hasClass("checked")) {
            $('table[name="color"] > tbody > tr.colorOption').removeClass('hidden');
            Background_Color_fcn();
            Font_Color_Fcn();
            Panel_color_fcn();
            Panel_Font_color_fcn();
            Element_color_fcn();
            Element_Font_color_fcn();
            Layout_Font_Color_fcn();
            Layout_Hover_Color_fcn();
            Layout_Background_Color_fcn();
            renderAll({
                'Customize': true,
                'Background_Color': $('#CustomBackgroundColor > input:text').val(),
                'Font_Color': $('#CustomFontColor > input:text').val(),
                'Panel_Color': $('#CustomPanelColor > input:text').val(),
                'Panel_Font_Color': $('#CustomPanelFontColor > input:text').val(),
                'Element_Color': $('#CustomElementColor > input:text').val(),
                'Element_Font_Color': $('#CustomElementFontColor > input:text').val(),
                'Layout_Font_Color': $('#LayoutFontColor > input:text').val(),
                'Layout_Hover_Color': $('#LayoutHoverColor > input:text').val(),
                'Layout_Background_Color': $('#LayoutBackgroundColor > input:text').val(),
            })
        } else {
            $('table[name="color"] > tbody > tr.colorOption').addClass('hidden');
            cancelAll();
        }
    }

    Customize_Color()
        .done(function (response) {
            var jsondata = JSON.parse(response.result);
            if (jsondata.status == 'Done')
                renderAll(jsondata);
        })
        .fail(function (xmlHttpRequset, textStatus, errorThorwn) {
            console.log(errorThorwn)
        })

    $(document).on('DOMNodeInserted', '#theme_customize_modal', function () {

        Customize_Color()
            .done(function (response) {
                var jsondata = JSON.parse(response.result);
                //renderAll(jsondata);
                if (jsondata.status === 'Done') {
                    $('#CustomBackgroundColor > input:text').val(jsondata.Background_Color);
                    $('#CustomBackgroundColor > span > i').css('backgroung-color', jsondata.Background_Color);
                    $('#CustomFontColor > input:text').val(jsondata.Font_Color);
                    $('#CustomFontColor > span > i').css('backgroung-color', jsondata.Font_Color);
                    $('#CustomPanelColor > input:text').val(jsondata.Panel_Color);
                    $('#CustomPanelColor > span > i').css('backgroung-color', jsondata.Panel_Color);
                    $('#CustomPanelFontColor > input:text').val(jsondata.Panel_Font_Color);
                    $('#CustomPanelFontColor > span > i').css('backgroung-color', jsondata.Panel_Font_Color);
                    $('#CustomElementColor > input:text').val(jsondata.Element_Color);
                    $('#CustomElementColor > span > i').css('backgroung-color', jsondata.Element_Color);
                    $('#CustomElementFontColor > input:text').val(jsondata.Element_Font_Color);
                    $('#CustomElementFontColor > span > i').css('backgroung-color', jsondata.Element_Font_Color);
                    $('#LayoutBackgroundColor > input:text').val(jsondata.Layout_Background_Color);
                    $('#LayoutBackgroundColor > span > i').css('backgroung-color', jsondata.Layout_Background_Color);
                    $('#LayoutFontColor > input:text').val(jsondata.Layout_Font_Color);
                    $('#LayoutFontColor > span > i').css('backgroung-color', jsondata.Layout_Font_Color);
                    $('#LayoutHoverColor > input:text').val(jsondata.Layout_Hover_Color);
                    $('#LayoutHoverColor > span > i').css('backgroung-color', jsondata.Layout_Hover_Color);
                }
                init();
            })
            .fail(function (xmlHttpRequset, textStatus, errorThorwn) {
                console.log(errorThorwn)
            })

        $('.dobtor_save').on('click', function () {
            var datas = {
                'jsonrpc': '2.0',
                'method': 'call',
                'params': {
                    'Customize': $('#dobtor_theme_Customize').hasClass('checked'),
                    'Background_Color': $('#CustomBackgroundColor > input:text').val(),
                    'Font_Color': $('#CustomFontColor > input:text').val(),
                    'Panel_Color': $('#CustomPanelColor > input:text').val(),
                    'Panel_Font_Color': $('#CustomPanelFontColor > input:text').val(),
                    'Element_Color': $('#CustomElementColor > input:text').val(),
                    'Element_Font_Color': $('#CustomElementFontColor > input:text').val(),
                    'Layout_Font_Color': $('#LayoutFontColor > input:text').val(),
                    'Layout_Hover_Color': $('#LayoutHoverColor > input:text').val(),
                    'Layout_Background_Color': $('#LayoutBackgroundColor > input:text').val(),
                },
                'id': Math.floor(Math.random() * 1000 * 1000 * 1000)
            }
            Upgrade_Color(datas)
                .done(function (data) {
                    var jsondata = JSON.parse(data.result);
                    alert(jsondata.status)
                })
                .fail(function (xmlHttpRequset, textStatus, errorThorwn) {
                    console.log(errorThorwn)
                })
        })

        $('input[name="colorstyle"]:radio').on('change', function () {
            customize_datas = {
                'jsonrpc': '2.0',
                'method': 'call',
                'params': {
                    'Customize': $('#dobtor_theme_Customize').hasClass("checked"),
                },
                'id': Math.floor(Math.random() * 1000 * 1000 * 1000)
            }
            $.ajax({
                type: "POST",
                url: '/dobtor_theme/customize/toggle/',
                dataType: 'json',
                async: true,
                data: JSON.stringify( customize_datas ),
                contentType: "application/json; charset=utf-8",
            }).done(function (data) {
                init();
            });
        })
    });

    $(document).on('DOMNodeRemoved', '#theme_customize_modal', function () {
        $('.dobtor_save').off('click');
        $('input[name="colorstyle"]:radio').off('change');
    });
});

