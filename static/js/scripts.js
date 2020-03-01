// Expand or collapse the correct issue or feature detail section
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

// Bootstrap tooltip
$('[data-toggle="tooltip"]').tooltip();

// Check for all required fields on a form. If they are all filled in
// enable the submit button.
$(document).on("keyup paste", ".ua-required", function() {
    var fields = $(".ua-required");
    var disable = false;
    var foo = 0;
    for (var i = 0; i < fields.length; i++) { // For loop faster than $.each
        if ($(fields[i]).val() === "") {
            disable = true;
            console.log(`Number of blank fields: ${++foo}`);
            //break;  // No need to go through all the fields.....it just takes one
        }
    }

    if (disable) {$("#submit-btn").addClass("ua-disabled");}
    else {$("#submit-btn").removeClass("ua-disabled");}
});

// Numeric or alpha only field checking
$(document).on("keypress paste", ".numeric-only", function(key) {
    if (key.charCode < 48 || key.charCode > 57) {return false;}
});
$(document).on("keypress paste", ".alpha-only", function(key) {
    if (key.charCode >= 48 && key.charCode <= 57) {return false;}
});

// For small form factor devices. Filters become a popover dropdown menu
$('[data-toggle="filter-popover-issues"]').popover( {
    html: true,
    content: function() {
        return $('#filter-popover-menu-issues').html();
    }
});
$('[data-toggle="filter-popover-features"]').popover( {
    html: true,
    content: function() {
        return $('#filter-popover-menu-features').html();
    }
});

// Check bid amount minimum and maximum.
$(".check-minmax-vals").click(function() {
    // Not sure how to stop Django from posting back to server.
    // For now this is just returning and checking on the backend.
    return;


    // Now check to see if there are min max values. If so, check those.
    // This code is assuming there is only one of these values. In production
    // this would have to iterate all input fields with this class.
    minVal = $(".minmax-vals").attr("min");
    maxVal = $(".minmax-vals").attr("max");
    if (minVal != "undefined") {
        if (parseInt(minVal) > parseInt($(".minmax-vals").val())) {
            alert(`Minimum acceptable bid is £${$(".minmax-vals").attr("min")}`);
        } else {
            if (maxVal != "undefined") {
                if (parseInt(maxVal) > parseInt($(".minmax-vals").val())) {
                    alert(`Maximum acceptable bid is £${$(".minmax-vals").attr("max")}`);
                } else {
                    // If we are here, the values are ok. Submit the form.
                    $("form").submit();
                }
            } else {
                alert("Requested to check maximum value, but no maximum value supplied.");
                return false;
            }
        }
    } else {
        alert("Requested to check minimum value, but no minimum value supplied.");
        return false;
    }
});

// Character count
$(document).on("keyup paste", ".char-countdown", function() {
    var maxlen = parseInt($(this).attr("maxlength"));
    if (maxlen === "undefined") {return;}
    $(".char-count").text((maxlen - $(this).val().length).toString());
});
