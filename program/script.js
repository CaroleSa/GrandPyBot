
$("button").on('click', function () {
    $('#thread').append("<p> Utilisateur : "+ $('textarea').val() +" </p>");
    $('textarea').val('').change();
});