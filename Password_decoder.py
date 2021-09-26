import base64

li = []
location = "F:\Passwords\Passwords.txt"
file = open(location,'r')
li = (file.read().split("\n"))
# print(li)
# print(len(li))
file.close()

def Password_decoder(s):
    # in encoder we first base64 ed it and then shifted by 5
    # now we need to do reverse i.e. shift it by len(s)-5 and then base64 decode it.
    s_shift = ''
    # print("s:"+s)
    k = (s.index(s[-1]) + 1) - 5
    if k > 0:
        pass
    else:
        k = k*(-1) # just in case if password is less than 5 letters (as it wont be so strong this case is very rarely used.)
    for i in range(len(s)):
        if i+k >= len(s):
            s_shift += s[i+k - len(s)]
        else:
            s_shift += s[i+k]
    s_decoded = base64.b64decode(s_shift,altchars=None, validate=False)
    return str(s_decoded)[2:-1]


# driver code

def key_passed(li):
    for i in range(len(li)-1):
        if li[i] == ' ':
            break
        else:
            print(str(i + 1) + '. ' + str(li[i][:li[i].index(":")]))

    n = int(input("What are you looking for : "))

    def encrypted_password(s):
        for i in range(len(s)):
            if s[i] == ":":
                return s[i + 1:]

    p = str(encrypted_password(li[n-1]))
    # print(p)
    # print(len(p))
    print("Password of "+str(li[n-1][0:li[n-1].index(":")]) + "is : "+ str(Password_decoder(p))) # answer.



# just a password to keep others from accessing the passwords folder.

key = str(input("Please enter the key to unlock the Password decrypter:"))

if len(key) == 15:
    if (key[8]) == '4' and (key[9]) == '5' and (key[10]) == '5' and (key[12]) == '0':
        status = 1
    else:
        status = 0
    if status == 1 and hex(ord(key[2])) == '0x6c' and ord(key[6]) == 95 and key[-1] == 'D' and key[5] == 'k':
        status = 1
    else:
        status = 0
    if status == 1 and chr(ord(key[4]) - 4) == '_' and ord(key[3]) == 111 and key[key.index("D") - 1] == "R":
        status = 1
    else:
        status = 0
    if status == 1 and key[key.index("4") - 1] == "P" and key[key.index("k") + key.index("_")] == "W" and key[0] == chr(int(0x75)) and key[key.index(chr(int(0x75))) + 1] == "n":
        status = 1
    else:
        status = 0
else:
    status = 0
if status == 0:
    print("Sorry you have no access.")
    print("please contact the admin for using the decryption file")
else:
    key_passed(li)


