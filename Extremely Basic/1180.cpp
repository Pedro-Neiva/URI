#include <iostream>

int main()
{
  int s=0, i=0, j=0, n=0, m=0, p=0;
  int a[1000];

  scanf("%d\n", &s);
  j = s;

  while(s--)
  {
    scanf("%d", &n);
    a[i] = n;
    if(n<m)
    {
      m = n;
      p = i;
    }
    i++;
  }

  printf("Menor valor: %d\n", m);
  printf("Posicao: %d\n", p);

  return 0;
}
