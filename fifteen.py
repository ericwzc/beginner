def solve(cur, a):
    if cur == 9:
        return True
    for i in range(1, 10):
        # try fill current cell
        a[cur] = i
        if cur == 2 and sum_fail(a, 0, 1, 2):
            continue
        if cur == 5 and sum_fail(a, 3, 4, 5):
            continue
        if cur == 6:
            if sum_fail(a, 0, 3, 6) or sum_fail(a, 2, 4, 6):
                continue
        if cur == 7:
            if sum_fail(a, 1, 4, 7):
                continue
        if cur == 8:
            if sum_fail(a, 2, 5, 8) or sum_fail(a, 0, 4, 8) or sum_fail(a, 6, 7, 8):
                continue
        # nums diff
        if diff(a, cur):
            success = solve(cur + 1, a)
            if success:
                return success
    return False


def sum_fail(a, i, j, k):
    return a[i] + a[j] + a[k] != 15


def diff(a, cur):
    l = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    i = 0
    while i <= cur:
        if l[a[i]] == 0:
            l[a[i]] += 1
        elif l[a[i]] == 1:
            return False
        i += 1
    return True


if __name__ == '__main__':
    a1 = [0 for i in range(0, 9)]
    r = solve(0, a1)
    if r:
        print(a1)

