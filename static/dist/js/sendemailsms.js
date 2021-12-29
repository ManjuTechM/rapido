//send trip details

function sendTripEmail(Tripid){

                swal({
                  title:"Want to send Trip Email to Customer?", 
                  icon:"warning",
                  buttons:["Cancel","Send"]
                }).then((willDelete) => {
                      if (willDelete) {
                        $('#loader').css("display","block");
                $.get('/rapido/sendtripdetailemail/'+Tripid+'/',function(data){
              if(data){
                        $('#loader').hide();
                swal({
                  title:"Email sent successfully",
                  icon:"success"
                }).then(function(){
                  window.location.reload();
                });
              }
                });
                      } else {
                        console.log("hello");
                      }
                    });
}


function sendTripSmsUser(Tripid){

                swal({
                  title:"Want to send Trip SMS to Customer?",
                  icon:"warning",
                  buttons:["Cancel","Send"]
                }).then((willDelete) => {
                      if (willDelete) {
                        $('#loader').css("display","block");
                $.get('/rapido/sendtripdetailsmsforuser/'+Tripid+'/',function(data){
              if(data){
                        $('#loader').hide();
                swal({
                  title:"Message sent successfully",
                  icon:"success"
                }).then(function(){
                  window.location.reload();
                });
              }
                });
                      } else {
                        console.log("hello");
                      }
                    });
}


function sendTripSmsDriver(Tripid){

                swal({
                  title:"Want to send Trip SMS to Driver?",
                  icon:"warning",
                  buttons:["Cancel","Send"]
                }).then((willDelete) => {
                      if (willDelete) {
                        $('#loader').css("display","block");
                $.get('/rapido/sendtripdetailsmsfordriver/'+Tripid+'/',function(data){
              if(data){
                        $('#loader').hide();
                swal({
                  title:"Message sent successfully",
                  icon:"success"
                }).then(function(){
                  window.location.reload();
                });
              }
                });
                      } else {
                        console.log("hello");
                      }
                    });
}

function sendEmail(bookingid){

                swal({
                  title:"Want to send Email to Customer?",
                  icon:"warning",
                  buttons:["Cancel","Send"]
                }).then((willDelete) => {
                      if (willDelete) {
                        $('#loader').css("display","block");
                $.get('/rapido/sendbookingemail/'+bookingid+'/',function(data){
              if(data){
                        $('#loader').hide();
                swal({
                  title:"Email sent successfully",
                  icon:"success"
                }).then(function(){
                  window.location.reload();
                });
              }
                });
                      } else {
                        console.log("hello");
                      }
                    });
}


function sendMessage(bookingid){

                swal({
                  title:"Want to send SMS to Customer?",
                  icon:"warning",
                  buttons:["Cancel","Send"]
                }).then((willDelete) => {
                      if (willDelete) {
                        $('#loader').css("display","block");
                $.get('/rapido/sendbookingsms/'+bookingid+'/',function(data){
              if(data){
                        $('#loader').hide();
                swal({
                  title:"Message sent successfully",
                  icon:"success"
                }).then(function(){
                  window.location.reload();
                });
              }
                });
                      } else {
                        console.log("hello");
                      }
                    });
}


  //cancel button action

  function cancelBooking(bookingid,buttonid){

    var id = $(buttonid).attr("id"); //get id
    var noteValue = $("#note"+bookingid).val(); //get notevalue
    var reasonValue = $('input[name=reason]:checked').val(); //get reason value
    
    console.log($("#cancel_form"+bookingid));
    var cancelJson = {          //convert to json object
      "id":bookingid,
      "reason":reasonValue,
      "note":noteValue
    };
    
        if($("#cancel_form"+bookingid).valid()){
          $.ajax({            //send json-object to api and read response
              url: '/rapido/cancelbooking/'+bookingid+"/",
              method: "POST",
              data: $("#cancel_form"+bookingid).serialize(),
              success: function(res) {
                console.log(res);
                  swal({
                    title:"Booking cancelled successfully",
                    icon:"success"
                  }).then((will)=>{
                    if(will){
                      location.reload();
                    }
                  });
              }
          });
        }
    
    }
    
    //cancel button action


//date range picker 

  // var bookDate = new Date();
  // bookDte = moment(bookDate).format('YYYY-MM-DD');
  //   bookMaster = '/rapido/admin_datewisebookings/'+bookDte+'/'+bookDte;
  //   bookStaff = '/rapido/staff_datewisebookings/'+bookDte+'/'+bookDte;
  //   $("#bookingMaster").attr("href",bookMaster);
  //   $("#bookingStaff").attr("href",bookStaff);


