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
		})
