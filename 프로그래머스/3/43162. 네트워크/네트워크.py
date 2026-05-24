# ai 도움을 받음
def solution(n, computers):
    answer = 0
    # 방문한 컴퓨터 확인
    visited = [0] * n
    def dfs(computer) :
        # 방문 시 해당 컴퓨터 번호를 1로 둠
        visited[computer] = 1
        # 해당 컴퓨터가 다른 컴퓨터와 연결되어 있는지, 그리고 해당 컴퓨터가 방문했는지 확인
        for j in range(n) :
            if computers[computer][j] == 1 and visited[j] == 0 :
                dfs(j)
    # 방문한 적 있는 컴퓨터를 제외한 나머지 경우엔 answer += 1함.
    for i in range(n) :
        if visited[i] == 0 :
            dfs(i)
            answer += 1
    return answer