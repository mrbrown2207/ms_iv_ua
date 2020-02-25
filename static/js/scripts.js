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
