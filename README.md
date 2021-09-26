# password_encoder
## Method/Algorithm:
Instead of hiding passwords I encoded them using bas64 and a shift in them. 
That is : 
First in Password_encoder.py file we can see that we use that to add(in a specific format) and encode the password.
Here the encoding is done like this:
First I took the input 
for example: facebook:123456 is the input 
then the part after ":" gets taken into the encoding part and added at last of the code(saving in the file).
And the encoding involves : base64 encryption and then shifting the charecters to right by 5.
