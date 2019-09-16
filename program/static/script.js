function getQuestionInThread() {
    var $textareaValueElt = $('textarea').val();
    $('#thread').append("<p><span id='userName'> Utilisateur : <br></span>" + $textareaValueElt + "</p>");



    $.ajax({
			data : {question: $('textarea').val()},
			type : 'POST',
			url : '/process'
	})
	.done(function(data) {
          $('#thread').append("<p><span id='userName'> Carole : <br></span>" + $textareaValueElt + "</p>");
    });
 	$('textarea').val('').change();
}

var map;
function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: -34.397, lng: 150.644},
    zoom: 8
    });
}


$("button").on('click', function () {
    getQuestionInThread();

    $.ajax({
			data : {question: $('textarea').val()},
			type : 'POST',
			url : '/process'
		})
});

$("textarea").keyup(function(e) {
    if (e.keyCode == 13) {
        getQuestionInThread();

    $.ajax({
			data : {question: $('textarea').val()},
			type : 'POST',
			url : '/process'
		})
    }
});

initMap();


