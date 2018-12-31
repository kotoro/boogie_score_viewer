function scorePlaceAnim(elem_place){
    $(elem_place +" > img").removeClass("hex-spawn");
    window.setTimeout(function(){
        $(elem_place +" > .place-number").removeClass("place-number-spawn");
        window.setTimeout(function(){
            $(elem_place +" > .line-container > img").removeClass("line-spawn");
            window.setTimeout(function(){
                $(elem_place +" > .line-container > .name-container > .name").removeClass("name-spawn");
            }, 600);
        }, 400)
    }, 400);
}
/*$(window).on("load", function(){
    scorePlaceAnim("#score-7");
    scorePlaceAnim("#score-8");
    scorePlaceAnim("#score-9");
    window.setTimeout(function(){
        scorePlaceAnim("#score-4");
        scorePlaceAnim("#score-5");
        scorePlaceAnim("#score-6");
        window.setTimeout(function(){
            scorePlaceAnim("#score-3");
            window.setTimeout(function(){
                scorePlaceAnim("#score-2");
                window.setTimeout(function(){
                    scorePlaceAnim("#score-1");
                }, 1600);
            }, 1600);
        }, 1600);
    }, 1600);
});*/

$(function(){
    var socket = io();

    socket.on('launch_anim_scoreboard', function(){
        scorePlaceAnim("#score-7");
        scorePlaceAnim("#score-8");
        scorePlaceAnim("#score-9");
        window.setTimeout(function(){
            scorePlaceAnim("#score-4");
            scorePlaceAnim("#score-5");
            scorePlaceAnim("#score-6");
            window.setTimeout(function(){
                scorePlaceAnim("#score-3");
                window.setTimeout(function(){
                    scorePlaceAnim("#score-2");
                    window.setTimeout(function(){
                        scorePlaceAnim("#score-1");
                    }, 1600);
                }, 1600);
            }, 1600);
        }, 1600);
    });

    socket.on('mission-initialized', function(data){
        $('#global-scoreboard').hide()
        $('#user-scoreboard').show()


        // Set firstname
        $('#user-firstname').text(data.prenom)
        $('#user-firstname-enc').text(data.prenom)

        // Set lastname
        $('#user-lastname').text(data.nom)
        $('#user-lastname-enc').text(data.nom)

        $('#user-drinks').text(data.nb_drinks)
        $('#user-cup').text(data.cup_used)
        $('#user-score').text(data.score)
        $('#user-alcool').text(data.nb_alc)
        $('#user-soft').text(data.nb_soft)
    });

    socket.on('mission-completed', function(){
        $('#global-scoreboard').show()
        $('#user-scoreboard').hide()
    });

    $('#user-scoreboard').hide()
});