/*
動的計画法
小さい部分問題の解をメモリに記憶しておき、大きい問題の解を計算するために有効利用することが、動的計画法の基本的な考え方

例：フィボナッチ数列
入力例:
3

出力例:
3
*/

#include <iostream>
using namespace std;

int main()
{
    int n; //0<=n<=44
    cin >> n;
    int F[50];

    F[0] = F[1] = 1;
    for (int i = 2; i <= n; i++)
    {
        F[i] = F[i - 1] + F[i - 2];
    }

    cout << F[n] << endl;

    return 0;
}