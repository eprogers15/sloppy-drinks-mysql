let padding = $("nav").height() + 12 + "px";
$("body").css("paddingTop", padding)

$(".navbar-toggler").click(function() {
    setTimeout(function() {
        let padding = $("nav").height() + 12 + "px";
        $("body").css("paddingTop", padding)
    }, 500)
})