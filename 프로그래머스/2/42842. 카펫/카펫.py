# 소인수분해를 통해 인수들을 다 구한다.
def prime(y) :
    dual = []
    for i in range(1, int(y**(1/2)) + 1) :
        if y % i == 0 :
            dual.append([i, y//i])
    return dual

def solution(brown, yellow):
    # 먼저 짝을 이룬 인수들을 다 구한다.
    d = prime(yellow)
    # 전체 카펫 수를 다 구한다.
    s = brown + yellow
    dLen = len(d)
    # 전체 카펫 수와 짝을 이룬 인수의 각 요소에 + 2 한 값(즉 나중에 갈색으로 가장자리를 채울 값)
    # 들을 곱해 전체 카펫 수와 같으면 각 요소에 + 2한 값들을 내림차순으로 정렬하여 반환한다.
    for i in range(dLen) :
        if s == (d[i][0] + 2) * (d[i][1] + 2) :
            return sorted([d[i][0] + 2, d[i][1] + 2], reverse = True)
