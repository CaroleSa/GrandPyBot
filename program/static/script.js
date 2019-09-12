function getQuestionInThread() {
    var $textareaValueElt = $('textarea').val();
    $('#thread').append("<p><span id='userName'> Utilisateur : <br></span>" + $textareaValueElt + "</p>");
 	$('textarea').val('').change();
}

var map;
function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: -34.397, lng: 150.644},
    zoom: 8
    });
}

function getRandomInt(max) {
  return Math.floor(Math.random() * Math.floor(max));
}


function answerError() {
    
    var $place = $('textarea').val();
    console.log($place.length);
    
    
    if ($place.length > 5) {
        var $answersUnknownPlace = "Je ne sais pas où ça se trouve, il semble que ma mémoire me joue des tours !";
 	    $('#thread').append("<p><span id='robotName'> GrandPyBot : <br></span>" + $answersUnknownPlace + "</p>");
    }else {
        const $answersNoPlace = ["Quel endroit cherches-tu ? Je ne comprends pas ...", "Hein ? Quoi ?", "Peux-tu vérifier ton orthographe s'il te plait ?"];
        var $randomNumber = getRandomInt($answersNoPlace.length);
        var $answer = $answersNoPlace[$randomNumber];
  	    $('#thread').append("<p><span id='robotName'> GrandPyBot : <br></span>" + $answer + "</p>");
    }
}


$("button").on('click', function () {
    getQuestionInThread();
    answerError();
    $.ajax({
			data : {question: $('textarea').val()},
			type : 'POST',
			url : '/process'
		})
});

$("textarea").keyup(function(e) {
    if (e.keyCode == 13) {
        getQuestionInThread();
        answerError();
    $.ajax({
			data : {question: $('textarea').val()},
			type : 'POST',
			url : '/process'
		})
    }
});


initMap();

