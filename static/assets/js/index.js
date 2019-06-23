document.addEventListener('DOMContentLoaded', function() {
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
          document.getElementById('profile').style.visibility = "visible";
          document.getElementById('signOut').style.visibility = "hvisible";
          document.getElementById('signUp').style.visibility = "hidden";
          }
          else {
            console.log('bad');
            document.getElementById('profile').style.visibility = "hidden";
            document.getElementById('signOut').style.visibility = "hidden";
            document.getElementById('signUp').style.visibility = "visible";
          }
        });
      }
      else {
        console.log('bad');
        document.getElementById('profile').style.visibility = "hidden";
        document.getElementById('signOut').style.visibility = "hidden";
        document.getElementById('signUp').style.visibility = "visible";
      }
}, false);
