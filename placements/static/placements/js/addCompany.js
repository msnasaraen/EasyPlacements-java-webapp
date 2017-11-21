$(document).ready(function () {

    $('#demo').on('change', function() {
      //alert( $(this).next().children().first().attr("title"));
      $(this).value = $(this).next().children().first().attr("title");
      $("#depts").val($(this).val());
      //alert($(this).val());
      //alert($("#depts").val());
    })
    $("#addCompany").click(function(){
        //e.preventDefault();
        //e.stopPropagation();
        //alert("hii");
        var companyDetails = objectifyForm($("#addCompany_form").serializeArray());
        var formData = new FormData($('#logo')[0].files[0]);
        var data = {"companyDetails":companyDetails,"file":formData};
        //formData.append("CompanyDetails",companyDetails);
        //formData.append('csrfmiddlewaretoken', '{{ csrf_token }}');

        //var img = $('#logo')[0].files[0];
        //formData.append("image",img);
        $.ajax({
           url: 'http://127.0.0.1:8000/placements/addCompanyDetails/',
           data:formData,
           processData: false,
           contentType: false,
           error: function() {
              $('#info').html('<p>An error has occurred</p>');
           },
           dataType: 'json',
           success: function(data) {
            alert("success");
           },
           type: 'GET'
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