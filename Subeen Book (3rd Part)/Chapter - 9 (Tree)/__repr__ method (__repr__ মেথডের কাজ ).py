# __repr__ method:
class A:
    def __init__(self):
        self.node = 10
        # উপরের def __init__ মেথডটা না দিলেও হবে ।  শুধু __repr__ মেথডটা  দিলেও হবে ।
    def __repr__(self):
        return 'class A: 10'
# Used for representing the object class, so that it can be reconstructed later.
# class এর Object কে প্রতিনিধিত্ব করার জন্য ব্যবহৃত হয়, যাতে এটি পরে পুনর্গঠন করা যায়।
a = A()
print(a)

# Second System:
# A simple Person class to __repr__ and rep() method:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        rep = 'Person(Name : ' + self.name + ', Age : ' + str(self.age) + ')'
        return rep


# Let's make a Person object and print the results of repr()

person = Person("John", 20)
print(repr(person))
