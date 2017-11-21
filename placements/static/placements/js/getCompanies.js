$(document).ready(function(){

    $.ajax({
           url: 'http://127.0.0.1:8000/placements/getCompanies/',
           data:'getDetails',
           processData: false,
           contentType: false,
           error: function() {
              $('#info').html('<p>An error has occurred</p>');
           },
           dataType: 'json',
           success: function(data) {
        /*       var html='';
                for(var i=0;i<data.length;i++){
                    html=html+parse(data[i]);
                }
                console.log(html);*/

                var template =  Handlebars.compile( $('#handlebar_template').html());


                $('.row').html(template(data));
           },
           type: 'GET'
        });



});