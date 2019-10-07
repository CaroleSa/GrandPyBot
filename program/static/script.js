// hide the loader and the map
$('#loader').hide();
$('#space2').show();
$("#rowMap").hide();

// getQuestionInThread function
function getQuestionInThread() {
    // get user's question
    var $textareaValueElt = $('textarea').val();

    // display user's question in the thread
    $('#messageThread').append("<br><p id='message'><span id='userName'> Utilisateur : <br></span>" + $textareaValueElt + "</p>");
    // delete TextMap in the last GrandPy Bot's answer
    $(".textMap").remove();

    // display the last text in the thread
    element = document.getElementById('thread');
	element.scrollTop = element.scrollHeight;

	// use ajax
    $.ajax({
            // post user's question in the backend
			data : {question: $('textarea').val()},
			type : 'POST',
			url : '/process'
	})

	.done(function(data) {
	    // hide loader
	    $('#loader').hide();
	    $('#space2').show();

	    if(data.error){
	            // display GrandPy Bot's answer in the thread
				$('#messageThread').append("<br><p id='message'><span id='robotName'> GrandPy Bot : <br></span>" + data.error + "</p>");

				// display the last text in the thread
				element = document.getElementById('thread');
	            element.scrollTop = element.scrollHeight;
				return

		}if(data.latitude){
		        // display GrandPy Bot's answer in the thread
                $('#messageThread').append("<br><p id='message'><span id='robotName'> GrandPy Bot : <br></span>" + data.address + "</p>");

                // display the last text in the thread
                element = document.getElementById('thread');
	            element.scrollTop = element.scrollHeight;

	            // display GrandPy Bot's answer in the thread
	            $('#messageThread').append("<p id='message'>" + data.history + "</p>");
	            $('#messageThread').append("<p class='textMap' id='message'>" + data.map + "</p>");

	            // display the map
                $("#rowMap").show();
                var map;
                var marker;

                // initMap function: creation of the map
                function initMap() {
                    var LatLng = {lat: data.latitude, lng: data.longitude};
                    map = new google.maps.Map(document.getElementById('map'), {
                    center: LatLng,
                    zoom: 15
                    });
                    marker = new google.maps.Marker({
                    position: LatLng,
                    map: map
                    });
                }
                // call initMap function
                initMap();
                }
    });
    // delete user's question in textarea
 	$('textarea').val('').change();
}

// if the user click in the button
$("button").on('click', function () {
    // display loader and hide the map
    $('#loader').show();
    $('#space2').hide();
    $("#rowMap").hide();
    // call getQuestionInThread function
    getQuestionInThread();
});

// if the user presses the space key
$("textarea").keyup(function(e) {
    if (e.keyCode == 13) {
        // display loader and hide the map
        $('#loader').show();
        $('#space2').hide();
        $("#rowMap").hide();
        // call getQuestionInThread function
        getQuestionInThread();
    }
});
