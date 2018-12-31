var drinkType;

function selectMission(type) {
    drinkType = type;

    $("#global-mission-board").hide()
    $("#global-goblet-board").show()
}

function hasGoblet(value) {
    $("#global-mission-board").show()
    $("#global-goblet-board").hide()

    // TODO Send drink request
}

$(function() {

    $("#global-goblet-board").hide();
});