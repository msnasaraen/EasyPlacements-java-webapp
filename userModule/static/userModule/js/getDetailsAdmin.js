$(document).ready(function () {
   $.ajax({
       url: 'http://127.0.0.1:8000/user/getAdminDetails/',
       data: "",
       error: function() {
          $('#info').html('<p>An error has occurred</p>');
       },
       dataType: 'json',
       success: function(data) {
          //alert(JSON.stringify(data));
          $('.btn-primary[data-title="'+data.gender+'"]').click();
          $("#adminDetails").autofill( data );
          //$("#photoFormAdmin").autofill( data );
          if(data.profilepicture!="" &&  !(typeof data.profilepicture === "undefined")){
              $("#adminPicture").css("display","block");
              $("#edit_admin_picture_a").attr("src",data.profilepicture);
              $("#edit_admin_picture_a").attr("href",data.profilepicture);
              $('#edit_admin_picture_a').attr("download",data.profilepicture.substr(data.profilepicture.lastIndexOf("/") + 1));
              $('#edit_admin_picture').attr("src",data.profilepicture);
          }
       },
       type: 'GET'
    });
});