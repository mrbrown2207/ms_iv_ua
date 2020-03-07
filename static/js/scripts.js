"use strict";

$(function() {
    // Define our required handler function. It checks for all required fields on a form.
    // If they are all filled in enable the submit button.
    var reqHandler = function() {
        var fields = $(".ua-required");
        var disable = false;
        for (var i = 0; i < fields.length; i++) { // For loop faster than $.each
            if ($(fields[i]).val() === "") {
                disable = true;
                break;  // No need to go through all the fields.....it just takes one
            }
        }

        if (disable) {$("#submit-btn").addClass("ua-disabled");}
        else {$("#submit-btn").removeClass("ua-disabled");}
    };

    // Character count
    var charCountHandler = function() {
        var maxlen = parseInt($(this).attr("maxlength"));
        if (maxlen === "undefined") {return;}
        $(".char-count").text((maxlen - $(this).val().length).toString());
    };

    // Call our handler for required field.
    $(document).on("keyup paste", ".ua-required", reqHandler);

    // Call our handler for char countdown fields.
    $(document).on("keyup paste", ".char-countdown", charCountHandler);

    // Any changes to the profile form enable the submit button.
    $(document).on("keyup paste", "#profile-form", function() {
        $("#submit-btn").removeClass("ua-disabled");
    });

    // Handle multiple events for our description fields.

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
    $(".check-minmax-vals").click(function(evt) {
        evt.preventDefault();

        // Now check to see if there are min max values. If so, check those.
        // This code is assuming there is only one of these values. In production
        // this would have to iterate all input fields with this class.
        var minVal = $(".minmax-vals").attr("min");
        var maxVal = $(".minmax-vals").attr("max");
        if (minVal != "undefined") {
            if (parseInt(minVal) > parseInt($(".minmax-vals").val())) {
                alert(`Minimum acceptable bid is £${$(".minmax-vals").attr("min")}`);
                return false;
            }
        } else {
            alert("Requested to check minimum value, but no minimum value supplied.");
            return false;
        } 
        if (maxVal != "undefined") {
            if (parseInt(maxVal) < parseInt($(".minmax-vals").val())) {
                alert(`Maximum acceptable bid is £${$(".minmax-vals").attr("max")}`);
                return false;
            }
        } else {
            alert("Requested to check maximum value, but no maximum value supplied.");
            return false;
        }

        // If we are here, the values are ok. Submit the form.
        $("form").submit();
    });
});
