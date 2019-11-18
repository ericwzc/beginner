#求n！
def jiechen(n):
    m = 1
    if n==1:
        return 1
    if n>1:
        m=n*jiechen(n-1)
    return m
#求100阶爬楼梯的方法
def louti(n):
    if n==1:
        return 1
    if n==2:
        return 2
    if n==3:
        return 4
    if n>3:
        return louti(n-1)+louti(n-2)+louti(n-3)

#韩罗塔原理：f起始，t目标，r中间过渡，n个盘子
def hanluota(f,t,r,n):
    if n==1:
        print("{}——→{} ".format(f,t))
    else:
        hanluota(f,r,t,n-1)
        hanluota(f,t,r,1)
        hanluota(r,t,f, n - 1)


if __name__ == '__main__':

    print(jiechen(3))

    print(louti(4))

    hanluota(1,3,2,3)