def solution(bandage, health, attacks):
    answer = 0
    aLen = len(attacks)
    # 최대 체력 저장
    mL = health
    # 몬스터의 마지막 공격 시간 저장
    fin = attacks[aLen-1][0]
    # 붕대 감은 횟수 저장
    heal = 0
    # 몬스터의 마지막 공격 시간까지 for문 돌림
    for i in range(1, fin+1) :
        # 몬스터의 공격 여부 확인
        attack = 0
        # 몬스터의 공격 확인
        for j in range(aLen) :
            if i == attacks[j][0] :
                health -= attacks[j][1]
                attack = 1
                heal = 0
                break
        # 만약에 몬스터의 공격을 안 받았다면 체력 회복
        if attack == 0 :
            health += bandage[1]
            heal += 1
            if heal == bandage[0] :
                health += bandage[2]
                heal = 0
        # 체력이 최대최력보다 높다면 최대체력으로 지정
        if health >= mL :
            health = mL
        # 만약 체력이 0 이하면 -1 return
        if health <= 0 :
            return -1
        
    return health