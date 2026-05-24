def solution(n, computers):
    answer = 0
    visited = [0] * n
    def dfs(computer) :
        visited[computer] = 1
        
        for j in range(n) :
            if computers[computer][j] == 1 and visited[j] == 0 :
                dfs(j)
        
    for i in range(n) :
        if visited[i] == 0 :
            dfs(i)
            answer += 1
    return answer