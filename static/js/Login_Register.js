function sendStudentRegister(){
    elem = document.getElementById('studentName');
    var content = elem.value;                   //获取该标签内容
    var pattern = elem.pattern;                 //获取该标签已经设置好的正则匹配规则
    var regex = new RegExp('^' + pattern + '$'); //将pattern加上头尾标识
    var match = regex.exec(content);              //进行正则匹配
    var flag=1;
    if(null!=match){
        elem = document.getElementById('studentCode');     //获取需要检查的标签元素
        content = elem.value;                   //获取该标签内容
        pattern = elem.pattern;                 //获取该标签已经设置好的正则匹配规则
        regex = new RegExp('^' + pattern + '$'); //将pattern加上头尾标识
        match = regex.exec(content);              //进行正则匹配
        if(null!=match){
            elem = document.getElementById('studentPhone');     //获取需要检查的标签元素
            content = elem.value;                   //获取该标签内容
            pattern = elem.pattern;                 //获取该标签已经设置好的正则匹配规则
            regex = new RegExp('^' + pattern + '$'); //将pattern加上头尾标识
            match = regex.exec(content);              //进行正则匹配
            if(null!=match){
                elem = document.getElementById('studentPassword');     //获取需要检查的标签元素
                content = elem.value;                   //获取该标签内容
                pattern = elem.pattern;                 //获取该标签已经设置好的正则匹配规则
                regex = new RegExp('^' + pattern + '$'); //将pattern加上头尾标识
                match = regex.exec(content);              //进行正则匹配
                if(null==match){
                    flag=0
                }
            }
            else
                flag=0;
        }
        else
            flag=0;
    }
    else
        flag=0;
    // 所有规则都匹配
    if(flag===1){
        $.post({
            url:"/register",
            data:{
                "type":"student",
                "username":$("#studentName").val(),
                "code":$("#studentCode").val(),
                "sex":$("input[name='sex']:checked").val(),
                "grade":$("input[name='grade']:checked").val(),
                "department":$("#studentDepartment").val(),
                "major":$("#studentMajor").val(),
                "adDate":$("#studentAdDate").val(),
                "phone":$("#studentPhone").val(),
                "password":$("#studentPassword").val()
            },
            dataType: 'json',
            //数据回调
            success:function(data){
                $("#studentName").val("");
                $("#studentCode").val("");
                $("#studentDepartment").val("");
                $("#studentMajor").val("");
                $("#studentAdDate").val("");
                $("#studentPhone").val("");
                $("#studentPassword").val("");
                $("#pStudentName").empty();
                $("#pStudentCode").empty();
                $("#pStudentDepartment").empty();
                $("#pStudentMajor").val("");
                $("#pStudentPhone").empty();
                $("#pStudentPassword").empty();
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
    if (id === 'studentName')
        temp = document.getElementById('pStudentName');
    else if (id === 'studentCode')
        temp = document.getElementById('pStudentCode');
    else if (id === 'studentPhone')
        temp = document.getElementById('pStudentPhone');
    else if (id === 'studentPassword')
        temp = document.getElementById('pStudentPassword');
    //匹配成功
    if (null!=match && temp!=null)
    {
        temp.innerHTML = "√";
        temp.style.color = "#00FF00";
    }
    //匹配失败
    else if (null==match && temp!=null)
    {
        temp.innerHTML = "x";
        temp.style.color = "#FF0000";
    }
}