// global namespace
window.L = window.L || {};

L.config = L.config || {};
L.method = L.method || {};
L.string = L.string || {};
L.widget = L.widget || {};

L.string.TIMEOUT = '操作超时！';
L.string.SUCCESS = '操作成功！';
L.string.FAILURE = '操作失败！';
L.string.WAITING = '处理中，请稍侯...';
L.string.LOADING = '加载中，请稍侯...';
L.string.POSTING = '发送中，请稍侯...';
L.string.CONFIRM = '确认执行该操作吗？';

/**
 * Format date time
 * @param string a Format
 * @param int    s Timestamp
 */
L.method.date = function(a, s)
{
    var d = s ? new Date(s) : new Date(), f = d.getTime();
    return ('' + a).replace(/a|A|d|D|F|g|G|h|H|i|I|j|l|L|m|M|n|s|S|t|T|U|w|y|Y|z|Z/g, function(a) {
        switch (a) {
        case 'a' : return d.getHours() > 11 ? 'pm' : 'am';  
        case 'A' : return d.getHours() > 11 ? 'PM' : 'AM';  
        case 'd' : return ('0' + d.getDate()).slice(-2);  
        case 'D' : return ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'][d.getDay()];  
        case 'F' : return ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'][d.getMonth()];  
        case 'g' : return (s = (d.getHours() || 12)) > 12 ? s - 12 : s;  
        case 'G' : return d.getHours();  
        case 'h' : return ('0' + ((s = d.getHours() || 12) > 12 ? s - 12 : s)).slice(-2);  
        case 'H' : return ('0' + d.getHours()).slice(-2);  
        case 'i' : return ('0' + d.getMinutes()).slice(-2);  
        case 'I' : return (function() {d.setDate(1); d.setMonth(0); s = [d.getTimezoneOffset()]; d.setMonth(6); s[1] = d.getTimezoneOffset(); d.setTime(f); return s[0] == s[1] ? 0 : 1;})();  
        case 'j' : return d.getDate();  
        case 'l' : return ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'][d.getDay()];  
        case 'L' : return (s = d.getFullYear()) % 4 == 0 && (s % 100 != 0 || s % 400 == 0) ? 1 : 0;  
        case 'm' : return ('0' + (d.getMonth() + 1)).slice(-2);  
        case 'M' : return ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'][d.getMonth()];  
        case 'n' : return d.getMonth() + 1;  
        case 's' : return ('0' + d.getSeconds()).slice(-2);  
        case 'S' : return ['th', 'st', 'nd', 'rd'][(s = d.getDate()) < 4 ? s : 0];  
        case 't' : return (function() {d.setDate(32); s = 32 - d.getDate(); d.setTime(f); return s;})();  
        case 'T' : return 'UTC';  
        case 'U' : return ('' + f).slice(0, -3);  
        case 'w' : return d.getDay();  
        case 'y' : return ('' + d.getFullYear()).slice(-2);  
        case 'Y' : return d.getFullYear();  
        case 'z' : return (function() {d.setMonth(0); return d.setTime(f - d.setDate(1)) / 86400000;})();  
        default  : return -d.getTimezoneOffset() * 60;  
        };  
    });  
};  

L.method.nl2br = function(t, b)
{
    return t.replace(/\r\n/g, "\n").replace(/[\r\n]/g, typeof(b) == "undefined" ? '<br>' : b);
};

L.method.htext = function(html)
{
    var div = document.createElement('div');
    div.appendChild(document.createTextNode(html));
    return div.innerHTML;
};

L.method.confirm = function(message)
{
    return confirm(typeof(message) == "undefined" ? L.string.CONFIRM : message);
};

L.method.prepare = function(options)
{
    var setting = {
        display: L.widget.display,
        message: L.string.WAITING
    };
    $.extend(setting, options || {});

    setting.display.render({
        hold: true,
        mode: 'wait',
        body: setting.message
    });
};

