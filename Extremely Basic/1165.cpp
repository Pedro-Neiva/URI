#include <iostream>

int main()
{
  long long int x=0;
  int n=0, p=0;

  scanf("%d\n", &n);

  while(n--)
  {
    scanf("%lld\n", &x);
    p=0;
    for (long long int i=2; i<(x/2)+1; i++)
    {
      if(x%i==0)
      {
        p=1;
      }
    }
    if (p==1)
    {
      printf("%lld nao eh primo\n", x);
    }
    else
    {
      printf("%lld eh primo\n", x);
    }
  }

  return 0;
}
