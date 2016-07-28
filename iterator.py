from collections import Iterator
# 用isinstance来判断是否为Iterator
print(isinstance((x for x in range(10)), Iterator))
# iter用来将dict，list，str转变为Iterator
print(isinstance(iter([]), Iterator))

# for x in [1, 2, 3, 4, 5]:
#   print(x)
# 完全等价于以下代码

# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
        print(x)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break

