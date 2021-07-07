function sendRank(content){
    $.post({
        url:"/rank",
        data:{
            "content":content,
        },
        //数据回调
        success:function(){
            location.reload();
        }
    });
}