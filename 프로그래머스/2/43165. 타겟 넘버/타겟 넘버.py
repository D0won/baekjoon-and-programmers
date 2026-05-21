def solution(numbers, target):
    answer = 0
    result = []
    def dfs(numbers, idx, snum) :
        if idx >= len(numbers) :
            result.append(snum)
            return 
        pnum = snum + numbers[idx]
        mnum = snum + numbers[idx] *(-1)
        dfs(numbers, idx+1, pnum)
        dfs(numbers, idx+1, mnum)    
    dfs(numbers, 0, 0)
    return result.count(target)