function getQuestionInThread() {
    var $textareaValueElt = $('textarea').val();
    if ($textareaValueElt.length > 3) {
 	    $('#thread').append("<p><span id='userName'><br> Utilisateur : </span>"+ $textareaValueElt +" </p>");
 	    $('textarea').val('').change();
    }else {
  	    $('textarea').val('').change();
    }
}





$("textarea").keyup(function(e) {
    if (e.keyCode == 13) {
        getQuestionInThread();
        $('textarea').val('').change();
    }
});





var map;
function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: -34.397, lng: 150.644},
    zoom: 8
    });
}

initMap();



