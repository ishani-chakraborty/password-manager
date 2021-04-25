#password manager
import string
import random
 
#print(string.ascii_letters)

def store_password()
    #username
    username = str(input('Enter your unique username: '))
    #website
    website = str(input('Website: '))
    #generated random encrypted(hashable) password
    password = ''
    digit = int(input("Enter the number of digits you want in your password(integers only please) "))
    for i in range(digit):
        char = random.choice(string.ascii_letters)
        password += char
    # #hash the password
    # salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    # pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
    # pwdhash = binascii.hexlify(pwdhash)
    # return (salt + pwdhash).decode('ascii')

    #store the password into a file
    f = open('password.txt', 'a')
    f.write(f"{username}-{website}-{str(password)}\n")
    f.close()

    print(f"Here's your password: {password}")
 
 ###########################################################

def search():
    username_or_website = str(input('Do you want to search for username or website? '))
    value = str(input("What value? "))
    f = open('password.txt', 'r')
    for line in f
        info = line.split('-')
        if username_or_website == 'username':
           if value == info[0]:
                return info[2]
        #search by username
        else: 
        #search by website
        if value == info[1]:
            return info[2]
        
#store_password()
result = search()

if result == None:
    print("No result found")
else:
    print(f"Here's your password: {result}")

"""
Generate Salt: random bits (0,1) added to each password instance before
its hashing  
"""
