# create a class restaurant, that accepts item and qty as inputs
# inside your class you are having the item and its cost (unit price) as a dictionary
# create a function calculate totalcost that prints the itemname, qty and totalcost

class restaurant:
    def __init__(self,item,qty):
        self.Item=item
        self.Quantity=qty
        self.menu={"Rice":40,"Chicken":100,"Paneer":60,"Roti":15}

    def totalcost(self):
        print("Total cost of the order:")
        print("Item:\t",self.Item)
        print("Quantity:\t",self.Quantity)
        global total
        total=self.Quantity*self.menu[self.Item]
        print("Total:\t",total)

toootal=0
n=int(input("Enter number of items:"))
for i in range(n):
    item=input("Enter item")
    qty=int(input("Enter quantity"))
    order=restaurant(item,qty)
    order.totalcost()
    toootal=toootal+total
    print("Total price:",toootal)


