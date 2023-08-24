def shorten(word):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    return ''.join(char for char in word if char.lower() not in vowels and not char.isdigit())
def main():
    text = input("Enter some text: ")
    shortened_text = shorten(text)
    print("Output:", shortened_text)
    
if __name__ == "__main__":
    main()
    