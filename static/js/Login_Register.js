function sendRegister(){
    elem = document.getElementById('username_regist');
    var content = elem.value;                   //获取该标签内容
    var pattern = elem.pattern;                 //获取该标签已经设置好的正则匹配规则
    var regex = new RegExp('^' + pattern + '$'); //将pattern加上头尾标识
    var match = regex.exec(content);              //进行正则匹配
    var flag=1;
    if(null!=match){
        elem = document.getElementById('email_regist');     //获取需要检查的标签元素
        content = elem.value;                   //获取该标签内容
        pattern = elem.pattern;                 //获取该标签已经设置好的正则匹配规则
        regex = new RegExp('^' + pattern + '$'); //将pattern加上头尾标识
        match = regex.exec(content);              //进行正则匹配
        if(null!=match){
            elem = document.getElementById('phone_regist');     //获取需要检查的标签元素
            content = elem.value;                   //获取该标签内容
            pattern = elem.pattern;                 //获取该标签已经设置好的正则匹配规则
            regex = new RegExp('^' + pattern + '$'); //将pattern加上头尾标识
            match = regex.exec(content);              //进行正则匹配
            if(null!=match){
                elem = document.getElementById('password_regist');     //获取需要检查的标签元素
                content = elem.value;                   //获取该标签内容
                pattern = elem.pattern;                 //获取该标签已经设置好的正则匹配规则
                regex = new RegExp('^' + pattern + '$'); //将pattern加上头尾标识
                match = regex.exec(content);              //进行正则匹配
                if(null!=match){
                    elem = document.getElementById('password_confirm');     //获取需要检查的标签元素
                    if(content !== elem.value)
                        flag=0
                }
                else
                    flag=0;
            }
            else
                flag=0;
        }
        else
            flag=0;
    }
    else
        flag=0;
    if(flag===1){
        $.post({
            url:"/register",
            data:{
                "username":$("#username_regist").val(),
                "email":$("#email_regist").val(),
                "phone":$("#phone_regist").val(),
                "password":$("#password_regist").val(),
                "intro":$("#content_regist").val()
            },
            dataType: 'json',
            //数据回调
            success:function(data){
                $("#username_regist").val("");
                $("#email_regist").val("");
                $("#phone_regist").val("");
                $("#password_regist").val("");
                $("#password_confirm").val("");
                $("#content_regist").val("");
                $("#pname").empty();
                $("#ppassword").empty();
                $("#pemail").empty();
                $("#pphone").empty();
                $("#pconfirm").empty();
                alert(data['errmsg']);
            }
        });
    }
    else
        alert("不符合规范！");
}
function sendLogin(){
    var username = $("#username_login").val();
    var password = $("#password_login").val();
    $.post({
        url:"/login",
        data:{
            "username":username,
            "password":password
        },
        dataType: 'json',
        //数据回调
        success:function(data){
            alert(data['errmsg']);
            if(data['errmsg'] === '登陆成功'){
                $("#username_login").val("");
                $("#password_login").val("");
                location.reload();
            }
        }
    });
}

function sendExit(){
    $.post({
        url:"/exit",
        data:{},
        dataType: 'json',
        //数据回调
        success:function(data){
            alert(data['errmsg']);
            if(data['errmsg'] === '退出成功'){
                location.reload();
            }
        }
    });
}

function check(id)
{
    var elem = document.getElementById(id);     //获取需要检查的标签元素
    var content = elem.value;                   //获取该标签内容
    var temp = null;
    var pattern = elem.pattern;                 //获取该标签已经设置好的正则匹配规则
    var regex = new RegExp('^' + pattern + '$'); //将pattern加上头尾标识
    var match = regex.exec(content);              //进行正则匹配

    if (id === 'username_regist')
        temp = document.getElementById('pname');
    else if (id === 'email_regist')
        temp = document.getElementById('pemail');
    else if (id === 'phone_regist')
        temp = document.getElementById('pphone');
    else if (id === 'password_regist')
        temp = document.getElementById('ppassword');
    else if (id === 'password_confirm')
        temp = document.getElementById('pconfirm');
    //内容变为空
    if (id==="password_confirm" && document.getElementById("password_regist").value!==content ||
        "" === content && temp!=null)
    {
        temp.innerHTML = "!";
        temp.style.color = "#FFA500";
    }
    //匹配成功
    else if (null != match && temp!=null)
    {
        temp.innerHTML = "√";
        temp.style.color = "#00FF00";
    }
    //匹配失败
    else if (null == match && temp!=null)
    {
        temp.innerHTML = "x";
        temp.style.color = "#FF0000";
    }
}