function doSendMail() {
    // 禁止重复发邮件，一旦点击发送按钮就不可用
    var btn_send = $("#btn_send");
    btn_send.css("display", "none");
    $.post({
        url:"/ecode",
        data:{
            "receiver":$("#regname").val()
        },
        dataType: 'json',
        success: function (data) {
            alert(data['errmsg']);
            // 成功才允许改密码
            if (data['errmsg'] == 'send-pass') {
                var btn_change = $("#btn_change");
                btn_change.css("display", "block");
            } else {  // 否则要重发邮件
                var btn_send = $("#btn_send");
                btn_send.css("display", "block");
            }
        }
    });
}

function doSendVerify() {
    $.post({
        url:"http://127.0.0.1:5000/verify",
        data:{
            "password":$("#regpwd").val()
        },
        dataType: 'json',
        success: function (data) {
            alert(data['errmsg']);
            window.location.replace("http://127.0.0.1:5000");
        }
    });
}