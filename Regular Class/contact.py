#develop a contact managment program where isers can add,edit,delete and search 
# new contact details using a dictionary.the menue options would facilitate these actions.

class contact:
    def __init__(self):
        self.details={}

    def adddetails(self,phone,name,place,age):
        temp={"Name":name,"Place":place,"Age":age}
        self.details[phone]=temp
        print(self.details)

    def searchnum(self,search):
        for num in self.details.keys():
            if search==num:
                print(self.details[searchnum])
    
    def updatecontact(self,search):
        for num in self.details.keys():
            if search==num:
                print(self.details[searchnum])
                update=input("Enter the detail to update:").title()
                if update=="Name":
                    new=input("Enter new details:")
                    self.details[searchnum][update]=new
                if update=="Place":
                    new=input("Enter new details:")
                    self.details[searchnum][update]=new
                if update=="Age":   
                    new=int(input("Enter new details:"))
                    self.details[searchnum][update]=new
                print(self.details[searchnum])
condet=contact()
while True:
    print("Contact Management")
    print("1. Add details\n2. Search contact\n3. Update Contact\n4.Delete contact\n5. Exit Menu")
    choice=int(input("Enter your choice:"))
    if choice==1:
        phone=input("Enter the phone number:")
        name=input("Enter the name:")
        place=input("ENter the place:")
        age=int(input("Enter the age:"))
        condet.adddetails(phone,name,place,age)
    
    elif choice==2:
        search=input("Enter number to be seached:")
        condet.searchnum(search)

    elif choice==3:
        searchnum=input("Enter number to be seached:")
        condet.updatecontact(searchnum)

    elif choice==4:
        print("hello")
    
    elif choice==5:
        exit()
    
    else:
        print("Wrong choice")
    

