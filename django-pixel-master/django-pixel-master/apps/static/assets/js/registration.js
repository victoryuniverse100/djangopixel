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

})
