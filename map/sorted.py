
#sorted 排序算法
#可接收一个key作为排序原则
#key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序
#lambda使用
print(sorted([36, 5, -12, 9, -21], key=abs))

def cmp(x):
    return x["age"]

li = [{"age":20,"name":"def"},{"age":25,"name":"abc"},{"age":10,"name":"ghi"}]
li = sorted(li,key=cmp)
print(li)

ni  = [{"age":20,"name":"def"},{"age":25,"name":"abc"},{"age":10,"name":"ghi"}]
ni = sorted(ni,key = lambda x:x["age"])
print(ni)