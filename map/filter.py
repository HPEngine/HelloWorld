#filter把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
#filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回lis
def is_odd(n):
    return n % 2 == 1
print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))
#把一个序列中的空字符串删掉
def not_empty(s):
    return s and s.strip()
list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
#艾氏筛法
#先定义一个从3开始的生成器
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
#再定义一个筛选器
def _not_divisible(n):
    return lambda x:x % n > 0
#生成器，不断产生下一个素数
def primes():
    yield 2
    it = _odd_iter() #初始序列
    while True:
        n = next(it) #返回序列第一个数
        yield n
        it = filter(_not_divisible(n),it)
#打印1000以内的素数
for n in primes():
    if n < 1000:
        print(n)
    else:
        break
