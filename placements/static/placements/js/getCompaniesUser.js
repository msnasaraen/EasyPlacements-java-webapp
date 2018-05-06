$(document).ready(function(){
    var template =  Handlebars.compile( $('#handlebar_template').html());
    var edit_template =  Handlebars.compile( $('#handlebar_template').html());
    $.ajax({
       url: 'http://127.0.0.1:8000/placements/getCompaniesUser/',
       data:'getDetails',
       processData: false,
       contentType: false,
       error: function() {
          $('#info').html('<p>An error has occurred</p>');
       },
       dataType: 'json',
       success: function(data){
            $('.companiesdiv').html(template(data));
       },
       type: 'GET'
    });

    $('#elligible').click(function () {
         $.ajax({
           url: 'http://127.0.0.1:8000/placements/getElligibleCompaniesUser/',
           data:'getDetails',
           processData: false,
           contentType: false,
           error: function() {
              $('#info').html('<p>An error has occurred</p>');
           },
           dataType: 'json',
           success: function(data){
                $('.elligiblecompaniesdiv').html(edit_template(data));

                $(document).find("li").removeClass("active");
                   $('#elligible').parent().parent().parent().addClass("active");
                   $('#elligible').parent().addClass("active");
                $('.right_col').addClass('hide');
                $('.elligible_companies').removeClass('hide');
           },
           type: 'GET'
        });
    });

    $('#get_companies').click(function () {
          $.ajax({
           url: 'http://127.0.0.1:8000/placements/getCompaniesUser/',
           data:'getDetails',
           processData: false,
           contentType: false,
           error: function() {
              $('#info').html('<p>An error has occurred</p>');
           },
           dataType: 'json',
           success: function(data){
                $('.companiesdiv').html(template(data));
                $(document).find("li").removeClass("active");
                $('#get_companies').parent().parent().parent().addClass("active");
                $('#get_companies').parent().addClass("active");
                $('.right_col').addClass('hide');
                $('.companies').removeClass('hide');
           },
           type: 'GET'
        });
    });

    var template_view =  Handlebars.compile( $('#handlebar_template_view_company').html());

    $(document).on('click','button',function() {
        if (this.getAttribute("name") == "view_company") {
            $.ajax({
                url: 'http://127.0.0.1:8000/placements/viewCompanyUser/' + this.getAttribute("id"),
                data: 'getDetails',
                processData: false,
                contentType: false,
                error: function () {
                    $('#info').html('<p>An error has occurred</p>');
                },
                dataType: 'json',
                success: function (data) {
                    $('#view_company_content').html(template_view(data));
                    $('.right_col').addClass('hide');
                    $('.company_details').removeClass('hide');
                },
                type: 'GET'
            });

        }
    });
});