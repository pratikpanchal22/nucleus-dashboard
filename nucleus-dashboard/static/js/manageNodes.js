$(document).ready(function () {
    if (!jQuery) {
        // jQuery is not loaded
        alert("Error jQuery is not loaded");
        return;
    }

    initializations();
});

function initializations() {
    stageElements = [];
    stageIsHidden = true;
    console.log("manageNodes.js: initializations");

    $("#idNodeList").click(function(e){
        
        if(e.target.id.length){
            console.log(e.target.id);
            
            if(e.target.id.startsWith("button")){
                $("#"+e.target.id).css("color", "orange");
                $.getJSON("manageNode.json?nodeId="+ e.target.id.split("-")[2] +"&action=settings" + Math.floor(Date.now() / 1000), function (result) {
                    console.log(result);
                }).done(function (){
                    console.log("done");
                    $("#"+e.target.id).css("color", "black");
                }).fail(function(xhr){
                    console.log(xhr.responseText);
                    $("#"+e.target.id).css("color", "red");
                });
            }
        }
    });

    //click handlers
    $("#header-left").click(function () {
        //settingsClickHandler();
        window.location.href = 'settings.html';
        console.log("header-left clicked");
    });
}