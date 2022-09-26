#!/usr/bin/python3
import re
email = input("Enter the Email: ")
def emailChecker():
   match = re.compile(r"'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'") # Your Regex goes between the double quotes

   if re.fullmatch(match, email):
       print (f"'{email}'looks like a valid Email")
   else:
       print ("Invalid Email")
       
#for checking for password
import re
Password=input("Enter your password:")
if not re.match("^(?!.*[a-z].*[a-z].*[a-z].*)(?!.*\d.*\d.*\d.*)(?!.*[!@#$%^&*()~].*[!@#$%^&*()~].*[!@#$%^&*()~].*)(?!.*[A-Z].*[A-Z].*[A-Z].*).{8,8}$", Password):
    print(f"'password'looks a invalid password")
      
else:
    print("password is valid")
#for checking name
First,Middle,Last=input("Enter your Full name of First,Middle and Last:").split()
print("First name :",First)
print("Middle name:",Middle)
print("Last name:",Last)
def check_form(data):
    if data['Full_name'].isdigit():
        print(f"'Full_name'looks invalid")

    else:
        print("full name is valid")
