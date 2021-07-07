
function AiteOne(followedBid,B_name){
    //检查艾特div中是否是重复值，非重复则添加，重复则删除
    //id序列比如 1 2 3 名字序列比如 @klkl @sdsf
    var HadIds= $("#aiteId").val();

    var spl=HadIds.split(' ')
    var id=''+followedBid
    var flag=$.inArray(id,spl)
    if(flag>=0){
        if(flag==0){//开头重复
            spl[0]=''
            $("#aiteId").val(spl.join(' ').substring(1,))
            var dd=$("#aiteMan").text().replace('@'+B_name+' ','');
            $("#aiteMan").text(dd);
        }else{
            $("#aiteId").val(HadIds.replace(' '+id+' ',' '))
            var dd=$("#aiteMan").text().replace('@'+B_name+' ','');
            $("#aiteMan").text(dd);
        }
        }
    else{
        $("#aiteId").val(HadIds+id+' ');
        var dd=$("#aiteMan").text();
        $("#aiteMan").text(dd+'@'+B_name+' ');
    }

}