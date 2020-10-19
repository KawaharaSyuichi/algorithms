/*
単一始点最短経路
与えられた重み付き有向グラフG=(V,E)について、単一始点最短経路のコストを求めるプログラム

ダイクストラのアルゴリズム
グラフG=(V,E)の頂点全体の集合をV、始点をs、最短経路木に含まれている頂点の集合をSとします。
各計算ステップで、最短経路木の辺と頂点を選びSへ追加します。
各頂点iについて、S内の頂点のみを経由したsからiへの最短経路のコストをd[i]、最短経路木におけるiの親をp[i]とする。
1.初期状態で、Sを空にする
 a. sに対してd[s]=0
 b. s意外のVに属する全ての頂点iに対してd[i]=∞
2.以下の処理をS=Vとなるまで繰り返す
 a. V-Sの中から、d[u]が最小である頂点uを選択
 b. uをSに追加すると同時に、uに隣接しかつV-Sに属する全ての頂点vに対する値を以下のように更新
 if d[u]+w(u,v)<d[v]
    d[v]=d[u]+w(u,v)
    p[v]=u

隣接行列を用いたダイクストラのアルゴリズムは、以下のような変数を準備
color[n] : color[v]にvの訪問状態WHITE,GRAY,BLACKのいずれかを記録
M[n][n] : M[u][v]にuからvへの辺の重みを記録した隣接行列
d[n] : d[v]に始点sからvまでの最短コストを記録
p[n] : p[v]に最短経路における頂点vの親を記録

このアルゴリズムは、dの値が最小である頂点uをO(|V|)で求める。
また、隣接行列を用いた場合は、頂点uに隣接する頂点をO(|V|)で調べる。
これらの処理を|V|回行うため、O(|V**2)のアルゴリズムになる。
なお、このアルゴリズムは負の重みの辺を含むグラフには適用できないため、
その場合にはベルマンフォードのアルゴリズムやワーシャルフロイドのアルゴリズムを適用する。

入力例:
5
0 3 2 3 3 1 1 2
1 2 0 2 3 4
2 3 0 3 3 1 4 1
3 4 2 1 0 1 1 4 4 3
4 2 2 1 3 3

出力例:
0 0
1 2
2 2
3 1
4 3
*/
#include <iostream>
using namespace std;
static const int MAX = 100;
static const int INFTY = (1 << 21);
static const int WHITE = 0;
static const int GRAY = 1;
static const int BLACK = 2;

int n, M[MAX][MAX];

void dijkstra()
{
    int minv;
    int d[MAX], color[MAX];

    for (int i = 0; i < n; i++)
    {
        d[i] = INFTY;
        color[i] = WHITE;
    }

    d[0] = 0;
    color[0] = GRAY;
    while (1)
    {
        minv = INFTY;
        int u = -1;
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
                if (d[v] > (d[u] + M[u][v]))
                {
                    d[v] = d[u] + M[u][v];
                    color[v] = GRAY;
                }
            }
        }
    }

    for (int i = 0; i < n; i++)
    {
        cout << i << " " << (d[i] == INFTY ? -1 : d[i]) << endl;
    }
}

int main()
{
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            M[i][j] = INFTY;
        }
    }

    int k, c, u, v;
    for (int i = 0; i < n; i++)
    {
        cin >> u >> k;
        for (int j = 0; j < k; j++)
        {
            cin >> v >> c;
            M[u][v] = c;
        }
    }

    dijkstra();

    return 0;
}