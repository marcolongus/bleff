$('#enter').click(
    function(event) {
      console.log(event);
      event.preventDefault() // Para no renderizar         
      
      $.ajax({
          url: '/post_definition',
          method: 'POST',
          contentType: "application/json",
          data: JSON.stringify({
              definition: $('#definition').val(),                
          }),
          
          complete: function () {
            window.location.href = "/lobby"
          },

          success: function (response) {
            console.log(response);
            alert('ENVIADO/RECIBIDO')
          },  

          error: function(error) {
            console.log('Error message:', error.responseText);
            console.log('Error status:', error.status);              
          }


      });
    }
  )