'''class A:
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
'''

class Status2015():
    def caption(self):
        print("caption added")

class Stauts2020(Status2015):
    def caption(self):
        super().caption()
        print("updated caption")

c = Stauts2020()
c.caption()

