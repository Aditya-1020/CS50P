def main():
    total_amount = 0
    print("Amount Due: 50")

    while total_amount < 50:
        coin = int(input("Insert coin: "))
    
        if coin == 25 or coin == 10 or coin == 5:
            total_amount += coin
        else:
            print("Invalid Value")
        
        if total_amount < 50:
            amount_due = 50 - total_amount
            print("Amount Due:", amount_due)
    
    change = total_amount - 50
    print("Change Owed:", change)

if __name__ == "__main__":
    main()
