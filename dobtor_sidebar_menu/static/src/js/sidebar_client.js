$(function () {
    Get_sidebarData = function () {
        return $.ajax({
            type: "POST",
            url: '/dobtor_sidebar_menu/dobtor_sidebar_menu/',
            dataType: 'json',
            async: true,
            data: JSON.stringify({}),
            contentType: "application/json; charset=utf-8",
        });
    }
    jsondata = [];
    Get_sidebarData()
        .done(function (response) {
            var sb_bottom = '40';
            var sb_right = '30';
            var pathname = location.pathname;

            jsondata = JSON.parse(response.result);
            $('.dobtor_sidebar').each(function (index, item) {
                var self = $('.dobtor_sidebar').eq(index);
                var self_id = self.attr('data-id');
                var queryResult = Enumerable.From(jsondata)
                    .Where(function (x) { return x.id == self_id }).First();

                self.css({
                    position: 'fixed',
                    bottom: sb_bottom + 'px',
                    right: sb_right + 'px',
                    width: queryResult.background_width + 'px',
                    height: queryResult.background_height + 'px',
                    'background-color': queryResult.background,
                    'z-index': '999',
                    'border-radius': queryResult.shape === 'circle' ? '50%' : '0',
                    'margin-top': queryResult.shape === 'circle' ? '2px' : '0',
                    display: pathname === '/web/login' ? 'none': 'block',
                });
                self.hover(function (e) {
                    $(this).css('background-color', e.type === "mouseenter" ? queryResult.background_hover : queryResult.background)
                })
                if (queryResult.iconType === 'img') {
                    self.find('div').css({
                        position: 'relative',
                        top: '50%',
                        transform: 'translateY(-50%)',
                    });
                    self.find('img').css({
                        margin: '0 auto',
                        'border-radius': queryResult.shape === 'circle' ? '50%' : '0',
                    });
                } else if (queryResult.iconType === 'iconic') {
                    self.find('div').css({
                        'font-size': queryResult.size,
                        'text-align': 'center',
                        width: '100%',
                        position: 'relative',
                        top: '50%',
                        transform: 'translateY(-50%)',
                        color: queryResult.font_color,
                    })
                }
                if (queryResult.display_name) {
                    self.find('div').append($('<font></font>').html(queryResult.name).css('padding', '0 8px 0 0'));
                    self.css('width', 'max-content');
                    self.find('img').css('display', 'inline');
                }
                if (queryResult.linkType === 'url') {
                    self.on('click', function () {
                        location.href = queryResult.url
                    })
                } else if (queryResult.linkType === 'content') {
                    $('.sidebar_content[data-id="' + self_id + '"]').html(queryResult.description);
                    $('.sidebar_content[data-id="' + self_id + '"]').css({
                        display: 'none',
                        width: queryResult.content_size + 'px',
                        padding: '10px',
                        height: 'max-content',
                        position: 'fixed',
                        bottom: parseInt(sb_bottom) + 'px',
                        right: parseInt(sb_right) + parseInt(queryResult.background_width) + 10 + 'px',
                        'z-index': 999,
                        'word-wrap': 'break-word',
                    });
                    $('.sidebar_tri[data-id="' + self_id + '"]').css({
                        display: 'none',
                        position: 'fixed',
                        bottom: parseInt(sb_bottom) + 5 + 'px',
                        right: parseInt(sb_right) + parseInt(queryResult.background_width) + 'px',
                        'z-index': 999,
                        'margin-top': parseInt(queryResult.background_height) - 10 + 'px',
                    });
                    $('.sidebar_padding[data-id="' + self_id + '"]').css({
                        display: 'none',
                        position: 'fixed',
                        bottom: parseInt(sb_bottom) + 10 + 'px',
                        right: parseInt(sb_right) + parseInt(queryResult.background_width) + 'px',
                        'z-index': 999,
                        width: '10px',
                        height: parseInt(queryResult.background_height) - 10 + 'px',
                        'background-color': 'transparent',
                    })
                    The_hover = function (e) {
                        $('.sidebar_content[data-id="' + self_id + '"]').css('display', e.type === "mouseenter" ? 'block' : 'none');
                        $('.sidebar_tri[data-id="' + self_id + '"]').css('display', e.type === "mouseenter" ? 'block' : 'none');
                        $('.sidebar_padding[data-id="' + self_id + '"]').css('display', e.type === "mouseenter" ? 'block' : 'none');
                    }
                    self.hover(The_hover);
                    $('.sidebar_content[data-id="' + self_id + '"], .sidebar_tri[data-id="' + self_id + '"], .sidebar_padding[data-id="' + self_id + '"]').hover(The_hover);
                }
                sb_bottom = parseInt(sb_bottom) + parseInt(queryResult.background_height);
            })

        })
        .fail(function (xmlHttpRequset, textStatus, errorThorwn) {
            console.log(errorThorwn)
        })

})