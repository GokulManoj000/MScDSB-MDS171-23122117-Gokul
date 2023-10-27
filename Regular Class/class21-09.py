# class MSCDSB:
#     def __init__(self):
#         # Data members / Properties / Attributes
#         self.name="MSC DS B"
#         self.students=["A","B","C"]

#     def printstudents(self):
#         for student in self.students:
#             print(student)


# obj=MSCDSB()
# print(obj.name,obj.students)
# obj.printstudents()





class car:
    def __init__(self,mfg,mdl,yr):
        self.Manufacturer=mfg
        self.Model=mdl
        self.Year=yr

    def __str__(self):
        return self.Manufacturer


bmw=car("BMW","F Series",2020)
print(bmw.Manufacturer)

ferrari=car("Ferrari","A series",2023)
print(ferrari.Model)

manufacturer=input("Enter the manufacturer:")
model=input("Enter the model:")
year=int(input("Enter the year:"))
audi=car(manufacturer,model,year)
print(audi.Manufacturer,audi.Model,audi.Year)



