from collections import Counter
def solution(points, routes):
    answer = 0
    xLen = len(routes)
    # 로봇의 경로를 차례대로 정리하는 리스트
    robots = []
    # 로봇의 경로중 가장 작은 움직임을 저장
    mLen = 0
    for route in routes :
        # 각 루트별 r좌표, c좌표를 저장하는 리스트
        dr = []
        dc = []
        # 각 로봇별 움직임을 저장하는 리스트
        robot = []
        # 각 루트별 r좌표, c좌표 저장
        for r in route :
            dr.append(points[r-1][0])
            dc.append(points[r-1][1])
        dLen = len(dr)
        rStart, cStart = dr[0], dc[0]
        robot.append([rStart, cStart])
        # r,c별로 Start 좌표와 End 좌표 설정
        for i in range(1, dLen) :
            rEnd, cEnd = dr[i], dc[i]
            rLen = abs(rEnd - rStart)
            cLen = abs(cEnd - cStart)
            for _ in range(rLen) :
                if rStart < rEnd :
                    rStart += 1
                else :
                    rStart -= 1
                robot.append([rStart, cStart])
            for _ in range(cLen) :
                if cStart < cEnd :
                    cStart += 1
                else :
                    cStart -= 1
                robot.append([rStart, cStart])
            if len(robot) > mLen :
                mLen = len(robot)
        robots.append(robot)
    for i in range(mLen) :
        temp = []
        for r in robots :
            if i < len(r) :
                temp.append(tuple(r[i]))
        
        counter = Counter(temp)
        
        for value in counter.values() :
            if value >= 2 :
                answer += 1
        
    return answer