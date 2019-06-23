var poolData = {
    UserPoolId : 'us-east-2_yFw2iwBrX', // Your user pool id here
    ClientId : '6522p2hv13jb7hilc9k4pa9s8g' // Your client id here
};
var userPool = new AmazonCognitoIdentity.CognitoUserPool(poolData);
var cognitoUser = userPool.getCurrentUser();

if (cognitoUser != null) {
  cognitoUser.getSession(function(err, session) {
    if (session.isValid()) {
      console.log('good');
      cognitoUser.getUserAttributes(function(err, result) {
        if (err) {
          console.log(err);
        }
        for (i = 0; i < result.length; i++) {
          if (result[i].getName() === 'custom:firstName') {
            document.getElementById('firstName').innerHTML = result[i].getValue();
          }
        }
      });
    }
    else {
      console.log('bad');
      window.location.href = "index.html";
    }
  });
}
else {
  console.log('bad');
  window.location.href = "index.html";
}
