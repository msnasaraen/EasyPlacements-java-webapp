$(document).ready(function(){

    $('#radioBtn a').on('click', function(){
    var sel = $(this).data('title');
    var tog = $(this).data('toggle');
    $('#'+tog).prop('value', sel);

    $('a[data-toggle="'+tog+'"]').not('[data-title="'+sel+'"]').removeClass('active').addClass('notActive');
    $('a[data-toggle="'+tog+'"][data-title="'+sel+'"]').removeClass('notActive').addClass('active');
    })

    $('#next').click(function () {

        var adminDetails = objectifyForm($('#adminDetails').serializeArray());
        alert(JSON.stringify(adminDetails));
        $.ajax({
           url: 'http://127.0.0.1:8000/user/addAdminDetails/',
           data: adminDetails,
           error: function() {
              $('#info').html('<p>An error has occurred</p>');
           },
           dataType: 'json',
           success: function(data) {
              alert("whooyaa");
           },
           type: 'POST'
        });

    });

    $('#finish').click(function () {

        $('#photoFormAdmin').submit();

    });

    $('#submitLogin').click(function(){
        var userDetails = objectifyForm($('#loginform').serializeArray());
        $.ajax({
           url: 'user/login_user/',
           data: userDetails,
           error: function() {
              $('#info').html('<p>An error has occurred</p>');
           },
           dataType: 'json',
           success: function(data) {
              if(data.status=="success")
              {
                var details = data.Details;
                if(details.type == "admin"){
                    if(details.isApproved=="yes"){
                        $("#index").submit();
                    }
                    else{
                        $("#provideDetailsAdmin").submit();

                    }
                }
                else{
                    if(details.isApproved=="yes"){
                    }
                    else{
                        $("#provideDetailsUser").submit();
                    }
                }
              }
           },
           type: 'POST'
        });
    });
    
    $('#submitRegister').click(function () {
        var userDetails = objectifyForm($('#registerform').serializeArray());
        $.ajax({
           url: 'user/register/',
           data: userDetails,
           error: function() {
              $('#info').html('<p>An error has occurred</p>');
           },
           dataType: 'json',
           success: function(data) {
              if(data.status=="success")
              {
                var details = data.Details;
                if(details.type == "admin"){
                    if(details.isApproved=="yes"){
                        $("#index").submit();
                    }
                    else{
                        $("#provideDetailsAdmin").submit();

                    }
                }
                else{
                    if(details.isApproved=="yes"){
                    }
                    else{
                        $("#provideDetailsUser").submit();
                    }
                }
              }

           },
           type: 'POST'
        });
    });

    function objectifyForm(formArray) {//serialize data function
      var returnArray = {};
      for (var i = 0; i < formArray.length; i++){
        returnArray[formArray[i]['name']] = formArray[i]['value'];
      }
      return returnArray;
    }


});
