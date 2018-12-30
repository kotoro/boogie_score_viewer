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
});