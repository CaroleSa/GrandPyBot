
function getQuestionInThread() {
    var $textareaValueElt = $('textarea').val();

    $('#messageThread').append("<p><span id='userName'> Utilisateur : <br></span>" + $textareaValueElt + "</p>");

    $.ajax({
			data : {question: $('textarea').val()},
			type : 'POST',
			url : '/process'
	})
	.done(function(data) {
	    if(data.error){
				$('#messageThread').append("<p><span id='robotName'> GrandPy Bot : <br></span>" + data.error + "</p>");
		}else{
                $('#messageThread').append("<p><span id='robotName'> GrandPy Bot : <br></span>Voici l'adresse de "
                + data.place + " :<br> "
                + data.address + ". <br>D'ailleurs ! Sais-tu que je connais très bien cet endroit ?<br>"
                + data.history + "<br>Désolé ! Je suis un peu bavard ... <br>Regardes ici, si tu veux en savoir plus : <a href ="
                + data.url + " target = '_blank'>ICI</a><br>Voici la carte où ça se trouve !</p>");
                var map;
                function initMap() {
                    map = new google.maps.Map(document.getElementById('map'), {
                    center: {lat: data.latitude, lng: data.longitude},
                    zoom: 8
                    });
                }
                initMap();
                $('#map').css('height','200px');
                $('#map').css('width','430px');
                $('#map').css('border-left','5px white inset');
                $('#map').css('border-right',' 5px white inset');
                $('#map').css('border-top',' 5px white inset');
                $('#map').css('border-bottom',' 5px white inset');
             }
    });
 	$('textarea').val('').change();
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




