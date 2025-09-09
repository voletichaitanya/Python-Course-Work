class A:
    def display_a(self):
        print("hello A")
class B(A):
    def dispaly_b(self):
        print("hello B")

b=B()
b.display_a()
b.dispaly_b()



class A:
    def display_a(self):
        print("hello A")
class B():
    def dispaly_b(self):
        print("hello B")
class C():
    def dispaly_c(self):
        print("hello C")
class D(A,B,C):
    def dispaly_d(self):
        print("hello D inherits A B C")

d=D()
d.display_a()
d.dispaly_b()
d.dispaly_c()
d.dispaly_d()

class A:
    def display_a(self):
        print("Hello A")

class B(A):
    def display_b(self):
        print("Hello B")
class C(A):
    def display_c(self):
        print("Hello C")
class D(A):
    def display_d(self):
        print("Hello D")


b=B()
b.display_a()
b.display_b()
c=C()
c.display_a()
c.display_c()
d=D()
d.display_a()
d.display_d()
class Status2015():
    def caption(self):
        print("caption added")

class Stauts2020(Status2015):
    def caption(self):
        super().caption()
        print("updated caption")

c = Stauts2020()
c.caption()

#One subclass inherits from one superclass.
class A:
   def display_a(self):
      print("parent class A")

class B(A):
   def display_b(self):
      print('Child class B (B<-A)')
a=A()
a.display_a()
b=B()
b.display_b()
b.display_a()

#Multiple Inheritance.
#more parents and single child.
#A class inherits from more than one parent class.
class A:
   def display_a(self):
      print("parent class A")

class B:
   def display_b(self):
      print('Child class B ')

class C:
   def display_c(self):
      print('Child class C ')

class D(A,B,C):
   def display_d(self):
      print('Child class A,B,C->D ')

d=D()

d.display_a()
d.display_b()
d.display_c()
d.display_d()

#Multilevel Inheritance.
#A subclass inherits from a class which itself is a subclass of another class.
class A:
   def display_a(self):
      print("parent class A")

class B(A):
   def display_b(self):
      print('Child class B ')

class C(B):
   def display_c(self):
      print('Child class C ')

class D(C):
   def display_d(self):
      print('Child class A,B,C->D ')

d=D()

d.display_a()
d.display_b()
d.display_c()
d.display_d()
#Hybrid Inheritance.
#Multiple subclasses inherit from a single superclass.
class A:
   def display_a(self):
      print("parent class A")

class B(A):
   def display_b(self):
      print('Child class B ')

class C(A):
   def display_c(self):
      print('Child class C ')

class D(B,C):
   def display_d(self):
      print('Child class A,B,C->D ')
'''
class D(A):
   def display_d(self):
      print('Child class A,B,C->D ')
'''

d=D()

d.display_a()
d.display_d()
d.display_b()
d.display_c()

c=C()
c.display_a()
c.display_a()

b=B()
b.display_a()
b.display_b()

a=A()
a.display_a()