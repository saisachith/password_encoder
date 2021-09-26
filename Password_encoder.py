import base64

def Password_encoder(s):
    # here lets first encode it with base64 and then shift by 5.
    s_ascii = s.encode("ascii")
    s_b64 = str(base64.b64encode(s_ascii,altchars=None))[2:-1]
    # now lets shift it by 5
    s_new = ''
    for i in range(len(s_b64)):
        if i+5 >= len(s_b64):
            s_new+=s_b64[i+5-len(s_b64)]
        else:
            s_new += s_b64[i+5]
    return s_new


#driver code
# this is a encoding file so this need to take input and encode it and save it in the location.

line = str(input("Enter the password with the site in this form (facebook:123456):"))
location = "F:\Passwords\Passwords.txt"
file = open(location,'a+')
info = file.read()
if len(info) > 0:
    file.write("\n")
for i in range(len(line)):
    if line[i] == ":":
        new_line = line[:i+1] + str(Password_encoder(line[i+1:]))

file.write(new_line+'\n')
file.close()