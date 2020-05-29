//  Below creates localStorage for Saving/Loading

window.localStorage;

$(document).ready(function() {

    // Roller Object

    let roller = new Object();

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
        console.log(roller)
    };

    function getRollThresh(x) {
        console.log(x)
        console.log(roller[x])
        $("#roll-threshold").text(roller[x])
    }

    getRollerStats()

    getRollThresh(roller.rolltype)

});