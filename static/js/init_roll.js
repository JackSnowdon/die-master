window.localStorage;

$(document).ready(function() {

    let mod = $(".mod").text()

    function getDiceRoll(x) {
        return Math.floor(Math.random() * x) + 1;
    }

    function initRoll() {
        $(".init-roll-button").attr("disabled", true);
        let result = getDiceRoll(10);
        setTimeout(function() {
            printInitTotals(result)
        }, 750);
    }

    function printInitTotals(x) {
        $(".init-amount").text(x);
        let total = x + parseInt(mod);
        $("#total-init").text(total);
        $(".final-init-sumbit").attr('value', total);
        $(".roll-banner").show();
    }

    /* Roll Buttons */

    $(".init-roll-button").click(function() {
        initRoll();
    });

});