L.method.request = function(options)
{
    var setting = {
        element: null,

        prepare: L.method.prepare,
        respond: L.method.respond,
        success: L.method.success,
        failure: L.method.failure
    };

    $.extend(setting, options || {});

    if (!setting.element) {
        if (setting._action) {
            $.ajax({
                url       : setting._action,
                type      : setting._method || 'get',
                data      : setting._params || '',
                dataType  : setting._format || 'json',
                beforeSend: function(xhr) {
                    if (setting.prepare(setting) === false) {
                        xhr.abort();
                    }
                },
                success   : function(response) {
                    setting.success(setting, response);
                },
                error     : function(xhr, err) {
                    setting.failure(setting, xhr, err);
                }
            });
        }

        return false;
    }

    setting.element = $(setting.element);

    if (setting.element.is('form')) {
        var form = setting.element;

        form.ajaxSubmit({
            dataType  : 'json',
            beforeSend: function(xhr) {
                if (setting.prepare(setting) === false) {
                    xhr.abort();
                }
            },
            success   : function(response) {
                setting.success(setting, response);

                // Auto reload captcha form
                L.widget.captcha.reload(form.find('.captcha'));
            },
            error     : function(xhr, err) {
                setting.failure(setting, xhr, err);
            }
        });
    } else {
        var link = setting.element;

        $.ajax({
            url       : link.attr('href') || link.data('href'),
            type      : 'get',
            dataType  : 'json',
            beforeSend: function(xhr) {
                if (setting.prepare(setting) === false) {
                    xhr.abort();
                }
            },
            success   : function(response) {
                setting.success(setting, response);
            },
            error     : function(xhr, err) {
                setting.failure(setting, xhr, err);
            }
        });
    }

    return false;
};

L.method.success = function(opts, resp)
{
    var args = {
        respond: L.method.respond,
    };
    $.extend(args, opts || {});

    args.respond(opts, resp);
}

L.method.respond = function(opts, resp)
{
    var args = {
        display: L.widget.display,
        forward: true
    };
    $.extend(args, opts || {});

    var msgs = [];
    if (resp.msg != null && resp.msg != '') {
        msgs.push(resp.sta ? resp.sta + ' ' + resp.msg : resp.msg);
    }

    if (resp.err) {
        if (args.forward && resp.url) {
            msgs.push('放弃操作，请 <a href="' + resp.url + '">点击这里</a>');
        }

        args.display.render({
            mode: 'warn',
            head: L.string.FAILURE,
            body: msgs.length ? msgs.join('<br/>') : L.string.FAILURE
        });
    } else {
        if (args.forward) {
            if (resp.url) {
                msgs.push('继续操作，请 <a href="' + resp.url + '">点击这里</a>');
            } else {
                msgs.push('继续操作，请 <a href="javascript:location.reload()">刷新当前页</a> 或 <a href="javascript:history.go(-1)">返回上一页</a>');
            }
        }

        args.display.render({
            head: L.string.SUCCESS,
            body: msgs.length ? msgs.join('<br/>') : L.string.SUCCESS
        });
    }
};

L.method.failure = function(opts, xhr, err)
{
    var args = {
        respond: L.method.respond,
    };
    $.extend(args, opts || {});

    var resp = {err: 1, sta: 0, msg: '', url: '', dat: {}};

    if (err == "error" || err == "parsererror") {
        var json = $.parseJSON(xhr.responseText);
        if (json) {
            resp = json;
        } else {
            resp['sta'] = xhr.status;
            resp['msg'] = xhr.statusText;
        }
    } else if (err == "timeout") {
        resp['sta'] = 504;
        resp['msg'] = L.string.TIMEOUT;
    }

    args.respond(opts, resp);
};

L.method.operate = function(method, action, params, format)
{
    L.method.request({_method: method, _action: action, _params: params, _format: format});
    return false;
};


/**
 * Widgets
 */
