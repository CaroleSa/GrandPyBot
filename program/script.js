
$("button").on('click', function () {
    var $textareaValueElt = $('textarea').val();
    if (($textareaValueElt.length > 3)&&($textareaValueElt.indexOf("<>"))) {
 	    $('#thread').append("<p><span id='userName'> Utilisateur : </span>"+ $textareaValueElt +" </p>");
 	    $('textarea').val('').change();
    }else {
  	    $('textarea').val('').change();
    }
});