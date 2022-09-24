#Welcome to Test_hackathon.py
import re
 #for checking Email
def emailChecker():

   match = re.compile(r"'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'") # Your Regex goes between the double quotes

   email = input("Enter the Email: ")

   if re.fullmatch(match, email):
       print (f"'{email}'looks like a valid Email")
   else:
       print ("Invalid Email")
#for checking Phone Number
def check_form(data):

   Pattern = re.compile("(0/91)?[6-9][0-9]{9}")

   Phone_Number=input("Enter your phone number:")

   if re.fullmatch(Pattern,Phone_Number):
       print(f"'{Phone_Number}'looks like a valid phone number")
   else:
       print("invalid phone number")
#for checking name
Full_name=input("Enter your Full name")
def check_form(data):
    if data['Full_name'].isdigit():
        print(f"'Full_name'looks invalid")

    else:
        print("full name is valid")

#for checking Username
