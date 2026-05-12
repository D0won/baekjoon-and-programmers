# 올바른 문자열인지 아닌지 확인
def par(p) :
    # 리스트(스택) 정의
    st = []
    # 만약 '(' 라면 append, 아니라면 pop
    for s in p :
        if s == '(' :
            st.append('(')
        else :
            # pop 가능하지 않으면 균형잡힌 괄호
            try :
                st.pop()
            except :
                return False
    # 문제 없다면 올바른 괄호
    return True

def solution(p):
    # 빈 문자열이면 빈 문자열 반환
    if p == '' :
        return ''
    # 왼쪽 괄호, 오른쪽 괄호 개수 세기
    l = 0
    r = 0
    # 괄호 문자열 길이 저장
    pLen = len(p)
    # 인덱스 저장하는 변수
    idx = 0
    # l과 r이 같다면 같은 지점(인덱스)를 저장
    for i in range(pLen) :
        if p[i] == '(' :
            l += 1
        else :
            r += 1
        if l == r :
            idx = i
            break
    # u와 v로 나누기
    u = p[:idx+1]
    v = p[idx+1:]
    # 3단계 수행
    if par(u) == True:
        return u + solution(v)
    # 4단계 수행
    else :
        st = '('
        st += solution(v)
        st += ')'
        temp = ''
        for y in u[1:len(u)-1] :
            if y == ')' :
                temp += '('
            else :
                temp += ')'
        st += temp
        return st