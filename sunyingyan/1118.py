def bobblesort(a):
    n = len(a)
    j = 0
    while j < n:
        i = 0 # interesting way of thinking, counting the number of swaps
        while i < n - j - 1:
            if a[i] > a[i+1]:
                a[i],a[i+ 1]=a[i + 1],a[i]
            i += 1
        j += 1

def fanzhuan(a):
    i = 0
    j = len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    print(a)

def fanzhuan2(a):
    i = 0
    while i < len(a) - 1 - i:
        a[i], a[len(a) - 1 - i] = a[len(a) - 1 - i], a[i]
        i += 1
    print(a)

# jiecheng(0) should return 1
def jiecheng(n):
    if n == 0:
        return 1
    return n*jiecheng(n - 1)

# 其实这是计算一个数的排列，数字之和是100
def step(n):#a+2b+3b=100,求abc的解法数量
    if n <= 3:
        return 7 # 这是错的，n = 1 时，只有一种方法
    return step(n - 1) + step(n - 2) + step(n - 3)

def hanoi(f,t,r,n):#f是from，t是target，r是relay中转，n是盘子的数量
    if n == 1:
        print('{}→{}'.format(f,t))
        return 0#如果开始只剩一个最下面的，就直接放到target
    hanoi(f,r,t,n - 1)#把开始的除了最下面的盘子，借助relay挪到target
    print('{}→{}'.format(f,t))#把from最下面的盘子挪到target
    hanoi(r,t,f,n-1)# 把剩下的上面的盘子（在relay上），挪到target
 
def findn(a,n):
  i = 0
  while i < len(a):
    if a[i] == n:
      print('{}在数组中的下标是{}'.format(n,i))
      return 0 # why always return 0? return i instead
    i += 1
  print('-1') # return -1, not print -1

def absort(a,b): # Can you do it by comparing elements one by one from each list, since they are already sorted?
  c=a+b
  bobblesort(c)
  return c

if __name__=='__main__':
    hanoi('起始','终点','中转',3)
    a=[1,4,3,2,5]
    n=5
    findn(a,n)
    b=[9,8]
    print(absort(a,b))
