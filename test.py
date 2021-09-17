class A:
    b = 0
    def add_a(self):
        self.b += 1


print(A().b)
a = A()

a.add_a()
print(a.b)

g = A()
print(g.b)

print(help(A))