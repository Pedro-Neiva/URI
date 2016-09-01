#include <iostream>

int main()
{
  int i=0, j=0, c=0;
  double n=0.0, t=0.0;
  double m[12][12];
  char o='a';

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
    for(j=0; j<11-i; j++)
    {
      t += m[i][j];
      c++;
    }
  }

  if(o == 'M')
  {
    t/=c;
  }

  printf("%.1lf\n", t);

  return 0;
}
