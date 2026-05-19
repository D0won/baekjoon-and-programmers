def solution(bandage, health, attacks):
    answer = 0
    aLen = len(attacks)
    mL = health
    fin = attacks[aLen-1][0]
    heal = 0
    for i in range(1, fin+1) :
        attack = 0
        for j in range(aLen) :
            if i == attacks[j][0] :
                health -= attacks[j][1]
                attack = 1
                heal = 0
                break
        if attack == 0 :
            health += bandage[1]
            heal += 1
            if heal == bandage[0] :
                health += bandage[2]
                heal = 0
        if health >= mL :
            health = mL
        if health <= 0 :
            return -1
        
    return health