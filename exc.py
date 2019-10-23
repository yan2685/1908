"""
求100000以内质数之和，
将过程封装为函数， 可以使用sum()函数求和
统计函数执行所用时间
"""
import time

def timeit(f):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        res = f(*args,**kwargs)
        end_time = time.time()
        print("%s函数运行时间：%.6f"%(f.__name__,end_time-start_time))
        return res
    return wrapper

# 判断一个数是否为质数
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2,n // 2 + 1):
        if n % i == 0:
            return False
    return True

# 求100000以内质数之和
@timeit
def prime():
    pr = []
    for i in range(1,100001):
        if isPrime(i):
            pr.append(i)
    print(sum(pr))

prime()

