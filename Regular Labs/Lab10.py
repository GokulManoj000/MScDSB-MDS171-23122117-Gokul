class student:
    def __init__(self):
        self.stud={}

    def addstud(self,name,regno,phone,place):
        self.stud[regno]={"Name":name,"Phone":phone,"Place":place}

    def addmark(self,regno,sub,mark):
        self.stud[regno]["Marks"][sub]=mark

    def updatemark(self,regno,sub,mark):
        for i in self.stud.keys():
            if i==regno:
                for j in self.stud[regno]["Marks"].keys():
                    if j==sub:
                        self.stud[regno]["Marks"][sub]=mark

    def searchstud(self,search):
        for i in self.stud.keys():
            if i==search:
                print(self.stud[search])

clg=student()
while True:
    print("\n\nWho is the user?\n1. Student \n2. Teacher")
    user=int(input("Enter the user number:"))
    if user==1:
        print("1. Add Student detail\n2. Search detail")
        choice=int(input("Enter choice:"))
        if choice==1:
            reg=int(input("Enter register number:"))
            name=input("Enter name:")
            phone=input("Enter phone number:")
            place=input("Enter place:")
            clg.addstud(name,reg,phone,place)

        elif choice==2:
            search=int(input("Enter register no to be searched:"))
            clg.searchstud(search)
        
        else:
            exit()
    
    elif user==2:
        print("1. Add mark\n2. Update mark\n3. Search details")
        choice=int(input("Enter choice:"))
        if choice==1:
            regno=int(input("Enter the register number:"))
            for i in range(5):
                sub=input("Enter the subect:")
                mark=int(input("ENter the mark:"))
                clg.addmark(regno,sub,mark)
            
        elif choice==2:
            regno=int(input("Enter the register number:"))
            sub=input("Enter the subect:")
            mark=int(input("Enter the mark:"))
            clg.updatemark(regno,sub,mark)
        
        elif choice==3:
            search=int(input("ENter regno:"))
            clg.searchstud(search)
        
        else:
            exit()
    
    else:
        exit()
        
