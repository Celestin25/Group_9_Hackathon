#!/usr/bin/python3
#for checking name
First,Middle,Last=input("Enter your Full name of First,Middle and Last")
print("First name :",First)
print("Middle name:",Middle)
print("Last name:",Last)
def check_form(data):
    if data['Full_name'].isdigit():
        print(f"'Full_name'looks invalid")

    else:
        print("full name is valid")
