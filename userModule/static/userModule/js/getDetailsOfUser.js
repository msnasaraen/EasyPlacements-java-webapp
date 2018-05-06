$(document).ready(function () {
   $.ajax({
       url: 'http://127.0.0.1:8000/user/getUserDetails/',
       data: "",
       error: function() {
          $('#info').html('<p>An error has occurred</p>');
       },
       dataType: 'json',
       success: function(data) {
          //alert(JSON.stringify(data));
          $('.btn-primary[data-title="'+data.gender+'"]').click();
          $("#userDetails").autofill( data );
          //$("#photoFormUser").autofill( data );
          if(data.resume!="" && !(typeof data.resume === "undefined")){
              $("#userResume").css("display","block");
              $("#edit_user_resume_a").attr("src",data.resume);
              $("#edit_user_resume_a").attr("href",data.resume);
              $('#edit_user_resume_a').attr("download",data.resume.substr(data.resume.lastIndexOf("/") + 1));
              $('#edit_user_resume').attr("src",data.resume);
          }
          if(data.profilepicture!="" && !(typeof data.profilepicture === "undefined")){
              $("#userPicture").css("display","block");
              $("#edit_user_picture_a").attr("src",data.profilepicture);
              $("#edit_user_picture_a").attr("href",data.profilepicture);
              $('#edit_user_picture_a').attr("download",data.profilepicture.substr(data.profilepicture.lastIndexOf("/") + 1));
              $('#edit_user_picture').attr("src",data.profilepicture);
          }
       },
       type: 'GET'
    });
});