#include <iostream>

int main()
{
  int a[20];
  int n=0;
  int i=-1, j=0;

  while(scanf("%d\n", &n) != EOF)
  {
    i++;
    a[i] = n;
  }

  for (i=0, j=19;i<10;i++,j--)
  {
    n = a[i];
    a[i] = a[j];
    a[j] = n;
  }

  for(i=0; i<20; i++)
  {
    printf("N[%d] = %d\n", i, a[i]);
  }

  return 0;
}