//date range picker master 
$(function() {

  var start = moment();
  var end = moment();
  var startDate;
  var endDate;
  var url;
  
  function cb(start, end) {
  $('#reportrange1').html(start.format('MMMM D, YYYY') + ' - ' + end.format('MMMM D, YYYY'));
  startDate = start.format('YYYY-MM-DD');
  endDate = end.format('YYYY-MM-DD');
  // console.log(startDate);
  // console.log(endDate);
  
  // $.get(url,function(data){
  
  //   console.log(data);
  //   // $("html").html(data);
  // });
  }
  $('#reportrange1').daterangepicker({
  startDate: start,
  endDate: end
  }, cb);

  $('#reportrange1').on('apply.daterangepicker', function(ev, picker) {
  console.log(picker.startDate.format('YYYY-MM-DD'));
  console.log(picker.endDate.format('YYYY-MM-DD'));
  dataUrl = "/rapido/master/";
  url=dataUrl+startDate+"/"+endDate+"/";
  console.log(url);
  location.href=url;
  
  });
  
  cb(start, end);
  // location.href=url;
  
  });
  

//date range picker staff 
$(function() {

  var start = moment();
  var end = moment();
  var startDate;
  var endDate;
  var url;
  
  function cb(start, end) {
  $('#reportrange2').html(start.format('MMMM D, YYYY') + ' - ' + end.format('MMMM D, YYYY'));
  startDate = start.format('YYYY-MM-DD');
  endDate = end.format('YYYY-MM-DD');
  // console.log(startDate);
  // console.log(endDate);
  
  // $.get(url,function(data){
  
  //   console.log(data);
  //   // $("html").html(data);
  // });
  }
  
  $('#reportrange2').daterangepicker({
  startDate: start,
  endDate: end
  }, cb);
  
  $('#reportrange2').on('apply.daterangepicker', function(ev, picker) {
  console.log(picker.startDate.format('YYYY-MM-DD'));
  console.log(picker.endDate.format('YYYY-MM-DD'));
  dataUrl = "/rapido/staff/";
  url=dataUrl+startDate+"/"+endDate+"/";
  console.log(url);
  location.href=url;
  
  });
  
  cb(start, end);
  // location.href=url;
  
  });  

//----create bookings autofill
$(function(){

  var url = '/rapido/api/get_bookerlist/';
  var companyId;
//data auto-fill
var bookername = [];
var onetwo;
$('#search').on('autocompleteclose', function (e, ui) {
  companyId = $("#companyid").val();
  });

$("#booker_name").autocomplete({
  source:bookername,
  select: function( event, ui ) {
        $(this).val(ui.item.label);
        $( "#booker_phone" ).val( ui.item.booking_phoneno);
        $( "#booker_email" ).val( ui.item.booking_email); //ui.item is your object from the array
        return false;
    }
  }).focus(function(){
    $.getJSON(url+companyId+'/', function(data) {
      $.each(data,function(key,value){
        bookername.push(value);
      });
  });

  $("#booker_name").autocomplete("option",{   //refresh autocomplete and update
    source:bookername
  });

  }).focusout(function(){
      bookername = [];
  });

});


//----this is for assign cab autofill
$(function(){

  var url = '/rapido/api/chauffeur_vehicel_list/';
  var vendorId;
//data auto-fill
var chauffeurname = [];
var onetwo;
$('#vensearch').on('autocompleteclose', function (e, ui) {
  vendorId = $("#vendorid").val();
  });

$("#vehicle_no").autocomplete({
  source:chauffeurname,
  select: function( event, ui ) {
        $(this).val(ui.item.label);
        $( "#chauffeur_phone" ).val( ui.item.chauffeur_phoneno);
        $( "#vehicle_model" ).val( ui.item.vehicle_modelname);
        $( "#chauffeur_name" ).val( ui.item.chauffeur_name);
        $("#vensearch").val(ui.item.vendor.vendor_name);
        $("#vendorid").val(ui.item.vendor.id);
        $( "#chauffeur_dl" ).val( ui.item.chauffeur_drivinglicense); //ui.item is your object from the array
        return false;
    }
  }).focus(function(){
    $.getJSON(url, function(data) {
      data = JSON.stringify(data);
      data = data.replace(/\"vehicle_no\":/g, "\"label\":");
      data = JSON.parse(data);
      $.each(data,function(key,value){
chauffeurname.push(value);
      });
  });

  $("#vehicle_no").autocomplete("option",{   //refresh autocomplete and update
    source:chauffeurname
  });

  }).focusout(function(){
      chauffeurname = [];
  });

});


