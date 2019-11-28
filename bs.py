import math

# binary search
def bs(a, f, t, n):
    if f > t:
        return -1
    mid = math.floor((f + t) / 2) 
    if a[mid] == n:
        return mid
    elif a[mid] > n:
        return bs(a, f, mid - 1, n)
    else:
        return bs(a, mid + 1, t, n)

def test(a, data):
    for x in data:
        i = bs(a, 0, len(a) - 1, x)
        print('find {}, result: {}'.format(x, i))

if __name__ == "__main__":
    a1 = [1,3,9]
    a2 = [0,2,4,5,6,7,10]
    test(a1, a1)
    test(a1, a2)