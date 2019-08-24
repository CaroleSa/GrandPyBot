
$("button").on('click', function () {
    var $textareaValueElt = $('textarea').val();
    if ($textareaValueElt.length > 3) {
 	    $('#thread').append("<p> Utilisateur : "+ $textareaValueElt +" </p>");
 	    $('textarea').val('').change();
    }else {
  	    $('textarea').val('').change();
    }
});