def main():
    camel_Case = input("camelCase: ")

    def snake_case(name):
        modified_name = ""
        for char in name:
            if char.isupper():
                modified_name += "_" + char.lower()
            else:
                modified_name += char
        if modified_name.startswith("_"):
            modified_name = modified_name[1:]
        return modified_name

    snake_case_name = snake_case(camel_Case)
    print("snake_case:", snake_case_name)
    
if __name__ == "__main__":
    main()
