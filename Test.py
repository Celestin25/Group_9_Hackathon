def DOB_checker():
    """ Check if date of birth is valid """
    match = re.compile(r"^(0?[1-9]|[12][0-9]|3[01])[\/._-](0?[1-9]|1[012])[\/._-]\d{4}$")  # Your Regex goes between the double quotes
    DOB = input("Enter the date of birth: ")

    if re.fullmatch(match, DOB):
        print(f"'{DOB}'looks like a valid date of birth")
    else:
        print("Invalid date of birth")


def phone_numChecker():
    match = re.compile(r"\+([0-9]){3}[\s|-]([0-9]){3}[\s|-]([0-9]){3}[\s|-]([0-9]){2,4}")
    phone_num = input("Enter your phone number (Eg: +27xxx): ")

    if re.fullmatch(match, phone_num):
        print(f"'{phone_num}'looks like a valid phone number")
    else:
        print("Invalid phone number!")
