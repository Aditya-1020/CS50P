def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything?\n") # added line break to make it more visualy appealing

    if answer == "42":
        print("Yes")
    elif answer == "Forty Two" or answer == "forty-two":
        print("Yes")

    else:
        print("No")

main()