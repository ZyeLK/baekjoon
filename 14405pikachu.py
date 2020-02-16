# Pikachu.py
# 백준 14405
# 주어진 문자열이 피카츄가 발음할 수 있는 단어인지 확인
# pi, ka, chu 만 발음가능

S = input()
i = 0
result = 'YES'

while i < len(S) :

    if i + 2 <= len(S) and (S[i:i + 2] == 'pi' or S[i:i + 2] == 'ka') :
        i += 2
        continue
    elif i + 3 <= len(S) and S[i:i + 3] == 'chu' :
        i += 3
        continue
    else :    
        result = 'NO'
        break

print(result)