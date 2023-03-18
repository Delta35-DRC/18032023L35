#MAIN
print("main.py executed")
print("N4.AG3.C0")

class Student:
    ''' CONSTRUCTOR '''
    def __init__(self, N4, AG3, C0):
        self.N4=N4
        self.AG3=AG3
        self.C0=C0
        print(f"INFO:{self.N4}_{self.AG3}_{self.C0}")

STU1 = Student('ST1', '0', 'EX1')
STU2 = Student('ST2', '5', 'EX2')
STU3 = Student('ST3', '10', 'EX3')
#print(STU1.N4, STU1.AG3, STU1.C0)
