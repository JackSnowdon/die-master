//  Below creates localStorage for Saving/Loading

window.localStorage;

$(document).ready(function() {

    // Roller Object

    let roller = new Object();
    let threshold = 0;
    let pass = 0;

    // Setup Functions

    function getRollerStats() {
        roller.rolltype = $("#rolltype").text();
        roller.weapon_skill = $("#wep-skill").text();
        roller.ballistic_skill = $("#bal-skill").text();
        roller.strengh = $("#strengh").text();
        roller.toughness = $("#toughness").text();
        roller.agility = $("#agility").text();
        roller.intelligence = $("#intelligence").text();
        roller.perception = $("#perception").text();
        roller.willpower = $("#willpower").text();
        roller.fellowship = $("#fellowship").text();
        roller.influence = $("#influence").text();
        roller.max_fate_points = $("#max-fate-points").text();
    };

    function PrintRollThresh(x) {
        let threshold = roller[x];
        console.log(threshold)
        $("#id_threshold").attr("value", threshold);
        $("#roll-threshold").text(threshold)
    }

    function getDiceRoll(x) {
        return Math.floor(Math.random() * x) + 1;
    }

    function checkPrintWinner(thresh, result) {
        if (result <= thresh) {
            $("#pass-fail").text("PASSED!").css("color", "green");
            pass = 1;
            $("#passed-roll").show()
        } else {
            $("#pass-fail").text("FAILED!").css("color", "red");
            $("#failed-roll").show()
            if (roller.max_fate_points > 0) {
                $("#reroll-button").attr("disabled", false);
                $("#reroll-promt").text("Spend a fate point to roll again?")
                $("#reroll-button").show()
            }
        }
    }

    function dieRoll() {
        $("#roll-button").attr("disabled", true);
        let result = getDiceRoll(100);
        setTimeout(function() {
            $("#sumbit-dark-roller").show();
            $("#id_roll_amount").attr("value", result);
            $("#roll-result").text(result);
            checkPrintWinner(threshold, result);
        }, 750);
    }

    getRollerStats()
    PrintRollThresh(roller.rolltype)

    $("#roll-button").click(function() {
        dieRoll();
    });

    $("#reroll-button").click(function() {
        $("#failed-roll").hide();
        $("#reroll-button").attr("disabled", true);
        roller.max_fate_points--;
        $("#max-fate-points").text(roller.max_fate_points)
        $("#pass-fail").empty()
        dieRoll();
    });


    // Working With Django Forms

    //$("#id_threshold").attr("disabled", true);
    //$("#id_fate_points").attr("disabled", true);
    // $("#id_roll_amount").attr("disabled", true);


    // $("#lose-test").attr("href", "{% url 'dark_die_result' this_roll.id " + result + " %}").addClass("btn btn-warning"); TEST

});