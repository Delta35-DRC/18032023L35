# MAIN
print("main.py executed")
print("n4.ag3.c0.m0.l3.r3")
print("Name.Age.Country.Money.Learning.Rest")


def processor(self, n4, ag3, m0, r3, l3):
    for i in range(10):
        print(f"IN: age:{ag3}, money:{self.m0}, rest:{self.r3}, learning:{self.l3}")
        ag3 += 0.25
        print(f"{self.n4} is {ag3}")
        if self.m0 <= 40:
            self.m0 += 25
            self.r3 -= 10
            self.l3 -= 3
            print(f"{n4} worked, money:{self.m0}, rest:{self.r3}")
        if self.l3 <= 40:
            self.r3 -= 10
            self.l3 += 25
            self.m0 -= 3
            print(f"{n4} learned, rest:{self.r3}, learning:{self.l3}")
        if self.l3 >= 41 and self.m0 >= 50:
            self.m0 -= 20
            self.r3 += 20
            self.l3 -= 10
            print(f"{n4} rested, money:{self.m0}, rest:{self.r3}, learning:{self.l3}")
        print(f"OUT: age:{ag3}, money:{self.m0}, rest:{self.r3}, learning:{self.l3}")


class Constructor:
    STUNUM = 0

    def __init__(self, n4, ag3, c0, m0, l3, r3):
        Constructor.STUNUM += 1
        self.n4 = n4
        self.ag3 = ag3
        self.c0 = c0
        self.m0 = m0
        self.l3 = l3
        self.r3 = r3
        print(f"INFO:{self.n4}_{self.ag3}_{self.c0}_{self.m0}_{self.l3}_{self.r3}")
        processor(self, n4, ag3, m0, r3, l3)


STU1 = Constructor('PETR', 18, 'Balance', 20, 50, 50)
STU2 = Constructor('SANYA', 20, 'Bed', 500, 30, 90)
STU3 = Constructor('VASYA', 21, 'Divan', 1000, 85, 30)
STU4 = Constructor('Alex', 19, 'Life', 20, 20, 20)

print(f"STUNUM={Constructor.STUNUM}")

# Petr, Mr. Thanos
# Sanya, Mr. Sleep
# Burjuy Vasya
# Alex, Reality
