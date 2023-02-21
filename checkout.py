import csv
import time
import subprocess
R=100000000
t=0
while R >= t:
    class checkout():
        def __init__(self):
            self.cart = []
            self.tax = 1.09

        def add_item(self, item):
            self.cart.append(item)

        def checkout(self):
            total = 0
            for item in self.cart:
                total += int(item[2])
            total_tax = total * self.tax
            print("Total before tax: ${:.2f}".format(total))
            print("Total with tax: ${:.2f}".format(total_tax))
        
        
        
            while True:
                print("Please choose a form of payment.")
                payment_method = input("Cash or credit? ")
                if payment_method == "credit":
                    scan = input("Please insert your card into the scanner. ")
                    break
                elif payment_method == "cash":
                    print("Please give your cash to the cashier.")
                    cash_amount = float(input("Enter cash amount: $"))
                    if cash_amount >= total_tax:
                        change = cash_amount - total_tax
                        print("Your change is: ${:.2f}".format(change))
                    else:
                        print("The amount is not enough. Please add more cash.")
                    break

    def read_csv():
        items = []
        with open("food.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                items.append(row)
        return items

    def add_to_cart(shopping_cart, items):
        while True:
            item = input("Please scan the barcode or type 'c' or 'checkout' when finished: ")
            if item == "c" or item == "checkout":
                break
            for i in items:
                if i[1] == item:
                    shopping_cart.add_item(i)
                    print("{} has been added to the cart.".format(i[0]))
                    break
        shopping_cart.checkout()
        restart = input("Would you like to start a new transaction? (yes/no): ")
        if restart.lower() == "no" or restart.lower() == "n":
            print("Goodbye.")
            subprocess.run(["python", "login.py"],bufsize=0)
        elif restart.lower() == "yes" or restart.lower() == "y":
            print("new transaction:")
        elif restart.lower() == "main" or restart.lower() == "exit":
            subprocess.run(["python", "main.py"], bufsize=0)
            pass
           
 
        
    shopping_cart = checkout()
    items = read_csv()
    add_to_cart(shopping_cart, items)
t += 1 
print(t)
