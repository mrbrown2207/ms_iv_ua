$('.toggle-button').click(function() {
    var idOfCollapse = $(this).attr("href");
    if ($(idOfCollapse).is(":hidden")) {
        var altText = $(this).attr('data-alt-text');
        $(this).attr('data-alt-text', $(this).text());
        $(this).text(altText);
        $(this).addClass('open');
    } else if ($(idOfCollapse).is(":visible")) {
        var altText = $(this).attr('data-alt-text');
        $(this).attr('data-alt-text', $(this).text());
        $(this).text(altText);
        $(this).removeClass('open');
    }
});

$('[data-toggle="tooltip"]').tooltip();

$(document).on("keyup paste", ".required", function() {
    var fields = ".required";
    var disable = false;
    for (var i = 0; i < fields.length; i++) { // For loop faster than $.each
        if ($(fields[i]).val() == "") {
            disable = true;
            break;  // No need to go through all the fields.....it just takes one
        }
    }

    if (disable) {$("#submit").addClass("disabled");}
    else {$("#submit").removeClass("disabled");}
});

$(document).on("keypress paste", ".numeric-only", function(key) {
    if (key.charCode < 48 || key.charCode > 57) {return false;}
});

$(document).on("keypress paste", ".alpha-only", function(key) {
    if (key.charCode >= 48 && key.charCode <= 57) {return false;}
});

