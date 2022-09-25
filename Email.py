#!/usr/bin/python3
import re
 #for checking Email
def emailChecker():

   match = re.compile(r"'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'") # Your Regex goes between the double quotes

   email = input("Enter the Email: ")

   if re.fullmatch(match, email):
       print (f"'{email}'looks like a valid Email")
   else:
       print ("Invalid Email")
