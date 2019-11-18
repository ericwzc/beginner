def bobblesort(a):
    n = len(a)
    j = 0
    while j < n:
        i = 0
        while i < n - j - 1:
            if a[i] > a[i+1]:
                a[i],a[i+ 1]=a[i + 1],a[i]
            i += 1
        j += 1


if __name__=='__main__':
    a=[34,2,24,7]
    bobblesort(a)
    print(a)
