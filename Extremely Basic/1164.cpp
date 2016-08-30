#include <iostream>

int main()
{
  int n=0;
  long long int x=0, t=0;

  scanf("%d\n", &n);

  while(n--)
  {
    scanf("%lld\n", &x);
    t=0;
    for(long long int i=1; i<x; i++)
    {
      if(x % i == 0)
      {
        t+=i;
      }
    }
    if(t == x)
    {
      printf("%lld eh perfeito\n", x);
    }
    else
    {
      printf("%lld nao eh perfeito\n", x);
    }
  }

  return 0;
}
