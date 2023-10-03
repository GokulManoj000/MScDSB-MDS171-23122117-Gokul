class stack:
    def __init__(self):
        self.lst=[]

    def push(self):
        item=input("\nEnter the item to add to the list:")
        self.lst.append(item)
        print("\nItem successfully added to the list")
        print(self.lst)
        return self.lst
    
    def pop(self):
        self.lst.pop()
        print("\nItem got deleted from the list")
        print(self.lst)

    def show(self):
        print("\nThe items in the stack are:")
        print(self.lst)

    def size(self):
        print("\nThe size of the stack is",len(self.lst))

    def topitem(self):
        print("\nThe top item in the stack is",self.lst[len(self.lst)-1])
    
    def stackempty(self):
        if len(self.lst)==0:
            print("Stack is empty")
        else:
            print("Stack is not empty")
stackfunction=stack()

a=True
while a==True:
    print("\n\nMenu driven program for Stack")
    print("1. Add element to the stack\n2. Remove element from the stack\n3. Print elements in the stack\n4. Print size of the stack \n5. Print the top item of the stack\n6. Check if stack is empty")
    choice=int(input("\n\nEnter your choice:"))
    if choice==1:
        stackfunction.push()
    elif choice==2:
        stackfunction.pop()
    elif choice==3:
        stackfunction.show()
    elif choice==4:
        stackfunction.size()
    elif choice==5:
        stackfunction.topitem()
    elif choice==6:
        stackfunction.stackempty()
    else:
        a=False

