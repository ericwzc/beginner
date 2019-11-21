# 翻转数组
# 用两个指针控制，J指针<i指针
def my_revent(a):
    i = len(a) - 1
    j = 0
    while j < i:
        a[j], a[i] = a[i], a[j]
        j += 1
        i -= 1
    print(a)


# 第一个和最后一个交换，第二个和倒数第二个……到1/2处为止
def my_revent1(a):
    i = 0
    while i < len(a) // 2:
        a[i], a[len(a) - 1 - i] = a[len(a) - 1 - i], a[i]
        i = i + 1
    print(a)


if __name__ == '__main__':
    a = [1, 2, 3]
    my_revent(a)

    b = [1, 2, 3, 6]
    my_revent1(b)
