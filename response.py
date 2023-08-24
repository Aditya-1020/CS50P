from validator_collection import validators

def main():
    email_address = input("What's your email? ").strip()
    try:
        email_isvalid = validators.email(email_address)
        print("Valid")
    except:
        print("Invalid")

if __name__ == "__main__":
    main()