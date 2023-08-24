def main():
    camel_Case = input("camelCase: ")
    print(camel_Case)
    
    def snake_case(name):
        modified = name.replace(" ", "_")
        return modified
    
    snake_case_name = snake_case(camel_Case)
    
    print("snake_case:", snake_case_name)
    
if __name__ == "__main__":
    main()
    