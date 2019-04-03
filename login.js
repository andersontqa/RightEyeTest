var login_attempts = 3;

function validateForm(){
  var email = document.forms["myform"]["email"].value;
  var password = document.forms["myform"]["password"].value;
  if (email == "coding@project.com" && password == "Coding@123"){
    alert("Login Successful");
    return false;
  } if(email != "coding@project.com"){
    alert("Wrong email address.");
  }
  if (password != "Coding@123"){
    if(login_attempts >= 2){
      alert("Email address and password do not match.");
      login_attempts--;
      return false;
    }
    if(login_attempts == 1){
      alert("You only have one more chance.\nPlease contact RightEye Support at 800-301-0803.");
      login_attempts--;
      return false;
    }
    if(login_attempts == 0){
      alert("Your email address is locked and invalid.\nPlease contact RightEye Support at 800-301-0803");
      return false;
    }

  }
  return false;

}
