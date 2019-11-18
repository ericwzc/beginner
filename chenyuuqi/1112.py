# 翻转数组
def my_revent(a):
    i = len(a)
    j = 0
    while j < len(a) / 2:
        a[j], a[i - 1] = a[i - 1], a[j]
        j = j + 1
        i = i - 1
    print(a)


# 冒泡法排序
def maopao(b):
    i = len(b)
    j = 0
    while i>0:
        while j < i-1:
            while b[j] > b[j + 1]:
                b[j], b[j + 1] = b[j + 1], b[j]
            j = j + 1
        j=0
        i=i-1


    print(b)

if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    my_revent(a)

    b = [5, 2, 3, 4, 1]
    maopao(b)
