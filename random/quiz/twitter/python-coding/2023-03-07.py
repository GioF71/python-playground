class A:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return A(self.x + other.x)
    

a1 = A(1)
a2 = A(2)

a3 = a1 + a2

print(a3.x)