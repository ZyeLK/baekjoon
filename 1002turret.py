import math

n = int(input())
for i in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    # 두 원의 교점의 개수 구하기

    d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    if d == 0 and r1 == r2 :
        print(-1) # 만나는 점 무한개
    elif d > r1 and d > r2 : # '외접'
        if r1 + r2 > d : print(2)
        elif r1 + r2 == d : print(1)
        else : print(0)
    else : # '내접'
        if abs(r1 - r2) < d : print(2)
        elif abs(r1 - r2) == d : print(1)
        else : print(0)