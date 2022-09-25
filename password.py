#!/usr/bin/python3
#for checking for password
import re
Password=input("Enter your password:")
if not re.match("^(?!.*[a-z].*[a-z].*[a-z].*)(?!.*\d.*\d.*\d.*)(?!.*[!@#$%^&*()~].*[!@#$%^&*()~].*[!@#$%^&*()~].*)(?!.*[A-Z].*[A-Z].*[A-Z].*).{8,8}$", password)::
        print(f"'password'looks a invalid password")
      
    else:
        print("password is valid")
