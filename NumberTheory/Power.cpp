//べき乗
/*
入力例:
5 8

出力例:
390625
*/

#include <iostream>
#include <cmath>

using namespace std;
typedef unsigned long long ullong;

ullong power(ullong x, ullong n, ullong M)
{
    ullong res = 1;

    if (n > 0)
    {
        res = power(x, n / 2, M);
        if (n % 2 == 0)
        {
            res = (res * res) % M;
        }
        else
        {
            res = (((res * res) % M) * x) % M;
        }
    }

    return res;
}

main()
{
    int m, n;
    cin >> m >> n;

    cout << power(m, n, 1000000007) << endl;

    return 0;
}