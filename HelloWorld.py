# 杨辉三角python写法
def triangles():
    n = [1]
    while True:
        yield n
        n.append(0)
        n = [n[i-1] + n[i] for i in range(len(n))]  # 精炼，简直了
t = triangles()
for i in range(1, 11):
    print(next(t)) 