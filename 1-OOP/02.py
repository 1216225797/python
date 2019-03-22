'''
知识点案例测试
'''

# self案例

class A():
    name = "xiaoguo"
    age = 18


# 此案例说明：
# 类实例属性和其对象实例的属性，在不对对象实例属性赋值的前提下，
# 指向同一个变量

    def run(self):
        self.name = "zhangsan"
        self.age = 19

print(A.name)
print(A.age)
print("=" * 50)
print(id(A.name))
print(id(A.age))
print("=" * 50)

a = A()

print(a.name)
print(a.age)
print("=" * 50)
print(id(a.name))
print(id(a.age))


print("*" * 100)
# 对对象属性赋值案例(接上)

class B():
    name = "gaoy"
    age = 20

    def run(self):
        self.name = "lisi"
        self.age = 90

print(B.name)
print(B.age)
print("=" * 50)
print(id(B.name))
print(id(B.age))
print("=" * 50)

print(B.__dict__)
print(b.__dict__)
b = B()
b.name = "王五"
b.age = 100

print(b.__dict__)
print(b.name)
print(b.age)
print("=" * 50)
print(id(b.name))
print(id(b.age))