
$("button").on('click', function () {
    $('#thread').append(' Utilisateur : ' + $('textarea').val());
    $('textarea').val('').change();
});