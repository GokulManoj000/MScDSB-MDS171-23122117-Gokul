#define a class expense tracker that stores the expenses and income in a dictionary
#implement the method to
# - store the transaction
# - view transactions
# - calculate the total expense/income

class expensetracker:
    def __init__(self):
       self.amt=amt
       self.exp_type=exp_type
       self.tracker={"Expense":{"Food":15000,"Rent":25000,"Transport":3000}, "Income":{"Salary":50000,"Production":20000,"Rent":5000}}

    def expensestore(self):
        self.tracker["Expense"][exp_type]=amt
        print(self.tracker)
    def incomestore(self):
        self.tracker["Income"][exp_type]=amt
        print(self.tracker)
type=int(input("Enter 1 for Expense or 2 for Income:"))
if type==1:
    exp_type=input("Enter expense type:")
    amt=int(input("Expense amount:"))
    order=expensetracker()
    order.expensestore()
elif type==2:
    exp_type=input("Enter income type:")
    amt=int(input("Income amount:"))
    order=expensetracker()
    order.incomestore()




    

