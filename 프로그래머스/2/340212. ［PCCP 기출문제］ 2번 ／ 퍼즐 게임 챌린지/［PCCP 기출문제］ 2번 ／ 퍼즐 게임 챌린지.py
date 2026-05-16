def solution(diffs, times, limit):
    dLen = len(diffs)
    dMax = max(diffs)
    dMin = 1
    answer = dMax
    while  dMin < dMax:
        time = 0
        pTime = 0
        level = (dMax + dMin) // 2 
        for i in range(dLen) :
            if diffs[i] <= level :
                time += times[i]
            else :
                time += (pTime + times[i]) * (diffs[i] - level) + times[i]
            pTime = times[i]
        if time <= limit :
            dMax = level
            answer = level
        else :
            dMin = level + 1
    return answer