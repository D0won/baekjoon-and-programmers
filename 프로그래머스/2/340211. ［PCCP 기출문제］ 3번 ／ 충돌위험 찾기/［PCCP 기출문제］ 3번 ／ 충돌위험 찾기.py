from collections import Counter

# AI 도움을 받음(시작 좌표 중복 문제 수정, Counter 함수 사용 참고)
def solution(points, routes):
    answer = 0

    # 각 로봇들의 전체 이동 경로를 저장할 리스트
    robots = []

    # 로봇들 중 가장 긴 이동 시간을 저장
    mLen = 0

    # route 하나가 로봇 한 대의 이동 경로
    for route in routes:
        # 해당 로봇이 지나가야 하는 r좌표와 c좌표를 따로 저장
        dr = []
        dc = []

        # 해당 로봇의 시간별 위치를 저장할 리스트
        robot = []

        # route에 적힌 번호를 실제 좌표로 바꿔서 저장
        for r in route:
            dr.append(points[r-1][0])
            dc.append(points[r-1][1])

        dLen = len(dr)

        # 처음 시작 좌표는 0초 위치이므로 먼저 저장
        rStart, cStart = dr[0], dc[0]
        robot.append([rStart, cStart])

        # 다음 목적지까지 순서대로 이동하면서 좌표 저장
        for i in range(1, dLen):
            rEnd, cEnd = dr[i], dc[i]

            # 현재 위치에서 목적지까지 r좌표, c좌표가 얼마나 차이나는지 계산
            rLen = abs(rEnd - rStart)
            cLen = abs(cEnd - cStart)

            # 문제 조건에 따라 r좌표를 먼저 이동
            for _ in range(rLen):
                if rStart < rEnd:
                    rStart += 1
                else:
                    rStart -= 1

                # 한 칸 이동할 때마다 현재 위치 저장
                robot.append([rStart, cStart])

            # r좌표 이동이 끝나면 c좌표 이동
            for _ in range(cLen):
                if cStart < cEnd:
                    cStart += 1
                else:
                    cStart -= 1

                # 한 칸 이동할 때마다 현재 위치 저장
                robot.append([rStart, cStart])

            # 가장 긴 로봇 경로 길이 저장
            if len(robot) > mLen:
                mLen = len(robot)

        # 완성된 한 로봇의 경로를 전체 로봇 리스트에 저장
        robots.append(robot)

    # 같은 시간대에 로봇들이 어디에 있는지 비교
    for i in range(mLen):
        temp = []

        # i초에 존재하는 로봇들의 위치를 모음
        for r in robots:
            if i < len(r):
                temp.append(tuple(r[i]))

        # 같은 좌표가 몇 번 나왔는지 카운트
        counter = Counter(temp)

        # 같은 시간, 같은 좌표에 로봇이 2대 이상 있으면 충돌 위험 1개로 계산
        for value in counter.values():
            if value >= 2:
                answer += 1

    return answer