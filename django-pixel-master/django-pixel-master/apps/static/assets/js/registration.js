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
         $('input[type=date]').removeAttr('readonly');
         $('input[type=select]').removeAttr('readonly');
         $('input[type=email]').removeAttr('readonly');
         $("#editButton").css("display","none");
         $("#updateButton").css("display","");

    })

})
