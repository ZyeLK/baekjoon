#hansu.py
#1 이상 N 이하 한수의 개수 출력 (N은 최대 1000)
#한수 : 각 자리수가 등차수열을 이루는 수

N = int(input())
result = 0

result += N if N < 100 else 99  # 1부터 99까지는 모든 수가 한수임.

for i in range(111, N + 1) :
    hunds, tens, ones = i // 100, i // 10 % 10, i % 10
    # 100의자리, 10의자리, 1의자리수
    if (hunds + ones) / 2 == tens :  # 등차수열 이루는지 판단
        result += 1

print(result)
