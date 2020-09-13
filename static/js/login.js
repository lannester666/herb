let userid = null;
let username = null;

$(document).ready(function () {
    isLogin();
})

function isLogin(){
    if(userid == null || username == null)
        document.getElementById('login').style.display = "none";
    else
        document.getElementById('not_login').style.display = "block";
}

$(function () {
    $('#confirmLogin').click(function () {
        let data = {};
        let tempData = $('form').serializeArray();
        $.each(tempData, function() {
        data[this.name] = this.value;
        });

    data = JSON.stringify(data);
    data = JSON.parse(data);
    console.log(data)

    // $.ajax({
    //     url:"http://127.0.0.1:1733/index/",
    //     data:{"userp":data},
    //     type: "POST",
    //     success:function (req) {
    //         alert(req);
    //         console.log(req);
    //     },
    //     error:function (e) {
    //         console.log(data.responseText)
    //     }
    // });

    })
})






