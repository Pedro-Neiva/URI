#include <iostream>

int main()
{
  int a[1000];
  int n=0, x=0;

  scanf("%d\n", &n);

  for(int i=0; i<1000; i++)
  {
    if(x == n)
    {
      x = 0;
    }
    a[i] = x;
    x++;
    printf("N[%d] = %d\n", i, a[i]);
  }


  return 0;
}
