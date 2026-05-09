def mTos(st) :
    stos = list(map(int, st.split(':')))
    s = stos[0] * 60 + stos[1]
    return int(s)
        

def solution(video_len, pos, op_start, op_end, commands):
    viL = mTos(video_len)
    po = mTos(pos)
    opS = mTos(op_start)
    opE = mTos(op_end)
    for c in commands :
        if po >= opS and po <= opE :
            po = opE
        if c == 'prev' :
            po -= 10
            if po <= 10 :
                po = 0
        else :
            po += 10
            if po >= viL :
                po = viL
    if po >= opS and po <= opE :
            po = opE
    return f'{po//60:02d}:{po%60:02d}'