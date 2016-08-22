#include <stdio.h>
#include <iostream>
#include <cmath>

int main (int argc, char* argv[])
{
  int r1, x1, y1, r2, x2, y2 = 0;
  double d = 0;


  while(scanf("%d %d %d %d %d %d", &r1, &x1, &y1, &r2, &x2, &y2) == 6)
  {
    d = sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));

    if (r2 + d <= r1)
    {
      printf("RICO\n");
    }
    else
    {
      printf("MORTO\n");
    }
  }
  return 0;
}
