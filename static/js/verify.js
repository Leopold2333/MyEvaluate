function doSendMail() {
    // ��ֹ�ظ����ʼ���һ��������Ͱ�ť�Ͳ�����
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
            // �ɹ������������
            if (data['errmsg'] == 'send-pass') {
                var btn_change = $("#btn_change");
                btn_change.css("display", "block");
            } else {  // ����Ҫ�ط��ʼ�
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