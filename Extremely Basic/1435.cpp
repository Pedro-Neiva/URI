#include <iostream>
#include <cmath>

int main()
{
  int d=0, i=0, j=0, c=0, v=1, l=1;
  int a[100][100];

  while(scanf("%d\n", &d), d!=0)
  {
    l= (d+1)/2;
    c=0;
    v=1;
    while(l--)
    {
      for(i=c; i<d-c; i++)
      {
        for(j=c; j<d-c; j++)
        {
          a[i][j] = v;
        }
      }
      v++;
      c++;
    }

    for(i=0; i<d; i++)
    {
      for(j=0; j<d; j++)
      {
        if(j==d-1)
        {
          printf("%3d", a[i][j]);
        }
        else
        {
          printf("%3d ", a[i][j]);
        }
      }
      printf("\n");
    }
    printf("\n");
  }

  return 0;
}
