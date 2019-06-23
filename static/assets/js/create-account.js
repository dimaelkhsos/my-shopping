var poolData = {
    UserPoolId : 'us-east-2_yFw2iwBrX', // Your user pool id here
    ClientId : '6522p2hv13jb7hilc9k4pa9s8g' // Your client id here
};
var userPool = new AmazonCognitoIdentity.CognitoUserPool(poolData);
var cognitoUser = userPool.getCurrentUser();
if (cognitoUser != null) {
  window.stop();
  window.location.href = "index.html";
}

var password = document.getElementById("password");
var confirmPassword = document.getElementById("confirmPassword");

function validatePassword(){
  if(password.value != confirmPassword.value) {
    confirmPassword.setCustomValidity("Passwords Don't Match");
  } else {
    confirmPassword.setCustomValidity('');
  }
}

password.onchange = validatePassword;
confirmPassword.onkeyup = validatePassword;

$("#register").submit(function(e){
    e.preventDefault();

    var attributeList = [];

    var dataEmail = {
        Name : 'email',
        Value : document.getElementById('email').value
    };

    var dataPhoneNumber = {
        Name : 'phone_number',
        Value : '+17722241555'
    };
    var dataFirstName = {
        Name : 'custom:firstName',
        Value : document.getElementById('firstName').value
    };
    var dataLastName = {
        Name : 'custom:lastName',
        Value : document.getElementById('lastName').value
    };
    var attributeEmail = new AmazonCognitoIdentity.CognitoUserAttribute(dataEmail);
    var attributePhoneNumber = new AmazonCognitoIdentity.CognitoUserAttribute(dataPhoneNumber);
    var attributeFirstName = new AmazonCognitoIdentity.CognitoUserAttribute(dataFirstName);
    var attributeLastName = new AmazonCognitoIdentity.CognitoUserAttribute(dataLastName);

    attributeList.push(attributeEmail);
    attributeList.push(attributePhoneNumber);
    attributeList.push(attributeFirstName);
    attributeList.push(attributeLastName);

    userPool.signUp(document.getElementById('email').value, document.getElementById('password').value, attributeList, null, function(err, result){
        if (err) {
            alert(err.message || JSON.stringify(err));
            return;
        }
        cognitoUser = result.user;
    });
});
