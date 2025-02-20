print('Multiple inheritance : ')
class A:
    def a(self):
        print('Class-A')
class B(A):
    def b(self):
        print('Class-B')
class C(B,A):
    def c(self):
        print('Class-C')
obj=C()
obj.c()
obj.b()
obj.a()