#include <iostream>

int main (int argc, char* argv[])
{

  int c, p, r, g, b = 0;
  char m, s = 'a';

  scanf("%d\n", &c);
  while (c)
  {
    scanf("%d\n", &p);
    r = 0;
    b = 0;
    g = 0;
    while (p)
    {
      scanf("%c %c\n", &m, &s);
      if (m == 'B' && s == 'G')
      {
        b++;
      }
      else if (m == 'B' && s == 'R')
      {
        b += 2;
      }
      else if (m == 'R' && s == 'B')
      {
        r++;
      }
      else if (m == 'R' && s == 'G')
      {
        r += 2;
      }
      else if (m == 'G' && s == 'R')
      {
        g++;
      }
      else if (m == 'G' && s == 'B')
      {
        g += 2;
      }
      p--;
    }

    if (r == g && r == b)
    {
      printf("trempate\n");
    }
    else if (r == g && r > b)
    {
      printf("empate\n");
    }
    else if (r == b && r > g)
    {
      printf("empate\n");
    }
    else if (b == g && b > r)
    {
      printf("empate\n");
    }
    else if (r > g && r > b)
    {
      printf("red\n");
    }
    else if (g > r && g > b)
    {
      printf("green\n");
    }
    else if (b > r && b > g)
    {
      printf("blue\n");
    }

    c--;
  }

  return 0;
}
