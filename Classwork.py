def calculate_tax(amount):
    return amount * 0.19

def calculate_discount(amount):
    return 2000

def calculate_total(subtotal, tax, discount):
    return subtotal + tax - discount

def print_receipt(subtotal):
    tax = calculate_tax(subtotal)
    discount = calculate_discount(subtotal)
    total = calculate_total(subtotal, tax, discount)
    
    print("Subtotal: ", subtotal)
    print("Tax:      ", tax)
    print("Discount: ", discount)
    print("Total:    ", total)
mytotalamount = float(input(f"Enter your total ammount{print_receipt}"))
#print_receipt(70000)
print(mytotalamount)