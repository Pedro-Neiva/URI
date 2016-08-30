#include <iostream>

int main ()
{
  int t=0, pa=0, pb=0, y=0;
  double g1=0.0, g2=0.0;

  scanf("%d\n", &t);

  while (t--)
  {
    scanf("%d %d %lf %lf\n", &pa, &pb, &g1, &g2);
    y=0;
    //printf("pa=%d pb=%d g1=%lf g2=%lf\n", pa,pb,g1,g2);
    while(y < 100)
    {
      //printf("Ano %d pa= %d pb=%d\n", y, pa, pb);
      y++;
      pa = pa * (1 + g1 / 100);
      pb = pb * (1 + g2 / 100);
      if (pa > pb)
      {
        printf("%d anos.\n", y);
        y = 65000;
      }
    }
    if(y != 65000)
    {
      printf("Mais de 1 seculo.\n");
    }
  }


  return 0;
}
