function formValidation()
{
var uname = document.registration.firstName;
var ulname = document.registration.lastName;
var uadd = document.registration.address;
var ucity = document.registration.city;
var ustate = document.registration.state;
var uzip = document.registration.zipcode;
var uemail = document.registration.email;

if(allLetter(uname))
{
if(allLetterl(ulname))
{
if(alphanumeric(uadd))
{ 
if(allnumeric(uzip))
{
if(ValidateEmail(uemail))
}
} 
} 
}
return false;
}
    
function allLetter(uname)
{ 
var letters = /^[A-Za-z]+$/;
if(uname.value.match(letters))
{
return true;
}
else
{
alert('First name must have alphabet characters only');
uname.focus();
return false;
}
}
    
function allLetterl(ulname)
{ 
var letters = /^[A-Za-z]+$/;
if(ulname.value.match(letters))
{
return true;
}
else
{
alert('Last name must have alphabet characters only');
ulname.focus();
return false;
}
}

function alphanumeric(uadd)
{ 
var letters = /^[0-9a-zA-Z]+$/;
if(uadd.value.match(letters))
{
return true;
}
else
{
alert('Address must have alphanumeric characters only');
uadd.focus();
return false;
}
}
    
function allnumeric(uzip)
{ 
var numbers = /^[0-9]+$/;
if(uzip.value.match(numbers))
{
return true;
}
else
{
alert('ZIP code must have numeric characters only');
uzip.focus();
return false;
}
}
    
function ValidateEmail(uemail)
{
var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
if(uemail.value.match(mailformat))
{
return true;
}
else
{
alert("You have entered an invalid email address!");
uemail.focus();
return false;
}
}


