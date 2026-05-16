def solution(A,B):
    # 하나는 오름차순, 하나는 내림차순으로 정렬한다.
    A.sort(reverse = True)
    B.sort()
    aLen = len(A)
    answer = 0
    # 그리고 오름차순 내림차순으로 두 수를 곱해 더한다.
    for i in range(aLen) :
        answer += A[i] * B[i]
    return answer