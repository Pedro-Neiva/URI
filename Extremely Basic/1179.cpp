#include <iostream>

int main()
{

  int impar[5], par[5], n=0, i=-1, j=-1, t=15;

  while(t--)
  {
    scanf("%d\n", &n);

    if(n%2==0)
    {
      i++;
      par[i] = n;
      if(i==4)
      {
        for(i=0;i<5;i++)
        {
          printf("par[%d] = %d\n", i, par[i]);
        }
        i = -1;
      }
    }
    else
    {
      j++;
      impar[j] = n;
      if(j==4)
      {
        for(j=0; j<5; j++)
        {
          printf("impar[%d] = %d\n", j, impar[j]);
        }
        j = -1;
      }
    }
  }


  for(n=0; n<=j; n++)
  {
    printf("impar[%d] = %d\n", n, impar[n]);
  }

  for(n=0; n<=i; n++)
  {
    printf("par[%d] = %d\n", n, par[n]);
  }

  return 0;
}
