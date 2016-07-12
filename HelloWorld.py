#杨辉三角python写法
def triangles():
    N = [1]
    while True:
        yield N
        N.append(0)
        N = [N[i-1] + N[i] for i in range(len(N))] #精炼，简直了
t = triangles()
for i in range(1,11):
    print(next(t))