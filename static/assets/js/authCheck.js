var poolData = {
    UserPoolId : 'us-east-2_yFw2iwBrX', // Your user pool id here
    ClientId : '6522p2hv13jb7hilc9k4pa9s8g' // Your client id here
};
var userPool = new AmazonCognitoIdentity.CognitoUserPool(poolData);
var cognitoUser = userPool.getCurrentUser();
if (cognitoUser != null) {
  window.location.href = "index.html";
}
