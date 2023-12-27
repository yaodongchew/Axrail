#Defining a class for vending machine
class vendingMachine:
    def __init__(self):
        self.item = {
            'coke': 2,
            'sprite': 3,
            'orange juice': 5,
            'beer': 15,
            'wine': 20
        }
    
    #Retrieve customer order
    def get_order(self, item, amount):
        item = item.lower()
        if item in self.item:
            price = self.item[item]
            total_price = price * int(amount)
            print(f'Total amount is {total_price}. Please pay by cash notes!')
            return total_price
        else:
            print('Invalid item!')
            return 0
    
    #Calculating changes
    def change_money(self, note_amount, total_price):
        if int(note_amount) < total_price:
            return "Insufficient amount! Please Insert More Notes!"
        
        change = int(note_amount) - total_price

        note = [100, 50, 20, 10, 5, 1]
        note_amount={}
        if change == 0:
            return "Thank You! Have a nice day!^_^"
        else:
            for amount in note:
                count = int(change // amount)
                if count > 0:
                    note_amount[amount] = count
                    change-= count * amount

        return note_amount

#Create Vending Machine
vending_Machine = vendingMachine()

#Order
item = input('Enter item to purchase: ')
quantity = input('Enter quantity: ')
totalpayment = int(vending_Machine.get_order(item, quantity))

#Payment
payment = input("Enter the amount of note inserted into the machine: ")
change_given = vending_Machine.change_money(payment, totalpayment)
print('Changes to be given: ')
if isinstance(change_given, str):
    print(change_given)
else:
    for note, num in change_given.items():
        print(f"RM {note} notes: {num}")
print("Thank You! Have a nice day!^_^")


