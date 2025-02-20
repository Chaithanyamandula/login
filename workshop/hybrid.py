print('Hybrid inheritance : ')
class A:
    def a(self):
        print('Class-A')
class B(A):
    def b(self):
        print('Class-B')
class C:
    def c(self):
        print('Class-C')
        
class D(C,B):
    def d(self):
        print('Class-D')
obj=B()
obj.a()
obj.b()
obj1=D()
obj1.c()
obj1.d()