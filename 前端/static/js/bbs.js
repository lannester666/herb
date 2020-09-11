function checkPPhone() {
	if($.trim(document.getElementById("pPhone").value).length !=11){
		$('#telephoneError').html("请输入中国大陆11位手机号码");
	}
	else {
		$('#telephoneError').html("");
		return true;
	}
}

function checkSPhone() {
	if($.trim(document.getElementById("sPhone").value).length !=11){
		$('#telephoneError').html("请输入中国大陆11位手机号码");
	}
	else {
		$('#telephoneError').html("");
		return true;
	}
}

function getPurchase() {
	var xmlhttp;
	if(window.XMLHttpRequest){
		//IE 7+
		xmlhttp=new XMLHttpRequest();
	}
	else {
		xmlhttp=new ActiveXObject();
	}
	// xmlhttp.onreadystatechange=function () {
	// 	if (xmlhttp.readyState==4&&xmlhttp.status==200){
	// 		//document.getElementById("purchase").innerHTML=xmlhttp.responseText;
	// 	}
    // }
    xmlhttp.open('GET','/bbs/getPurchase',true)
	xmlhttp.send()
}

function getAll() {

}

function timestampToTime(timestamp) {
        var date = new Date(timestamp * 1000);//时间戳为10位需*1000，时间戳为13位的话不需乘1000
        var Y = date.getFullYear() + '-';
        var M = (date.getMonth()+1 < 10 ? '0'+(date.getMonth()+1) : date.getMonth()+1) + '-';
        var D = date.getDate() + ' ';
        var h = date.getHours() + ':';
        var m = date.getMinutes() + ':';
        var s = date.getSeconds();
        return Y+M+D+h+m+s;
    }