#include <iostream>

int main()
{
  int l=0, i=0, j=0;
  double n=0.0, t=0.0;
  int m[12][12];
  char o='a';

  scanf("%d\n", &l);
  scanf("%c\n", &o);

  for(i=0; i<12; i++)
  {
    for(j=0; j<12; j++)
    {
      scanf("%lf\n", &n);
      m[i][j] = n;
    }
  }

  for(i=0; i<12; i++)
  {
    t+=m[l][i];
  }

  if(o == 'M')
  {
    t/=12;
  }

  printf("%.1lf\n", t);

  return 0;
}
