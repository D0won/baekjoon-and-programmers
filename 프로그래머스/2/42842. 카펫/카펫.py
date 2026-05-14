def prime(y) :
    dual = []
    for i in range(1, int(y**(1/2)) + 1) :
        if y % i == 0 :
            dual.append([i, y//i])
    return dual
def solution(brown, yellow):
    d = prime(yellow)
    s = brown + yellow
    dLen = len(d)
    for i in range(dLen) :
        if s == (d[i][0] + 2) * (d[i][1] + 2) :
            return sorted([d[i][0] + 2, d[i][1] + 2], reverse = True)
