$('#loader').hide();
$("#rowMap").hide();

function getQuestionInThread() {
    var $textareaValueElt = $('textarea').val();
    $('#thread').append("<p><span id='userName'> Utilisateur : <br></span>" + $textareaValueElt + "</p>");
    $.ajax({
			data : {question: $('textarea').val()},
			type : 'POST',
			url : '/process'
	})
	.done(function(data) {
	    $('#loader').hide();
	    if(data.error){
				$('#thread').append("<p><span id='robotName'> GrandPy Bot : <br></span>" + data.error + "</p>");
				return
		}if(data.latitude){
                $('#thread').append("<p><span id='robotName'> GrandPy Bot : <br></span>" + data.address + "<br>"
                + data.history + "<br>" + data.map + "</p>");
                $("#rowMap").show();
                var map;
                function initMap() {
                    map = new google.maps.Map(document.getElementById('map'), {
                    center: {lat: data.latitude, lng: data.longitude},
                    zoom: 18
                    });
                }
                initMap();
                $('#map').css('height','200px');
                $('#map').css('width','430px');
                $('#map').css('border-left','5px white inset');
                $('#map').css('border-right',' 5px white inset');
                $('#map').css('border-top',' 5px white inset');
                $('#map').css('border-bottom',' 5px white inset');

                }else{
                    $("#rowMap").hide();
                    $('#thread').append("<p><span id='robotName'> GrandPy Bot : <br></span>" + data.address + "<br>"
                    + data.history + "<br>" + data.map + "</p>");
                    }


    });

 	$('textarea').val('').change();
}



$("button").on('click', function () {
    $('#loader').show();
    $("#rowMap").hide();
    getQuestionInThread();
});

$("textarea").keyup(function(e) {
    if (e.keyCode == 13) {
        $('#loader').show();
        $("#rowMap").hide();
        getQuestionInThread();
    }
});




