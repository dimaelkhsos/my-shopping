$("#login").submit(function(e) {
    e.preventDefault();
    var authenticationData = {
        Username : document.getElementById('login-email').value,
        Password : document.getElementById('login-password').value,
    };
    var authenticationDetails = new AmazonCognitoIdentity.AuthenticationDetails(authenticationData);
    var poolData = {
        UserPoolId : 'us-east-2_yFw2iwBrX', // Your user pool id here
        ClientId : '6522p2hv13jb7hilc9k4pa9s8g' // Your client id here
    }
    var userPool = new AmazonCognitoIdentity.CognitoUserPool(poolData);
    var userData = {
        Username : document.getElementById('login-email').value,
        Pool : userPool
    };
    var cognitoUser = new AmazonCognitoIdentity.CognitoUser(userData);
    cognitoUser.authenticateUser(authenticationDetails, {
        onSuccess: function (result) {
            var accessToken = result.getAccessToken().getJwtToken();

            /* Use the idToken for Logins Map when Federating User Pools with identity pools or when passing through an Authorization Header to an API Gateway Authorizer*/
            var idToken = result.idToken.jwtToken;
            localStorage.setItem('myToken', accessToken);
            window.location.href = "profile.html";
        },

        onFailure: function(err) {
            console.log(err);
        },

    });
});
