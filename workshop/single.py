print('Single inheritance : ')
class A:
    def a(self):
        print('Class-A')
class B(A):
    def b(self):
        print('Class-B')
class C(B):
    def c(self):
        print('Class-C')
obj=C()
obj.a()
obj.b()
obj.c()