//------------send booking sms for others----------------

      function getMsg(selector){
        return $(selector).attr('data-msg');
      }

function sendBookOther(bookingid) {

      $("#sendBookingOthers").validate({
        messages:{
         enterOther:getMsg("#enterOther")
        }
      });

        if($("#sendBookingOthers").valid()){
          $.ajax({            //send json-object to api and read response
              url: '/rapido/sendbookingsmsforothers/'+bookingid+"/",
              method: "POST",
              data: $("#sendBookingOthers").serialize(),
              success: function(res) {
                console.log(res);
                  swal({
                    title:"SMS sent successfully",
                    icon:"success"
                  }).then((will)=>{
                    if(will){
                      location.reload();
                    }
                  });
              }
          });
        }
}


//------------send trip sms for others----------------


  //called when key is pressed in textbox
  $("#enterOther,#enterOthers").keypress(function (e) {
     //if the letter is not digit then display error and don't type anything
     if (e.which != 8 && e.which != 0 && (e.which < 48 || e.which > 57)) {
        //display error message
        $("#errmsg").html("Numbers only").show().fadeOut("slow");
               return false;
    }
   });
      function getMsg(selector){
        return $(selector).attr('data-msg');
      }

function sendTripOther(bookingid) {

      $("#sendTripOthers").validate({
        messages:{
         enterOther:getMsg("#enterOther")
        }
      });

        if($("#sendTripOthers").valid()){
          $.ajax({            //send json-object to api and read response
              url: '/rapido/sendtripdetailsmsforothers/'+bookingid+"/",
              method: "POST",
              data: $("#sendTripOthers").serialize(),
              success: function(res) {
                console.log(res);
                  swal({
                    title:"SMS sent successfully",
                    icon:"success"
                  }).then((will)=>{
                    if(will){
                      location.reload();
                    }
                  });
              }
          });
        }
}


function sendOtherEmail(bookingid){

                swal({
                  title:"Want to send Email to Customer?",
                  icon:"warning",
                  buttons:["Cancel","Send"]
                }).then((willDelete) => {
                      if (willDelete) {
                        $('#loader').css("display","block");
                $.get('/rapido/sendcancelemail/'+bookingid+'/',function(data){
              if(data){
                        $('#loader').hide();
                swal({
                  title:"Email sent successfully",
                  icon:"success"
                }).then(function(){
                  window.location.reload();
                });
              }
                });
                      } else {
                        console.log("hello");
                      }
                    });
}


function sendOtherMessage(bookingid){

                swal({
                  title:"Want to send SMS to Customer?",
                  icon:"warning",
                  buttons:["Cancel","Send"]
                }).then((willDelete) => {
                      if (willDelete) {
                        $('#loader').css("display","block");
                $.get('/rapido/sendcancelsms/'+bookingid+'/',function(data){
              if(data){
                        $('#loader').hide();
                swal({
                  title:"Message sent successfully",
                  icon:"success"
                }).then(function(){
                  window.location.reload();
                });
              }
                });
                      } else {
                        console.log("hello");
                      }
                    });
}

//------------------send XL-------------

function uploadXL(vendorid) {

        if($("#uploadVehicleXL").valid()){
          $.ajax({            //send json-object to api and read response
              url: '/rapido/add_chauffeur_vehicel/'+vendorid+"/",
              method: "POST", 
              data: $("#uploadVehicleXL").serialize(),
              success: function(res) {
                console.log(res);
                  swal({
                    title:"file Upload successfully",
                    icon:"success"
                  }).then((will)=>{
                    if(will){
                      location.reload();
                    }
                  });
              }
          });
        }
}


//=========== Default date attaching for urls for filter Todays bookig histroy ===============

$(function(){
  var bookDate = new Date();
  bookDte = moment(bookDate).format('YYYY-MM-DD');
  $("#staffPendingBooking").attr("href","/rapido/staff_datewisebookings/"+bookDte+"/"+bookDte+"/")
  $("#staffPendingDispatch").attr("href","/rapido/staff_dutyslip_list/"+bookDte+"/"+bookDte+"/")
  $("#staffOnTrip").attr("href","/rapido/staff_ontrip_list/"+bookDte+"/"+bookDte+"/")
  $("#adminPendingBooking").attr("href","/rapido/admin_datewisebookings/"+bookDte+"/"+bookDte+"/")
  $("#adminPendingDispatch").attr("href","/rapido/admin_dutyslip_list/"+bookDte+"/"+bookDte+"/")
  $("#adminOnTrip").attr("href","/rapido/admin_ontrip_list/"+bookDte+"/"+bookDte+"/")
})