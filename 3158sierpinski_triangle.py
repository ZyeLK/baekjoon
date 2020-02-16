# sierpinski_triangle.py
# 힇힇

N = int(input()) - 1 # 3 * 2^k 꼴의 자연수 입력(전체 줄의 수)
i = 0 # 현재 몇 번째 줄인지 기억

# 삼각형 앞쪽 공백
def front(N, i) :
    print(' ' * (N - i), end='')

def convertstr(lst, i) :
    s = ""
    for b in lst :
        if b == 0:
            s += "     "
        else :
            if i % 3 == 0 : s += "  *  "
            elif i % 3 == 1: s += " * * "
            else : s += "*****"
        s += " "
    
    del s[-1]
    return s