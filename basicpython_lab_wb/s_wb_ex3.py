#1
#display namespace

class MyClass:
    class_variable = 33

    def __init__(self):  # Fix: Use double underscores for the init method
        self.instance_variable = 116

    def method(self):
        local_variable = 108
        print("Namespace inside method:", locals())

# Creating an instance of MyClass
obj = MyClass()

# Displaying namespaces
print("Namespace of the class:", MyClass.__dict__)  # Fix: Use double underscores for __dict__
print("Namespace of the instance:", obj.__dict__)  # Fix: Use double underscores for __dict__

# Calling a method to show its local namespace
obj.method()




#2
#display attribute

class Student:
    def __init__(self, student_id, student_name):  # Fix: Use double underscores for __init__
        self.student_id = student_id
        self.student_name = student_name

    def add_student_class(self, student_class):
        self.student_class = student_class

# Creating an instance of the Student class
student = Student(1, 'SriRam')

# Displaying the attributes and their values before removal
print("Attributes and values before removal:")
print(student.__dict__)  # Fix: Use double underscores for __dict__

# Adding a new attribute student_class
student.add_student_class('Class 10')

# Displaying the attributes and their values after adding student_class
print("\nAttributes and values after adding student_class:")
print(student.__dict__)  # Fix: Use double underscores for __dict__

# Removing the student_name attribute
delattr(student, 'student_name')

# Displaying the attributes and their values after removing student_name
print("\nAttributes and values after removing student_name:")
print(student.__dict__)  # Fix: Use double underscores for __dict__




#3
#bankaccount stuff

class ba:
    def __init__(self, an, n, b):
        self.an = an
        self.n = n
        self.b = b

    def dep(self, a):
        if a > 0:
            self.b += a
            print(f"deposit of rs.{a} successful")
        else:
            print("invalid deposit amount")

    def wd(self, a):
        if 0 < a <= self.b:
            self.b -= a
            print(f"withdrawal of rs.{a} successful")

    def bf(self):
        f = 0.05 * self.b
        self.b -= f
        print(f"bank fees of rs.{f} applied")

    def dis(self):
        print(f"account number: {self.an}")
        print(f"account holder: {self.n}")
        print(f"balance: rs.{self.b}")

a1 = ba(an=123456, n="JohnDoe", b=1000)

a1.dis()
a1.dep(500)
a1.wd(200)
a1.bf()
a1.dis()
