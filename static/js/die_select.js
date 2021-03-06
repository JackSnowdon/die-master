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
        $(".rolltype-button").removeClass("rolltype-selected");
        var rolltype = $(this).attr('value');
        $(this).addClass("rolltype-selected")
        $(".roll-banner").fadeIn('slow');
        $(".select-roll-type").attr('value', rolltype);
    });

    $('#send-all-model').on('hidden.bs.modal', function() {
        $(".rolltype-button").removeClass("rolltype-selected");
        $(".roll-banner").fadeOut('slow');
    })

});