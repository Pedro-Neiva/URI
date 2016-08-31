#include <iostream>

int main()
{
  int x[10];
  int n=0, i=0;
  while(scanf("%d\n", &n) == 1)
  {
    x[i] = n;
    i++;
  }
  for(i=0; i<10; i++)
  {
    if(x[i] <= 0)
    {
      x[i] = 1;
    }
    printf("X[%d] = %d\n", i, x[i]);
  }


  return 0;
}
