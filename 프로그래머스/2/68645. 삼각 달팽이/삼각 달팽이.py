def solution(n):
    p = 1
    maxi = sum([ i for i in range(1, n + 1)])
    snail = [0] * (maxi)
    idx = 0
    num = 1
    k = 0
    for i in range(n) :
        if i % 3 == 0 :
            for j in range(n - i) :
                idx += k
                snail[idx] = num
                num += 1
                k += 1
        elif i % 3 == 1 :
            for j in range(n-i) :
                idx += 1
                snail[idx] = num
                num += 1
        else :
            for j in range(n-i) :
                idx -= k
                snail[idx] = num
                num += 1
                k -= 1
    return snail