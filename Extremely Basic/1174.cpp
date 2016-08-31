#include <iostream>

int main()
{
  double a[100];
  double n = 0.0;
  int i=-1;

  while(scanf("%lf\n", &n) != EOF)
  {
    i++;
    a[i] = n;
    
    if(i==100)
    {
      break;
    }
    if(n <= 10.0)
    {
      printf("A[%d] = %.1lf\n", i, n);
    }
  }

  return 0;
}
