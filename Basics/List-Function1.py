Students ={
    "Ali" : {"Maths" : 90 , "Physics" : 75 , "Chemistry" : 80},
"Sarmad" : {"Maths" : 80 , "Physics" : 95 , "Chemistry" : 70},
"Basit" : {"Maths" : 70 , "Physics" : 85 , "Chemistry" : 75},
"Uzair" : {"Maths" : 60 , "Physics" : 75 , "Chemistry" : 78},
"Shahroz" : {"Maths" : 50 , "Physics" : 65 , "Chemistry" : 82}
}
subjects = ["Maths" , "Physics" , "Chemistry"]
for subject in subjects:
    markslist=[]
    for Student in Students:
        markslist.append(Students[Student][subject])
    average = sum(markslist)/len(markslist)
    print(average)
print (" highest Marks ")
for subject in subjects:
    highest_marks = 0
    for Student in Students:
        marks = Students[Student][subject]
        if  marks> highest_marks:
            highest_marks = marks
    print (highest_marks)

SaveMart = {
    "Lays": {"Price": 50, "Quantity": 10},
    "Choclates": {"Price": 30, "Quantity": 20},
    "Icecream": {"Price": 100, "Quantity": 30},
}

total_bill = 0

print("       SaveMart Menu      ")
print("1. Lays - Rs.50")
print("2. Choclates - Rs.30")
print("3. Icecream - Rs.100")
print("4. Done (checkout)")
print

while True:
    choice = input("Which Item You want to choose ? Enter Number: ")
    match choice:
        case "1":
            item_name = "Lays"
        case "2":
            item_name = "Choclates"
        case "3":
            item_name = "Icecream"
        case "4":
            break
        case _:
            print("Invalid choice.\n")
            continue

    Item_Quantity = int(input("How much Quantity {item_name} You want ? "))

    if  Item_Quantity <= 0:
        print("Quantity should be greater than zero.")
        continue

    if  Item_Quantity > SaveMart[item_name]["Quantity"]:
        print(f"This Quantity is not Available: {SaveMart[item_name]['Quantity']}\n")
        continue

    item_cost = SaveMart[item_name]["Price"] * Item_Quantity
    total_bill += item_cost
    SaveMart[item_name]["Quantity"] -= Item_Quantity

    print(f"{Item_Quantity} x {item_name} added. Cost: {item_cost}\n")

if total_bill > 0:
    payment_method = input("Payment method (card/cash)? ")
    match payment_method:
        case "card":
            tax = total_bill * 0.08
        case "cash":
            tax = total_bill * 0.18
        case _:
            print("Invalid payment method")
            tax = 0

    final_bill = total_bill + tax

    print("Subtotal:", total_bill)
    print(f"Tax ({payment_method}):")
    print(f"Final Total (with tax):", final_bill)
else:
    print("No Item is Selected.")
print(SaveMart)




