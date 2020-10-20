/*
単一始点最短経路
与えられた重み付き有向グラフG=(V,E)について、単一始点最短経路のコストを求めるプログラム

ダイクストラのアルゴリズム(優先度付きキュー)
グラフG=(V,E)の頂点全体の集合をV、始点をs、最短経路木に含まれている頂点の集合をSとします。
各計算ステップで、最短経路木の辺と頂点を選びSへ追加します。
各頂点iについて、S内の頂点のみを経由したsからiへの最短経路のコストをd[i]、最短経路木におけるiの親をp[i]とする。
1.初期状態で、Sを空にする
 a. sに対してd[s]=0
 b. s意外のVに属する全ての頂点iに対してd[i]=∞
 c. d[i]をキーとして、Vの頂点をmin-ヒープHとして構築します。
2.以下の処理をS=Vとなるまで繰り返す
 a. Hからd[u]が最小である頂点uを取り出します。
 b. uをSに追加すると同時に、uに隣接しかつV-Sに属する全ての頂点vに対する値を以下のように更新
 if d[u]+w(u,v)<d[v]
    d[v]=d[u]+w(u,v)
    p[v]=u
    vを起点にヒープHを更新

隣接リストと優先度付きキューを用いた実装は、|V|の数だけキューから頂点が取り出され、|E|の数だけキューに挿入されるので、計算量はO((|V|+|E|)log|V|)

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
#include <algorithm>
#include <queue>
using namespace std;
static const int MAX = 10000;
static const int INFTY = (1 << 20);
static const int WHITE = 0;
static const int GRAY = 1;
static const int BLACK = 2;

int n;
vector<pair<int, int>> adj[MAX]; //重み付き有向グラフの隣接リスト表現

void dijkstra()
{
    priority_queue<pair<int, int>> PQ;
    int color[MAX];
    int d[MAX];
    for (int i = 0; i < n; i++)
    {
        d[i] = INFTY;
        color[i] = WHITE;
    }

    d[0] = 0;
    PQ.push(make_pair(0, 0));
    color[0] = GRAY;

    while (!PQ.empty())
    {
        pair<int, int> f = PQ.top();
        PQ.pop();
        int u = f.second;
        color[u] = BLACK;

        //最小値を取り出し、それが最短でなければ無視
        if (d[u] < f.first * (-1))
        {
            continue;
        }

        for (int j = 0; j < adj[u].size(); j++)
        {
            int v = adj[u][j].first;
            if (color[v] == BLACK)
            {
                continue;
            }
            if (d[v] > d[u] + adj[u][j].second)
            {
                d[v] = d[u] + adj[u][j].second;
                //priority_queueはデフォルトで大きい値を優先するため-1を掛ける
                PQ.push(make_pair(d[v] * (-1), v));
                color[v] = GRAY;
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
    int k, u, v, c;

    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> u >> k;
        for (int j = 0; j < k; j++)
        {
            cin >> v >> c;
            adj[u].push_back(make_pair(v, c));
        }
    }

    dijkstra();

    return 0;
}