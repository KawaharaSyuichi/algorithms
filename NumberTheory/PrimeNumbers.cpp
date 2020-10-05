//素数判定
/*
入力例:
6
2
3
4
5
6
7

出力例:
4
*/
#include <stdio.h>
#include <iostream>
#include <algorithm>
using namespace std;

int isPrime(int x)
{
    if (x < 2)
    {
        return 0;
    }
    else if (x == 2)
    {
        return 1;
    }
    if (x % 2 == 0)
    {
        return 0;
    }

    for (int i = 3; i * i < x; i += 2) //iがxの平方根以下の間
    {
        if (x % i == 0)
        {
            return 0;
        }
    }

    return 1;
}

int main()
{
    int n, x;
    int cnt = 0;
    scanf("%d", &n);

    for (int i = 0; i < n; i++)
    {
        scanf("%d", &x);
        if (isPrime(x))
        {
            cnt++;
        }
    }

    cout << cnt << endl;
    return 0;
}