L.widget.display = {};
L.widget.display.locate = function(opts)
{
    var args = {
        uqid: ''
    };
    $.extend(args, opts || {});

    var dial = $('.dial[data-id="dial' + args.uqid + '"]');
    if (!dial.size()) {
        var html = ''
        + '<div data-id="dial' + args.uqid + '" class="modal hide fade dial" tabindex="-1" role="dialog" aria-hidden="true">'
        + '    <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>'
        + '    <div class="modal-header dial-head"></div>'
        + '    <div class="modal-body dial-body"></div>'
        + '    <div class="modal-footer dial-foot"></div>'
        + '</div>'
        + '';

        $('body').append(html);
        dial = $(dial.selector);
    }

    return dial;
}
L.widget.display.render = function(opts)
{
    var args = {
        mode: '',
        head: '',
        body: '',
        foot: '',
        
        hold: false
    };
    $.extend(args, opts || {});

    var dial = L.widget.display.locate(opts);

    if (!dial.data('bind')) {
        dial.data('bind', true);
        dial.on('hide', function() {
            return !$(this).data('hold');
        });
    }

    if (dial.data('mode')) {
        dial.removeClass('dial-mode-' + dial.data('mode'));
        dial.data('mode', '');
    }
    if (args.mode) {
        dial.data('mode', args.mode);
        dial.addClass('dial-mode-' + dial.data('mode'));
    }

    dial.data('hold', args.hold ? true : false);
    args.hold ? dial.find('.close').hide() : dial.find('.close').show();

    dial.find('.dial-head').html(args.head);
    args.head == '' ? dial.find('.dial-head').hide() : dial.find('.dial-head').show();

    dial.find('.dial-body').html(args.body);
    args.body == '' ? dial.find('.dial-body').hide() : dial.find('.dial-body').show();

    dial.find('.dial-foot').html(args.foot);
    args.foot == '' ? dial.find('.dial-foot').hide() : dial.find('.dial-foot').show();

    if (dial.is(':hidden')) {
        dial.modal('show');
    }
};
L.widget.display.remove = function(opts)
{
    var args = {
        stay: 0
    };
    $.extend(args, opts || {});

    var dial = L.widget.display.locate(opts);

    if (dial.size() && !dial.is(':hidden')) {
        if (args.stay > 0) {
            setTimeout(function() {dial.modal('hide')}, args.stay);
        } else {
            dial.modal('hide');
        }
    }
};

L.widget.captcha = {};
L.widget.captcha.create = function(form)
{
    form = $(form);
    if (form.hasClass('captcha') && !form.find('.captcha-form').size()) {
        var html = '' +
        '<div class="captcha-form">' +
        '    <div class="captcha-btns">' +
        '        <a href="javascript:;" class="captcha-btns-reload" title="获取新的验证" onclick="L.widget.captcha.reload(this);"></a>' +
        '        <a href="javascript:;" class="captcha-btns-whatis" title="输入验证码有助于我们识别当前是否机器操作"></a>' +
        '    </div>' +
        '    <div class="captcha-show">' +
        '        <a href="javascript:;" onclick="L.widget.captcha.reload(this);" title="获取新的验证"><img onload="L.widget.captcha.onload(this);" src="/check.jpeg?form=' + (form.data('form') || '') + '&time=' + (new Date).getTime() + '"></a>' +
        '    </div>' +
        '    <div class="captcha-main">' +
        '        <input type="text" class="captcha-code" name="_code" autocomplete="off" placeholder="输入验证码">' +
        '        <input type="hidden" name="_form" value="' + (form.data('form') || '') + '">' +
        '    </div>' +
        '</div>' +
        '';
        
        form.html(html);
    }
};
L.widget.captcha.onload = function(form)
{
    form = $(form).closest('.captcha');
    if (form.size()) {
        form.find('.captcha-code').focus().select();
        form.find('.captcha-form').removeClass('captcha-proc-reload');
    }
};
L.widget.captcha.reload = function(form)
{
    form = $(form).closest('.captcha');
    if (form.size()) {
        form.find('.captcha-form').addClass('captcha-proc-reload');
        form.find('.captcha-show img').attr('src', '/check.jpeg?form=' + (form.data('form') || '') + '&time=' + (new Date).getTime());
    }
};

$(function() {
    if ($('body').data('exts-scrollup')) {
        $.scrollUp({
            scrollName: 'scrollUp', // Element ID
            topDistance: '300', // Distance from top before showing element (px)
            topSpeed: 300, // Speed back to top (ms)
            animation: 'fade', // Fade, slide, none
            animationInSpeed: 200, // Animation in speed (ms)
            animationOutSpeed: 200, // Animation out speed (ms)
            scrollText: '', // Text for element
            activeOverlay: false  // Set CSS color to display scrollUp active point, e.g '#00FFFF'
        });
    }

    $('.require-confirm').on('click', function() {
        return L.method.confirm();
    });

    $('.request-ajax-link, .request-ajax-link-with-confirm').on('click', function() {
        if (!$(this).hasClass('request-ajax-link-with-confirm') || L.method.confirm()) {
            L.method.request({element: this});
        }

        return false;
    });

    $('.request-ajax-form, .request-ajax-form-with-confirm').on('submit', function() {
        if (!$(this).hasClass('request-ajax-form-with-confirm') || L.method.confirm()) {
            if (window.CKEDITOR) {
                for (instance in CKEDITOR.instances) {
                    CKEDITOR.instances[instance].updateElement();
                }
            }

            L.method.request({element: this});
        }

        return false;
    });
});
