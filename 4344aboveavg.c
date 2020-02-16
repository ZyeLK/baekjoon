#include <stdio.h>
#include <stdlib.h>

int main(void) {
  int C;
  scanf("%d\n", &C);
  for(int i=0; i<C; i++){
    int N;
    scanf("%d", &N);
    int *scores = calloc(N, sizeof(int));

    int sum = 0;
    for(int j=0; j<N; j++){
      scanf("%d", scores + j);
      sum += scores[j];
    }

    double avg = (double) sum / N;
    
    int above = 0;
    for(int j=0; j<N; j++){
      if(scores[j] > avg){
        above++;
      }
    }
    float percent = (float) above * 100 / N;
    if(percent < 10.0){
      printf("%5.3f%%\n", (float) above * 100 / N);
    }else{
      printf("%6.3f%%\n", (float) above * 100 / N);
    }
    
  }
  return 0;
}