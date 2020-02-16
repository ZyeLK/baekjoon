#include <stdio.h>

int main(void){
    int A, B, C;
    scanf("%d\n%d\n%d", &A, &B, &C);
    int num = A * B * C;
    
    char str[10];
    sprintf(str, "%d", num);
    int amount[10];
    for(int i = 0; i < 10; i++){
        amount[i] = 0;
    }
    
    for(int i = 0; i < 10; i++){
        if(str[i] >= '0' && str[i] <= '9'){
            amount[str[i] - '0']++;
        }
    }
    
    for(int i = 0; i < 10; i++){
        printf("%d\n", amount[i]);
    }
    
    return 0;
}