$(document).on("submit",'form',function(e){
    e.preventDefault();
    
    email = $('#emailInput').val();
    username = $('#userInput').val();
    password = $('#passwordInput').val();

    if (email == "" || username == "" || password== ""){
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: "Register Failed",
          })
    }

    // create a ajax
    $.ajax({
        url:"/validation",
        type:"POST",
        data:{
            email: email,
            username : username,
            password :password
        },
        success:function(data){
            if(data["message"]){
                Swal.fire({
                    position: 'center',
                    icon: 'success',
                    title: 'Register Successfully',
                    showConfirmButton: false,
                    timer: 1500
                  })
            }
            else{
                Swal.fire({
                    icon: 'error',
                    title: 'Oops...',
                    text: "Register Failed",
                  })
            }
        }
    })
})