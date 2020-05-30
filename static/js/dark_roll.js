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
        threshold = roller[x];
        $("#roll-threshold").text(threshold)
    }

    function getDiceRoll(x) {
        return Math.floor(Math.random() * x) + 1;
    }

    function checkPrintWinner(thresh, result) {
        if (result <= thresh) {
            $("#pass-fail").text("PASSED!").css("color", "green");
            pass = 1;
        } else {
            $("#pass-fail").text("FAILED!").css("color", "red");
        }
    }

    getRollerStats()
    PrintRollThresh(roller.rolltype)

    $("#roll-button").click(function() {
        $("#roll-button").attr("disabled", true);
        let result = getDiceRoll(100);
        setTimeout(function() {
            $("#roll-result").text(result);
            checkPrintWinner(threshold, result);
        }, 750);
    });

});