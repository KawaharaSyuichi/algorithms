/*
最長増加部分列(LSI)

A:数列
L[n] : L[i]を長さがi+1であるような増加部分列の最後の要素の最小値とする配列(詳しくはP.423を参照)
length_i : i番目の要素までを使った最長増加部分列の長さを表す整数

入力例:
5
5
1
3
2
4

出力例:
3
*/
#include <iostream>
#include <algorithm>
#define MAX 100000
using namespace std;

int n, A[MAX + 1], L[MAX];

int lis()
{
    L[0] = A[0];
    int length = 1;

    for (int i = 1; i < n; i++)
    {
        if (L[length - 1] < A[i])
        {
            L[length++] = A[i];
        }
        else
        {
            *lower_bound(L, L + length, A[i]) = A[i];
        }
    }

    return length;
}

int main()
{
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> A[i];
    }

    cout << lis() << endl;

    return 0;
}