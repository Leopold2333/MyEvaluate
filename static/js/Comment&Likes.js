function clickLike(blogid){
    $.post({
        url:"/likeinfo",
        data:{
            "blogid":blogid,
        },
        dataType: 'json',
        success: function (data) {
            var dd=data['errmsg'].split(',');
            var total=dd.length;
            if(data['errmsg'] === ""){
                total=0;
            }

            $("#likebutton"+blogid).text('查看点赞('+total+')');
            $("#Likeinfo"+blogid).text("点赞小伙伴: "+data['errmsg']);
        }
    });

}

function clickComment(blogid){

    $.post({
        url:"/Commentinfo",
        data:{
            "blogid":blogid,
        },
        dataType: 'json',
        success: function (data) {
            var total=data['msg'].length;
            $("#commentbutton"+blogid).text("查看评论("+total+")");
            $("#comment"+blogid).empty();
            var Html="";
            for(var i=0;i<data['msg'].length;i++){
                Html+="<div class='row' style='font-size: smaller'>"+
                "<div class='col-5'>"+data['msg'][i]['username']+'</div>'+
                '<div class="col-7">评论时间: '+data['msg'][i]['time']+'</div>'+
                '</div><div class="row"><div class="col-1"></div>'+
                '<div class="col-11"><div style="border-left: solid 1px white;border-bottom: solid 1px white;margin-bottom: 5px;padding: 5px">'+
                data['msg'][i]['content']+'</div></div></div>';

            }
            Html+="<div style='margin-top: 5px'>期待你的评论哦！</div>";

            $("#comment"+blogid).html(Html);
        }
    });

}

function addComment(blogid) {
    var content = $.trim($("#usercomment"+blogid).val());
    $("#usercomment"+blogid).val("");
    if(content.length<5){
        alert("评论内容过短");
    }
    else{
        $.post({
            url:"/comment",
            data:{
                "blogid":blogid,
                "content":content,
            },
            dataType: 'json',
            success: function (data) {
                alert(data['errmsg']);
                if(data['errmsg'].indexOf("成功")!=-1){
                clickComment(blogid);
            }
                //location.reload();
            }
        });
    }
}

function addLikes(blogid) {

    if($.trim($("#liks"+blogid).text())=="点赞"){

        //$("#liks"+blogid).text("取消");

        url = "likes/yes"
    }
    else{
        //$("#liks"+blogid).text("点赞");
        url = "likes/no"
    }

    $.post({
        url:url,
        data:{
            "blogid":blogid,
        },
        dataType: 'json',
        success: function (data) {
            alert(data['errmsg']);
            if(data['errmsg'].indexOf("成功")!=-1){

            if($.trim($("#liks"+blogid).text())=="点赞"){
               $("#liks"+blogid).text("取消");
               clickLike(blogid);
            }
            else{
                $("#liks"+blogid).text("点赞");
                clickLike(blogid);
            }

            }
            //location.reload();
        }
    });
}


function addFollow(user_id,username) {

    var url="";
    $("span[id^='"+"followB"+user_id+"-']").each(function(){
        if($.trim($(this).text())=="关注伪主"){

        //$(this).text("取消关注");
        url = "follow/yes";
    }
    else{
        //$(this).text("关注伪主");
        url = "follow/no";
    }
    }
    );

    $.post({
        url:url,
        data:{
            "B_name": username,
            "followedB":user_id
        },
        dataType: 'json',
        success: function (data) {
            alert(data['errmsg']);
            if(data['errmsg'] === "关注成功！"){
                $("span[id^='"+"followB"+user_id+"-']").each(function(){
                    if($.trim($(this).text()) === "关注伪主"){
                        $(this).text("取消关注");
                    }
                    else{
                        $(this).text("关注伪主");
                    }
                }
            );
            //刷新艾特模态框表
            $("#AiteList").empty()
            var Html=""
            for(var i=0;i<data['AiteRe'].length;i++){
                Html+='<button onclick="AiteOne('+data['AiteRe'][i]['followedB']+',\''+data['AiteRe'][i]['B_name']+'\')" type="button" class="list-group-item list-group-item-action"'+
                ' data-dismiss="modal">'+
                data['AiteRe'][i]['B_name']+'</button>'
            }

            $("#AiteList").html(Html)

            }

            //location.reload();
        }
    });
}



//删除微博
function deleteweb(blogid){
    $.post({
        url:"/delete",
        data:{
            "blogid":blogid,
        },
        dataType: 'json',
        success: function (data) {
            alert(data['errmsg']);
            location.reload();
        }
    });

}

