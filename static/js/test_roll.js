window.localStorage;

$(document).ready(function() {

    $('.slider').on('input change', function() {
        $(this).next($('.mod-label')).html(this.value);
    });
    $('.mod-label').each(function() {
        var value = $(this).prev().attr('value');
        $(this).html(value);
    });

    $(".rolltype-button").click(function() {
        var rolltype = $(this).attr('value');
        console.log(rolltype)
        $("#test-roll-type").attr('value', rolltype);
    });

});