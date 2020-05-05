from model1 import fun1, Foo
from model2 import fun2
# fun1(123, 12312, 2, 3, 4, 5, 56)
# fun2()
f = Foo()
print(f)
f.foo(1)

def Foo(x):
    if (x==1):
        return 1
    else:
        return x+Foo(x-1)

print(Foo(4))