function getQuestionInThread() {
    var $textareaValueElt = $('textarea').val();
    if ($textareaValueElt.length > 3) {
 	    $('#thread').append("<p><span id='userName'> Utilisateur : </span>"+ $textareaValueElt +" </p>");
 	    $('textarea').val('').change();
    }else {
  	    $('textarea').val('').change();
    }
}

$("button").on('click', function () {
    getQuestionInThread();
});

$("textarea").keyup(function(e) {
    if (e.keyCode == 13) {
        getQuestionInThread();
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