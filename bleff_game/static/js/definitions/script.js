$(document).ready(function(){
    $("#send-definition").on("submit", function(event){
        event.preventDefault();
        const word = $("#word-button").text();                
        const definition = $("#definition").val();

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
