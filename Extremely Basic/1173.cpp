#include <iostream>

int main()
{
  int n[10];
  int v = 0;

  scanf("%d\n", &v);

  for(int i=0; i<10; i++)
  {
    n[i] = v;
    v*=2;
    printf("N[%d] = %d\n", i, n[i]);
  }

  return 0;
}
