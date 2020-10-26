/*
木の直径
非負の重みを持つ無向の木Tの直径を求める。木の最遠接点間の距離を木の直径とする。
入力例:
4
0 1 2
1 2 1
1 3 3
出力例:
5
*/
#include <iostream>
#include <queue>
#include <vector>
using namespace std;
#define MAX 100000
#define INFTY (1 << 30)

class Edge
{
public:
    int t, w;
    Edge() {}
    Edge(int t, int w) : t(t), w(w) {}
};

vector<Edge> G[MAX];
int n, d[MAX];

bool vis[MAX];
int cnt;

void bfs(int s)
{
    for (int i = 0; i < n; i++)
    {
        d[i] = INFTY;
    }
    queue<int> Q;
    Q.push(s);
    d[s] = 0;
    int u;
    while (!Q.empty())
    {
        u = Q.front();
        Q.pop();
        for (int i = 0; i < G[u].size(); i++)
        {
            Edge e = G[u][i];
            if (d[e.t] == INFTY)
            {
                d[e.t] = d[u] + e.w;
                Q.push(e.t);
            }
        }
    }
}

void solve()
{
    //適当な視点sから最も遠い節点tgtを求める
    bfs(0);
    int maxv = 0;
    int tgt = 0;
    for (int i = 0; i < n; i++)
    {
        if (d[i] == INFTY)
        {
            continue;
        }
        if (maxv < d[i])
        {
            maxv = d[i];
            tgt = i;
        }
    }

    //tgtから最も遠い節点の距離maxvを求める
    bfs(tgt);
    maxv = 0;
    for (int i = 0; i < n; i++)
    {
        if (d[i] == INFTY)
        {
            continue;
        }
        maxv = max(maxv, d[i]);
    }

    cout << maxv << endl;
}

int main()
{
    int s, t, w;
    cin >> n;

    for (int i = 0; i < n - 1; i++)
    {
        cin >> s >> t >> w;

        G[s].push_back(Edge(t, w));
        G[t].push_back(Edge(s, w));
    }

    solve();

    return 0;
}
