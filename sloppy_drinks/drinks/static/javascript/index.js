// Set initial starting point of body content based on navbar height
let padding = $("nav").height() + 16 + "px";
$("body").css("paddingTop", padding);

// Reset starting point of body content based on navbar height after button click
$(".navbar-toggler").click(function () {
  setTimeout(function () {
    let padding = $("nav").height() + 16 + "px";
    $("body").css("paddingTop", padding);
  }, 500);
});

// Reset starting point of body content based on navbar height after window resizing
$(window).resize(function () {
  setTimeout(function () {
    let padding = $("nav").height() + 16 + "px";
    $("body").css("paddingTop", padding);
  }, 500);
});