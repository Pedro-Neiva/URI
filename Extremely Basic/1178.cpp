#include <iostream>

int main()
{
  double a[100];
  double n = 0.0;

  scanf("%lf\n", &n);

  for(int i=0; i<100; i++)
  {
    a[i] = n;
    n /=2;
    printf("N[%d] = %.4lf\n", i, a[i]);
  }

  return 0;
}
