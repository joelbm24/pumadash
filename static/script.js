function displayInfo(type) {
    $.ajax({
        url: "/info/"+type,
        cache: false,
        success: function(html){
            $('#info-area').empty();
            $('#info-area').append(html);
            }
        });
}

function accordAnim() {
    $(".container h2").click(function(){
    $(this).next("div").slideToggle("fast")
    .siblings("div:visible").slideUp("fast");
    });
}


$(document).ready(function(){
    accordAnim();
});
