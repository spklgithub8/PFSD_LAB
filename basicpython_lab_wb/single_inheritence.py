class parent:
    def function1(self):
        print("this is function 1")

class child(parent):
    def function2(self,a):
        print("this is function 2")
        print(a)
    b=20

y=child()
y.function1()
y.function2(10)
print(y.b)
