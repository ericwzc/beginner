#写函数合并两个排好序的列表为一个列表，要求生成一个新列表，包含两个列表的内容，
# 且按照从小到大排好序。
def combine(a,b):
    for x in range(0,len(b)):
        a.append(b[x])
    maopao(a)


def maopao(b):
    i = len(b)
    j = 0
    while i>0:
        while j < i-1:
            if b[j] > b[j + 1]:
                b[j], b[j + 1] = b[j + 1], b[j]
            j = j + 1
        j=0
        i=i-1
    print(b)


#给定一个排好序的列表，和一个数字，写函数判断该数字是否在列表中，
# 如果找到数字返回该数字在列表中的下标，找不到返回-1
def panduan(a,b):
    i=0
    while i<len(a):
        if a[i]==b:
            print(i)
            break
        i=i+1
    if i==len(a):
        print('-1')


#写程序将数字1-9，填入一个3*3的表格，使得每行，每列，斜线相加都等于15.
# 提示：可以用一个长度为9的列表表示每个格子
def shudu():
    a = []
    for x in range(1, 10):
        for y in range(1, 10):
            if 15 - x - y > 0 and 20 - 2 * x - y > 0 and x + y - 5 > 0 and 2 * x + y - 10 > 0 and x != y and x != 5 and y != 5 and 15 - x - y != 5 and 20 - 2 * x - y != 5 and x + y - 5 != 10 - x and 15 - x - y != y and (
                    15 - x - y) != (20 - 2 * x - y) and (15 - x - y) != (2 * x + y - 10) and x != (20 - x * 2 - y):
                a.append(x)
                a.append(y)
                a.append(15 - x - y)
                a.append(20 - 2 * x - y, )
                a.append(5)
                a.append(2 * x + y - 10)
                a.append(x + y - 5)
                a.append(10 - x)
                a.append(10 - y)
            if len(a) > 0:
                print(a)
            a = []




if __name__ == '__main__':
    a=[2,4,8,9]
    b=[1,7,11]
    combine(a,b)

    x=[2,6,8,9,10]
    y=6
    panduan(x,y)

    shudu()






