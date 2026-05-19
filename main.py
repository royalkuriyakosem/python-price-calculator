def calculate_total(price, quantity, percentTax=0):
    total = price * quantity 
    total+=total*(percentTax/100)
    return total


def main():
    price = 100
    quantity = 2
    percentTax = 10

    total = calculate_total(price, quantity, percentTax)

    print(f"Total amount: {total}")


main()