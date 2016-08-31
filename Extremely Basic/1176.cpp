#include <iostream>



int main()
{
  long long int t=0, n=0, a=0, b=0, c=0;
  scanf("%lld\n", &t);

  while(t--)
  {
    scanf("%lld\n", &n);
    a = 0;
    b = 1;
    for(int i=0; i<n; i++)
    {
      c = a+b;
      a = b;
      b = c;
    }
    printf("Fib(%lld) = %lld\n", n, a);
  }

  return 0;
}
