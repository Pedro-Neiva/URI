#include <iostream>

int main()
{
  int a = 0, n = 0, t = 0;
  while(scanf("%d %d\n", &a, &n) != EOF)
  {
    t = 0;
    while(n <= 0)
    {
      scanf("%d\n", &n);
    }
    while (n > 0)
    {
      t = t + a;
      a++;
      n--;
    }
    printf("%d\n", t);
  }
  return 0;
}
