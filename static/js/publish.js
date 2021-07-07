function sendPublish(){
    var aiteIds=$.trim($("#aiteId").val());
    $.post({
        url:"/publish",
        data:{
            "content":UE.getEditor("content").getContentTxt(),
            "html":UE.getEditor("content").getContent(),
            "aite":aiteIds
        },
        dataType: 'json',
        //数据回调
        success:function(data){
            alert(data['errmsg']);

            location.reload();
        }
    });
}
