# 분 단위를 초 단위로 바꾼다.
def mTos(st) :
    stos = list(map(int, st.split(':')))
    s = stos[0] * 60 + stos[1]
    return int(s)
        

def solution(video_len, pos, op_start, op_end, commands):
    # 모든 변수를 다 초 단위로 바꾼다.
    viL = mTos(video_len)
    po = mTos(pos)
    opS = mTos(op_start)
    opE = mTos(op_end)
    # 커맨드에 따라 현재 재생 위치를 변경한다.
    for c in commands :
        # 만약 현재 재생 위치가 오프닝이라면 오프닝 끝으로 이동시킨다.
        if po >= opS and po <= opE :
            po = opE
        # 커맨드가 'prev'일때 10을 빼고 0 이하면 현재 재생 위치를 0초로 둔다.
        if c == 'prev' :
            po -= 10
            if po <= 0 :
                po = 0
        # 커맨드가 'next'일때 10을 더하고 영상 끝 이상이면 현재 재생 위치를 영상 끝 위치로 둔다.
        else :
            po += 10
            if po >= viL :
                po = viL
    # 다시 한 번 현재 위치가 오프닝이면 오프닝 끝으로 이동시킨다.
    if po >= opS and po <= opE :
            po = opE
    return f'{po//60:02d}:{po%60:02d}'