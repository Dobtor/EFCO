/* © 2017 Nedas Žilinskas <nedas.zilinskas@gmail.com>
 * License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
 */
odoo.define('website_snippet.editor', function(require) {
    "use strict";

    var core = require('web.core');
    var ajax = require('web.ajax');
    var Class = require('web.Class');
    var website = require('website.website');
    var options = require('web_editor.snippets.options');
    var editor = require('web_editor.snippet.editor');
    var snippets = require('website_snippet.snippets');
    var widget = require('web_editor.widget');
    var Ace = require('website.ace');
    var contentMenu = require('website.contentMenu');
    var ace_call = require('website.ace_call');

    var _t = core._t;
    var QWeb = core.qweb;

    ajax.loadXML('/website_snippet/static/src/xml/templates.xml', QWeb);

    editor.Class.include({
        compute_snippet_templates: function(html) {
            var $html = $('<div/>').append(html);

            for (var i in snippets) {
                var snippet = '<section data-oe-name=\'' + snippets[i].name + '\' data-oe-type=\'snippet\' data-oe-thumbnail=\'/website_snippet/static/src/img/thumbnail.png\' class=\'snippet-snippet\'>' + snippets[i].html + '</section>';
                $html.find('#snippet_snippets .o_panel_body').append(snippet);
            }


            return this._super($html.html());
        },
    });

    var XmlDocument = Class.extend({
        init: function(text) {
            this.xml = text;
        },
        isWellFormed: function() {
            var error;
            if (document.implementation.createDocument) {
                // use try catch for ie
                try {
                    var dom = new DOMParser().parseFromString(this.xml, "text/xml");
                    error = dom.getElementsByTagName("parsererror");
                    return error.length === 0 || $(error).text();
                } catch (e) {}
            }
            if (window.ActiveXObject) {
                // IE
                var msDom = new ActiveXObject("Microsoft.XMLDOM");
                msDom.async = false;
                msDom.loadXML(this.xml);
                return !msDom.parseError.errorCode || msDom.parseError.reason + "\nline " + msDom.parseError.line;
            }
            return true;
        },
        format: function() {
            return vkbeautify.xml(this.xml, 4);
        },
    });

    var ErrDialog = widget.Dialog.extend({
        "template": "website_snippet.error"
    });

    function raise_validation(message) {
        var err_dialog = new ErrDialog();
        err_dialog.appendTo("body");
        err_dialog.$el.find('.errmsg').text(message);
    }

    var NewSnippetDialog = widget.Dialog.extend({
        template: "website_snippet.new",
        start: function() {
            var self = this;
            ace_call.load()

            self.htmlEditor = window.ace.edit(self.$el.find("#ws-html-view-editor")[0]);
            self.htmlEditor.setTheme("ace/theme/monokai");
            self.htmlEditor.getSession().setUseWorker(false);
            self.htmlEditor.getSession().setMode("ace/mode/xml");

            self.cssEditor = window.ace.edit(self.$el.find("#ws-css-view-editor")[0]);
            self.cssEditor.setTheme("ace/theme/monokai");

            return self._super();
        },
        save: function() {
            var title = this.$el.find("[name='ws_title']").val();
            var html = this.htmlEditor.getValue();
            var css = this.cssEditor.getValue();

            var valid = true;
            if (title.indexOf("'") > -1) {
                var valid = false;
            }

            if (valid && this.$el.find("[name='ws_title']")[0].checkValidity()) {

                try {
                    var json = JSON.stringify(html);
                    JSON.parse(json);
                    var valid = true;
                } catch (e) {
                    var valid = false;
                }

                if (html.indexOf("'") > -1) {
                    var valid = false;
                }

                var xml = new XmlDocument(html);

                if (valid && xml.isWellFormed()) {
                    ajax.jsonRpc('/web/dataset/call_kw', 'call', {
                        model: 'x_website_snippet',
                        method: 'create',
                        args: [{
                            'x_name': title,
                            'x_html': html,
                            'x_css': css,
                        }],
                        kwargs: {}
                    }).then(function() {
                        location.reload();
                    });
                } else {
                    raise_validation(_t('There is an error in your HTML code. Please validate it according to XML format. Do not use single quotes.'));
                }
            } else {
                raise_validation(_t('Please enter valid title for the building block. Do not use single quotes.'));
            }
        }
    });

    contentMenu.TopBar.include({
        new_snippet: function() {
            var self = this;
            var dialog = new NewSnippetDialog();
            dialog.appendTo("body");
        },
    });

    options.registry.custom_snippet = options.Class.extend({
        on_prompt: function() {
            var self = this;
            var dialog = new NewSnippetDialog();
            dialog.appendTo("body");
        },

        drop_and_build_snippet: function() {
            this.on_prompt();
            this.on_remove();
            this._super();
        },

        edit_html: function(type, value) {
            if (type !== "click") return;

            this.on_prompt();
        },

    });
});