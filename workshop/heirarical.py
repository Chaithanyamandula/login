print('Heirarical inheritance : ')
class A:
    def a(self):
        print('class-A')
class B(A):
    def b(self):
        print('class-B')
class C(A):
    def c(self):
        print('class-C')
obj=C()
obj1=B()
obj.a()
obj1.b()
obj.c()