# 高阶函数
# 1.变量可以指向函数
# 2.函数名可以是变量
# 3.传入函数
def f(a):
    return a*a

def add(x, y, f):
    print(f(x) + f(y))
k = f
add(1, 2, k)

