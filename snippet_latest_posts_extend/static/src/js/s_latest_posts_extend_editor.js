odoo.define('snippet_latest_posts_extend.s_latest_posts_editor', function (require) {
    'use strict';

    var core = require('web.core');
    var s_options = require('web_editor.snippets.options');
    var s_animation = require('web_editor.snippets.animation');
    var Model = require('web.Model');

    var _t = core._t;

    // content
    s_options.registry.js_get_content = s_options.Class.extend({
        start: function () {
            var self = this;
            setTimeout(function () {
                var ul = self.$overlay.find(".snippet-option-js_get_content > ul");
                if (self.$target.attr("data-content")) {
                    var limit = self.$target.attr("data-content");
                    ul.find('li[data-content="' + limit + '"]').addClass("active");
                } else {
                    ul.find('li[data-content="1"]').addClass("active");
                }
            }, 10)
        },

        content: function (type, value, $li) {
            var self = this;
            if (type != "click") { return }
            value = parseInt(value);
            
            this.$target.attr("data-content", value)
                .data("content", value)
                .data('snippet-view').redrow(true);
            setTimeout(function () {
                $li.parent().find("li").removeClass("active");
                $li.addClass("active");
            }, 10);

        },
    });

    // cover_img
    s_options.registry.js_get_cover_img = s_options.Class.extend({
        start: function () {
            var self = this;
            setTimeout(function () {
                var ul = self.$overlay.find(".snippet-option-js_get_cover_img > ul");
                if (self.$target.attr("data-cover_img")) {
                    var limit = self.$target.attr("data-cover_img");
                    ul.find('li[data-cover_img="' + limit + '"]').addClass("active");
                } else {
                    ul.find('li[data-cover_img="1"]').addClass("active");
                }
            }, 10)
        },

        cover_img: function (type, value, $li) {
            var self = this;
            if (type != "click") { return }
            value = parseInt(value);

            this.$target.attr("data-cover_img", value)
                .data("cover_img", value)
                .data('snippet-view').redrow(true);
            setTimeout(function () {
                $li.parent().find("li").removeClass("active");
                $li.addClass("active");
            }, 10);

        },
    });

});