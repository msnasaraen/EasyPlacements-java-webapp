$(document).ready(function(){

    var template_view =  Handlebars.compile( $('#handlebar_template_view_company').html());
    var template =  Handlebars.compile( $('#handlebar_template').html());

    $(".right_col").css('min-height', $(window).height());
    $('.right_col').addClass('importantRule');

    $('#checkall_admin').click(function () {
            $(".check_admin").prop('checked', $(this).prop('checked'));
    });

    $('#checkall_user').click(function () {
            $(".check_user").prop('checked', $(this).prop('checked'));
    });

    $('#demo').on('change', function() {
      $(this).value = $(this).next().children().first().attr("title");
      $("#depts").val($(this).val());;
    })

    $('#demo_details').on('change', function() {
      $(this).value = $(this).next().children().first().attr("title");
      $("#depts_edit").val($(this).val());;
    })

    $('#demo_admin').on('change', function() {
      $(this).value = $(this).next().children().first().attr("title");
      $("#depts_admin").val($(this).val());;
    })

    $('#demo_user').on('change', function() {
      $(this).value = $(this).next().children().first().attr("title");
      $("#depts_user").val($(this).val());;
    })
    $('#filter_dept_user').click(function () {
       var depts = $('#depts_user').val();
       if(depts.length<=0)
           return;
       var jsonData = {"depts":depts};
       $.ajax({
               url: 'http://127.0.0.1:8000/placements/filterUser/',
               data:jsonData,
               error: function() {
                  $('#info').html('<p>An error has occurred</p>');
               },
               dataType: 'json',
               success: function(data) {
                   fillUser(data);
               },
               type: 'GET'
           });
    });

    $('#filter_dept_admin').click(function () {
       var depts = $('#depts_admin').val();
       if(depts.length<=0)
           return;
       var jsonData = {"depts":depts};
       $.ajax({
               url: 'http://127.0.0.1:8000/placements/filterAdmin/',
               data:jsonData,
               error: function() {
                  $('#info').html('<p>An error has occurred</p>');
               },
               dataType: 'json',
               success: function(data) {
                   fillAdmin(data);
               },
               type: 'GET'
           });
    });

    $(document).on('click','button',function(){
       if(this.getAttribute("name")=="view_company") {
           $.ajax({
               url: 'http://127.0.0.1:8000/placements/viewCompany/'+this.getAttribute("id"),
               data:'getDetails',
               processData: false,
               contentType: false,
               error: function() {
                  $('#info').html('<p>An error has occurred</p>');
               },
               dataType: 'json',
               success: function(data) {
                   $('#view_company_content').html(template_view(data));
                    $('.right_col').addClass('hide');
                    $('.company_details').removeClass('hide');
               },
               type: 'GET'
           });

       }
       if(this.getAttribute("name")=="delete_company") {
           $.ajax({
               url: 'http://127.0.0.1:8000/placements/deleteCompany/'+this.getAttribute("id"),
               data:'getDetails',
               error: function() {
                  $('#info').html('<p>An error has occurred</p>');
               },
               dataType: 'json',
               success: function(data) {
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
                                $('.companiesdiv').html(template(data));
                           },
                           type: 'GET'
                    });
                    $('.right_col').addClass('hide');
                    $('.companies').removeClass('hide');
               },
               type: 'GET'
           });

       }
    });

    $(document).on('click','a',function(){
       if(this.getAttribute("name")=="edit_company") {
           $.ajax({
               url: 'http://127.0.0.1:8000/placements/viewCompany/'+this.getAttribute("id"),
               data:'getDetails',
               processData: false,
               contentType: false,
               error: function() {
                  $('#info').html('<p>An error has occurred</p>');
               },
               dataType: 'json',
               success: function(data) {
                    $('.right_col').addClass('hide');
                    $("#edit_image").attr('src',data.company_logo);
                    $("#editCompany_form").autofill( data );
                    $('.update_company').attr("id",data.company_id);
                    var departments = data.depts.split(',');
                    for(var i=0;i<departments.length;i++){
                        $("#demo_details option[value='"+departments[i].toLowerCase()+"']").attr("selected","selected");
                    }
                    $('.company_details_edit').removeClass('hide');
                    var items = $('#demo_details').next().find('.multiselect-container li');
                    var selected_text = '';
                    items.each(function(idx, li) {
                        var product = $(li);
                        $(li).find('input').removeAttr('checked');
                        if(departments.indexOf($.trim($(li).text()))>=0) {
                            $(li).addClass('active');
                            $(li).find('input').attr('checked', 'checked');
                            selected_text+=$.trim($(li).text())+' ,';
                        }
                        // and the rest of your code
                    });
                    selected_text = selected_text.substring(0,selected_text.length-1);
                    $('#demo_details').next().find('.multiselect-selected-text').html(selected_text);
                   },
                   type: 'GET'
               });
       }
       if(this.getAttribute("name")=="update_company") {
           $('.right_col').addClass('hide');
           var newDetails = objectifyForm($('#editCompany_form').serializeArray());
           var id = this.getAttribute("id");
           $.ajax({
                   url: 'http://127.0.0.1:8000/placements/updateCompany/'+this.getAttribute("id")+'/',
                   data:newDetails,
                   error: function() {
                      $('#info').html('<p>An error has occurred</p>');
                   },
                   dataType: 'json',
                   success: function(data) {
                       $.ajax({
                           url: 'http://127.0.0.1:8000/placements/viewCompany/'+id,
                           data:'getDetails',
                           processData: false,
                           contentType: false,
                           error: function() {
                              $('#info').html('<p>An error has occurred</p>');
                           },
                           dataType: 'json',
                           success: function(data) {
                               $('#view_company_content').html(template_view(data));
                                $('.right_col').addClass('hide');
                                $('.company_details').removeClass('hide');
                           },
                           type: 'GET'
                       });
                   },
                   type: 'POST'
            });
       }
    });

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
               // var template =  Handlebars.compile( $('#handlebar_template').html());
                $('.companiesdiv').html(template(data));
           },
           type: 'GET'
    });


    $('#get_companies').click(function () {
       $(document).find("li").removeClass("active");
       $('#get_companies').parent().addClass("active");
       $('#get_companies').parent().parent().parent().addClass("active");
       $('.right_col').addClass('hide');
       $('.companies').removeClass('hide');
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
               // var template =  Handlebars.compile( $('#handlebar_template').html());
                $('.companiesdiv').html(template(data));
           },
           type: 'GET'
        });
    });


   $('#approveUsers').click(function () {
        var inputs = $(".check_user");
        var id=[];
        var j=0;
        for(var i = 0; i < inputs.length; i++){
            if(inputs[i].checked)
                id[j++]=$(inputs[i]).val();
        }
       // alert(id);
       var csrf = $('[name="csrfmiddlewaretoken"]').val();
       var data = {"csrfmiddlewaretoken":csrf,"id":id};
       //alert(JSON.stringify(data));
       $.ajax({
           url: 'http://127.0.0.1:8000/placements/approvethisadmin/',
           data:data,
           error: function() {
              $('#info').html('<p>An error has occurred</p>');
           },
           dataType: 'json',
           success: function(data) {
               //alert("Whoo");
               $('#get_users').click();
           },
           type: 'POST'
        });

   });

   $('#get_users').click(function () {
       $(document).find("li").removeClass("active");
       $('#get_users').parent().parent().parent().addClass("active");
       $('#get_users').parent().addClass("active");
       $('.right_col').addClass('hide');
       $('.approve_user').removeClass('hide');
        $.ajax({
           url: 'http://127.0.0.1:8000/placements/getUsersForApproval/',
           data:'getDetails',
           processData: false,
           contentType: false,
           error: function() {
              $('#info').html('<p>An error has occurred</p>');
           },
           dataType: 'json',
           success: function(data) {
               fillUser(data);
           },
           type: 'GET'
        });

   });

   function  fillUser(data) {
        var html='';
        for(var i=0;i<data.length;i++){
            html=html+parse(data[i]);
        }
        console.log(html);
        $("#tablebody_user").html(html);
   }

    function parse(data) {
        return ""+
          '<tr>'+
            '<td class="a-center">'+
              '<input type="checkbox" name="id" value="'+data.id+'" class="check_user">'+
            '</td>'+
            '<td class=" ">'+data.name+'</td>'+
            '<td class=" ">'+data.rollno+'</td>'+
            '<td class=" ">'+data.email+'</td>'+
            '<td class=" ">'+data.year+'</td>'+
            '<td class=" ">'+data.branch+'</td>'+
            '<td class=" "><img style="width: 50px;height: 50px;" src='+data.url+'></td>'+
            '</td>'+
          '</tr>';

    }


    $('#approveAdmin').click(function () {
        var inputs = $(".check_admin");
        var id=[];
        var j=0;
        for(var i = 0; i < inputs.length; i++){
            if(inputs[i].checked)
                id[j++]=$(inputs[i]).val();
        }
       // alert(id);
       var csrf = $('[name="csrfmiddlewaretoken"]').val();
       var data = {"csrfmiddlewaretoken":csrf,"id":id};
       //alert(JSON.stringify(data));
       $.ajax({
           url: 'http://127.0.0.1:8000/placements/approvethisadmin/',
           data:data,
           error: function() {
              $('#info').html('<p>An error has occurred</p>');
           },
           dataType: 'json',
           success: function(data) {
               //alert("Whoo");
               $('#get_admins').click();
           },
           type: 'POST'
        });

   });


   $('#get_admins').click(function () {

       $(document).find("li").removeClass("active");
       $('#get_admins').parent().parent().parent().addClass("active");
       $('#get_admins').parent().addClass("active");
       $('.right_col').addClass('hide');
       $('.approve_admin').removeClass('hide');

       $.ajax({
           url: 'http://127.0.0.1:8000/placements/getAdminForApproval/',
           data:'getDetails',
           processData: false,
           contentType: false,
           error: function() {
              $('#info').html('<p>An error has occurred</p>');
           },
           dataType: 'json',
           success: function(data) {
               fillAdmin(data);
           },
           type: 'GET'
        });


   });

    function fillAdmin(data) {
        var html='';
        for(var i=0;i<data.length;i++){
            html=html+parseadmin(data[i]);
        }
        console.log(html);
        $("#tablebody_admin").html(html)
    }


    function parseadmin(data) {
        return ""+
          '<tr>'+
            '<td class="a-center">'+
              '<input type="checkbox" name="id" value="'+data.id+'" class="check_admin">'+
            '</td>'+
            '<td class=" ">'+data.name+'</td>'+
            '<td class=" ">'+data.rollno+'</td>'+
            '<td class=" ">'+data.email+'</td>'+
            '<td class=" ">'+data.year+'</td>'+
            '<td class=" ">'+data.branch+'</td>'+
            '<td class=" "><img style="width: 50px;height: 50px;" src='+data.url+'></td>'+
            '</td>'+
          '</tr>';

    }



    $("#addCompany").click(function(){
        var companyDetails = objectifyForm($("#addCompany_form").serializeArray());
        //var formData = new FormData($('#logo')[0].files[0]);
        //var data = {"companyDetails":companyDetails,"file":formData};

        var form_data = new FormData();
        form_data.append('company_logo', $('#logo')[0].files[0]);
        form_data.append('companyDetails',JSON.stringify(companyDetails));
        $.ajax({
           url: 'http://127.0.0.1:8000/placements/addCompanyDetails/',
           data:form_data,
           headers:{'X-CSRFToken': $('[name="csrfmiddlewaretoken"]').val()},
           processData: false,
           contentType: false,
           error: function() {
              $('#info').html('<p>An error has occurred</p>');
           },
           success: function(data) {
            alert("Company Added Successfully");
            $("#addCompany_form").find("input, textarea").val("");
            $('#get_companies').click();
           },
           type: 'POST',
        });
    });

    function objectifyForm(formArray) {//serialize data function
      var returnArray = {};
      for (var i = 0; i < formArray.length; i++){
        returnArray[formArray[i]['name']] = formArray[i]['value'];
      }
      return returnArray;
    }

    $('#add_company_page').click(function () {
       $(document).find("li").removeClass("active");
       $('#add_company_page').parent().parent().parent().addClass("active");
       $('#add_company_page').parent().addClass("active");
       $('.right_col').addClass('hide');
       $('.add_company_form').removeClass('hide');
    });

});