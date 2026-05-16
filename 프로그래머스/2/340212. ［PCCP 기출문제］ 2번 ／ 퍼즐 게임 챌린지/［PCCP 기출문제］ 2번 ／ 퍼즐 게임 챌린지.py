def solution(diffs, times, limit):
    # 요소들의 길이 저장
    dLen = len(diffs)
    # 요소들의 큰 것과 작은 것들을 각각 저장
    dMax = max(diffs)
    dMin = min(diffs)
    # answer은 제일 큰 요소라고 지정
    answer = dMax
    # dMin이 dMax와 같거나 클 때 loop 중단(이진 탐색)
    while  dMin < dMax:
        time = 0
        pTime = 0
        # 중간값 계산
        level = (dMax + dMin) // 2 
        for i in range(dLen) :
            if diffs[i] <= level :
                time += times[i]
            else :
                time += (pTime + times[i]) * (diffs[i] - level) + times[i]
            pTime = times[i]
        # 만약에 time이 limit 보다 작거나 같다면 dMax를 level로 둠.
        if time <= limit :
            dMax = level
            answer = level
        # 만약에 time이 level보다 크다면 dMin을 level + 1로 둠
        else :
            dMin = level + 1
    return answer