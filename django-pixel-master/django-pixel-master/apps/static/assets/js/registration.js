$(document).ready(function(){
			$("#customerForm").submit(function(e){
			console.log(e)
				e.preventDefault();
				var serializedData = $(this).serialize();
				$.ajax({
					type : 'POST',
					url :  "{% url 'customerFormData' %}",
					data : serializedData,
					success : function(response){

						 $('#customerForm').html(response);
						console.log(response);
					},
					error : function(response){
						console.log(response)
					}
				})
			})


	$("#editButton").click(function() {
         $('input[type=text]').removeAttr('readonly');
         $('#dob').prop('readonly', false);
         $('input[type=select]').removeAttr('readonly');
         $('#email_id').prop('readonly', false);
         $("#editButton").css("display","none");
         $("#updateButton").css("display","");

    })


    $("#editSeminar").click(function() {
         $('#payirchi-id').prop('readonly', false);
         $('#payirchi-name').prop('readonly', false);
         $('#first-payment').prop('readonly', false);
         $('#first-payment-date').prop('readonly', false);
         $('#second-payment').prop('readonly', false);
         $('#second-payment-date').prop('readonly', false);
         $('#third-payment').prop('readonly', false);
         $('#third-payment-date').prop('readonly', false);
         $('#fourth-payment').prop('readonly', false);
         $('#fourth-payment-date').prop('readonly', false);
         $('#introducer').prop('readonly', false);
         $('#teamleader').prop('readonly', false);
         $('#assistantleader').prop('readonly', false);
         $('#leader').prop('readonly', false);
         $("#editSeminar").css("display","none");
         $("#updateSeminar").css("display","");

    })

})



