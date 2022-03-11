def print_formatted(T):
    for ind, el in enumerate(T):
        if ind == len(T)-1:
            print(el)
        else:
            print(el, end=' ')


def bin(TAB, x):
    left = 0
    right = len(TAB)-1
    while left <= right:
        mid = (left+right)>>1
        if TAB[mid] > x:
            right = mid - 1
        elif TAB[mid] < x:
            left = mid + 1
        else:
            return True
    return False


def cat(TAB, x):
    if x == 0:
        return True
    N = len(TAB)
    i = 0
    j = 1
    while j < N:
        d = TAB[j] - TAB[i]
        if d == x:
            return True
        elif d < x:
            j += 1
        else:
            i += 1
    return False


def mmd(TAB):
    N = len(TAB)
    min_val = 10**100
    max_val = -10**100
    for i in range(N//2):
        (lwr, hgr) = ((TAB[i<<1], TAB[(i<<1)+1]) if TAB[i<<1] < TAB[(i<<1)+1] 
                                             else (TAB[(i<<1)+1], TAB[i<<1]))
        if min_val > lwr:
            min_val = lwr
        if max_val < hgr:
            max_val = hgr
    if N & 1 == 1:
        if min_val > TAB[N-1]:
            min_val = TAB[N-1]
        if max_val < TAB[N-1]:
            max_val = TAB[N-1]
    return max_val-min_val


def isrt(TAB):
    N = len(TAB)
    for i_div in range(1, N):
        j = 0
        while TAB[i_div] > TAB[j] and j < i_div:
            j += 1
        
        tmp = TAB.pop(i_div)
        TAB.insert(j, tmp)



def ssrt(TAB):
    N = len(TAB)
    for i_div in range(N-1):
        min_ind = i_div
        for j in range(i_div, N):
            if TAB[j] < TAB[min_ind]:
                min_ind = j
        TAB[i_div], TAB[min_ind] = TAB[min_ind], TAB[i_div]



def bsrt(TAB):
    N = len(TAB)
    for i in range(N-1):
        for j in range(i, N):
            if TAB[i] > TAB[j]:
                TAB[i], TAB[j] = TAB[j], TAB[i]


def qsrt(TAB, left=0, right=None):
    if right is None:
        right = len(TAB)-1
    pivot = TAB[(left+right)>>1]
    i = left
    j = right
    while i <= j:
        while TAB[i] < pivot:
            i += 1
        while TAB[j] > pivot:
            j -= 1
        if i <= j:
            TAB[i], TAB[j] = TAB[j], TAB[i]
            i += 1
            j -= 1
    if left < j:
        qsrt(TAB, left, j)
    if i < right:
        qsrt(TAB, i, right)


if __name__ == '__main__':
    q = int(input())

    inp = input().split()
    tab = [int(v) for v in inp]
    # print(mmd(tab))

    # qsrt(tab)
    # print_formatted(tab)

    for i in range(q):
        # print(bin(tab, int(input())))
        print(cat(tab, int(input())))
