import csv

def addItems():
    print("Hello user. Please select your preferred product input. (normal or weighted)")
    print("Normal for a product with a set price per item.")
    print("Weighted for a product that is priced per pound (lb).")
    userinput = input("Normal or Weighted: ").lower()
    Input1 = None
    while Input1 is None: 
        if userinput == "normal": 
            print("Please enter the name, code, and price of the product.")
            Input1 = input().split(',')
        elif userinput == "weighted":
            print("Please enter the name, code, price, and weight of the product.")
            Input1 = input().split(',')
        else:
            print("Invalid input. Please enter either 'normal' or 'weighted'.")
            userinput = input("Normal or Weighted: ").lower()
    item = Input1
    
    with open("food.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(item)

addItems()
