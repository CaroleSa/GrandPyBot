$('#loader').hide();
$('#space2').show();
$("#rowMap").hide();


function getQuestionInThread() {
    var $textareaValueElt = $('textarea').val();
    $('#messageThread').append("<br><p id='message'><span id='userName'> Utilisateur : <br></span>" + $textareaValueElt + "</p>");
    $(".textMap").remove();
    element = document.getElementById('thread');
	element.scrollTop = element.scrollHeight;
    $.ajax({
			data : {question: $('textarea').val()},
			type : 'POST',
			url : '/process'
	})

	.done(function(data) {
	    $('#loader').hide();
	    $('#space2').show();

	    if(data.error){
				$('#messageThread').append("<br><p id='message'><span id='robotName'> GrandPy Bot : <br></span>" + data.error + "</p>");
				element = document.getElementById('thread');
	            element.scrollTop = element.scrollHeight;
				return

		}if(data.latitude){
                $('#messageThread').append("<br><p id='message'><span id='robotName'> GrandPy Bot : <br></span>" + data.address + "</p>");
                element = document.getElementById('thread');
	            element.scrollTop = element.scrollHeight;
	            $('#messageThread').append("<p id='message'>" + data.history + "</p>");
	            $('#messageThread').append("<p class='textMap' id='message'>" + data.map + "</p>");
                $("#rowMap").show();
                var map;
                var marker;
                function initMap() {
                    var LatLng = {lat: data.latitude, lng: data.longitude};
                    map = new google.maps.Map(document.getElementById('map'), {
                    center: LatLng,
                    zoom: 15
                    });
                    marker = new google.maps.Marker({
                    position: LatLng,
                    map: map,
                    title: 'Hello World!'
                    });
                }

                initMap();
                $('#map').css('height','180px');
                $('#map').css('max-width','100%');
                $('#map').css('margin','10px');
                $('#map').css('border-left','5px white inset');
                $('#map').css('border-right',' 5px white inset');
                $('#map').css('border-top',' 5px white inset');
                $('#map').css('border-bottom',' 5px white inset');

                }else{
                    $('#messageThread').append("<br><p id='message'><span id='robotName'> GrandPy Bot : <br></span>" + data.address + "</p>");
                    element = document.getElementById('thread');
	                element.scrollTop = element.scrollHeight;
	                $('#messageThread').append("<p id='message'>" + data.history + "<br>" + data.map + "</p>");
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




