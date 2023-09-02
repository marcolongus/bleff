$(document).ready(function(){
    $("form").on("submit", function(event){
        event.preventDefault();

        const word = $("input[name='word']").val();
        const definition = $("input[name='definition']").val();

        $.ajax({
            url: '/submit_definition',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ word, definition }),
            success: function(response){
                console.log("Definition submitted successfully")
            },
            error: function(error){
                console.log("Error submitting definition")
            }
        });
    });
});
