$(document).ready(function () {
        $.ajax({
           url: 'http://127.0.0.1:8000/user/getDetails/',
           error: function() {
              $('#info').html('<p>An error has occurred</p>');
           },
           dataType: 'json',
           success: function(data) {
              if(data.status=="success")
                $("#username-header").html(data.username);
                $("#username-sidebar").html(data.username);
                $('#profile-header').attr("src",data.profilepicture);
                $('#profile-sidebar').attr("src",data.profilepicture);
           },
           type: 'GET'
        });
});