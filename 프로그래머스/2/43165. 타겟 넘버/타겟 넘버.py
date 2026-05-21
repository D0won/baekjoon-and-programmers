def solution(numbers, target):
    # 더하고 뺀 결과를 담는 리스트
    result = []
    # dfs를 활용하여 numbers 안의 수가 - 혹은 +로 재귀를 통해 더하여 index가 넘으면 반환
    def dfs(numbers, idx, snum) :
        if idx >= len(numbers) :
            result.append(snum)
            return 
        pnum = snum + numbers[idx]
        mnum = snum + numbers[idx] *(-1)
        dfs(numbers, idx+1, pnum)
        dfs(numbers, idx+1, mnum)    
    dfs(numbers, 0, 0)
    # result 리스트 안의 target의 수를 반환
    return result.count(target)