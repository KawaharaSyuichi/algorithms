/*
最小全域木(MST)
グラフの全域木の中で、辺の重みの総和が最小のグラフ。
グラフの全域木とは、グラフの全ての頂点を含むグラフであり、木(閉路を持たないグラフ)である限りできるだけ多くの辺を持つグラフ。

最小全域木を求めるアルゴリズム[プリムのアルゴリズム]は以下の通り。
グラフG=(V,E)の頂点全体の集合をV、MSTに属する頂点の集合をTとする。このとき、
1. Gから任意の頂点rを選び、それをMSTのルート(根)として、Tに追加
2. 次の処理をT=Vになるまで繰り返す
   a. Tに属する頂点とV-Tに属する頂点を繋ぐ辺の中で、重みが最小のものである辺(pu(uの親),u)を選び、それをMSTの辺として、uをTに追加

このアルゴリズムを実装するポイントは、辺の選択ステップで「どのように最小の重みを持つ辺を保存しておくか」になる。
隣接行列を用いたプリムのアルゴリズムは以下のような変数を準備して実装する。ここで、n=|V|。

color[n] : color[v]にvの訪問状態をWHITE,GRAY.BLACKを記録
M[n][n] : M[u][v]にuからvへの辺の重みを記録した隣接行列
d[n] : d[v]にTに属する頂点とT-Vに属する頂点をつなぐ辺の中で、重みが最初の辺の重みを記録
p[n] : p[v]にMSTにおける頂点vの親を記録

プリムのアルゴリズムでは、dが最小である頂点uを探すために、グラフの頂点の数だけ調べる必要がある。この探索を頂点の数だけ行うので、O(|V|**2)のアルゴリズムになる。
プリムのアルゴリズムは、二分ヒープ(優先度付きキュー)を使って頂点を決定すれば、高速化を行うことができる。その方法は最短経路問題に関する問題の解法で利用する。

入力例:
5
-1 2 3 1 -1
2 -1 -1 4 -1
3 -1 -1 1 1 
1 4 1 -1 3
-1 -1 1 3 -1

出力例:
5
*/
#include <iostream>
using namespace std;
static const int MAX = 100;
static const int INFTY = (1 << 21);
static const int WHITE = 0;
static const int GRAY = 1;
static const int BLACK = 2;

int n, M[MAX][MAX];

int prim()
{
    int u, minv;
    int d[MAX], p[MAX], color[MAX];

    for (int i = 0; i < n; i++)
    {
        d[i] = INFTY;
        p[i] = -1;
        color[i] = WHITE;
    }

    d[0] = 0;

    while (1)
    {
        minv = INFTY;
        u = -1;
        for (int i = 0; i < n; i++)
        {
            if (minv > d[i] && color[i] != BLACK)
            {
                u = i;
                minv = d[i];
            }
        }
        if (u == -1)
        {
            break;
        }
        color[u] = BLACK;
        for (int v = 0; v < n; v++)
        {
            if (color[v] != BLACK && M[u][v] != INFTY)
            {
                if (d[v] > M[u][v])
                {
                    d[v] = M[u][v];
                    p[v] = u;
                    color[v] = GRAY;
                }
            }
        }
    }
    int sum = 0;
    for (int i = 0; i < n; i++)
    {
        if (p[i] != -1)
        {
            sum += M[i][p[i]];
        }
    }

    return sum;
}

int main()
{
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            int e;
            cin >> e;
            M[i][j] = (e == -1) ? INFTY : e;
        }
    }

    cout << prim() << endl;

    return 0;
}