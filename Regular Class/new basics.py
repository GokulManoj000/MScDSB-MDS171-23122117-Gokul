class petStore():
    def __init__(self):
        self.pets={"Dogs":[],"Cat":[],"Rabbit":[],"Parrot":[]}

    def storepet(self):
        petlist={}
        species=input("Enter the type of pet:").title()
        breed=input("Enter the breed:")
        age=input("Enter the age:")
        price=int(input("Enter the amount:"))
        petlist["Breed"]=breed
        petlist["Age"]=age
        petlist["Price"]=price

        for i in self.pets.keys():
            flag=True
            if i==species:
                self.pets[species].append(petlist)
                break
            else:
                flag=False
        if flag==False:
            print("\nSelected pet is not available right now")
        print(self.pets)

    def searchpet(self):
        search=input("Enter type of pet to be searched:").title()
        for key in self.pets.keys():
            flag=True
            if search==key:
                print(self.pets[key])
                breed=input("Enter the breed to be searched:")
                for i in self.pets[key]:
                    for j in i.keys():
                        if breed==i[j]:
                            print("The available pet with given inputs:",i)
                            break
                break
            else:
                flag=False
        if flag==False:
            print("Searched pet no found")

p=petStore()
a=True
while a==True:
    print("1. Store Details\n2. Search pet\n3. Sell a pet\n4. List all the pets\n5. Exit the menu")
    choice=int(input("Enter the choice:"))
    if(choice==1):
        p.storepet()
    elif(choice==2):
        p.searchpet()
    # elif(choice==3):

    # elif(choice==4):
        
    elif(choice==5):
        a=False    
    else:
        print("Wrong Choice")
p.storepet()