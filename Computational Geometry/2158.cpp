#include <iostream>

int main (int argc, char* argv[])
{
  long long int fp, fh, v, f, a, m = 0;

  while(scanf("%lld %lld\n", &fp, &fh) == 2)
  {
    m++;
    a = ((fp * 5) + (fh * 6)) / 2;
    f = fp + fh;
    v = a + 2 - f;
    printf("Molecula #%lld.:.\n", m);
    printf("Possui %lld atomos e %lld ligacoes\n\n", v, a);
  }
  return 0;
}
