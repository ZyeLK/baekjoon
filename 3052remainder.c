#include <stdio.h>

int main(void){
    int N = 10;
    int div = 42;
    
    int rs[N]; // 나머지의 리스트
    int temp;  // 저장소
    
    // 초기화
    scanf("%d", &temp);
    rs[0] = temp % div;
    int ans = 1; // 최종 답(몇 개가 다른지)
    
    for(int i=0; i<N-1; i++){
        scanf("%d", &temp);
        int r = temp % div;
        
        int new = 1; // r이 새로운 나머지인지 여부
        for(int j=0; j<ans; j++){
            if(rs[j] == r){
                new = 0;
                break;
            }
        }
        if(new == 1){
            rs[ans] = r;
            ans++;
        }
    }
    
    printf("%d", ans);
    return 0;
}