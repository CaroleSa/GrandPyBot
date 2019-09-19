$('#loader').hide();
$('#space2').show();
$("#rowMap").hide();

function getQuestionInThread() {
    var $textareaValueElt = $('textarea').val();

    $('#messageThread').append("<br><p><span id='userName'> Utilisateur : <br></span>" + $textareaValueElt + "</p>");
    $("#textMap").remove();
    $.ajax({
			data : {question: $('textarea').val()},
			type : 'POST',
			url : '/process'
	})
	.done(function(data) {
	    $('#loader').hide();
	    $('#space2').show();

	    if(data.error){

				$('#messageThread').append("<br><p><span id='robotName'> GrandPy Bot : <br></span>" + data.error + "</p>");
				element = document.getElementById('thread');
	            element.scrollTop = element.scrollHeight;
				return
		}if(data.latitude){

                $('#messageThread').append("<br><p><span id='robotName'> GrandPy Bot : <br></span>" + data.address + "<br>"
                + data.history + "</p>");
                element = document.getElementById('thread');
	            element.scrollTop = element.scrollHeight;
	            $('#messageThread').append("<p id='textMap'>" + data.map + "</p>");
                $("#rowMap").show();

                var map;
                function initMap() {
                    map = new google.maps.Map(document.getElementById('map'), {
                    center: {lat: data.latitude, lng: data.longitude},
                    zoom: 18
                    });
                }
                initMap();
                $('#map').css('max-height','100%');
                $('#map').css('max-width','100%');
                $('#map').css('object-fit','cover');
                $('#map').css('border-left','5px white inset');
                $('#map').css('border-right',' 5px white inset');
                $('#map').css('border-top',' 5px white inset');
                $('#map').css('border-bottom',' 5px white inset');

                }else{

                    $('#messageThread').append("<br><p><span id='robotName'> GrandPy Bot : <br></span>" + data.address + "<br>"
                    + data.history + "<br>" + data.map + "</p>");
                    element = document.getElementById('thread');
	                element.scrollTop = element.scrollHeight;
                    }


    });

 	$('textarea').val('').change();
}



$("button").on('click', function () {
    $('#loader').show();
    $('#space2').hide();
    $("#rowMap").hide();

    getQuestionInThread();
});

$("textarea").keyup(function(e) {
    if (e.keyCode == 13) {
        $('#loader').show();
        $('#space2').hide();
        $("#rowMap").hide();
        getQuestionInThread();
    }
});




