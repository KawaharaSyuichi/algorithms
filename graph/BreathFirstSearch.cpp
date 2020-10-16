/*
幅優先探索(BFS)

幅優先探索は以下のアルゴリズムに従い、各頂点vについてsからの距離をd[v]に記録します。
1. 始点sをキューQに入れる(訪問する)。
2. Qが空でない限り以下の処理を繰り返す:
　a. Qから頂点uを取り出し訪問する(訪問完了)。
　b. uに隣接し未訪問の頂点vについてd[v]をd[u]+1と更新し、vをQに入れる。

隣接行列を用いた幅優先探索は、各頂点について全ての頂点に隣接しているかどうかを調べるため、O(|V|**2)のアルゴリズムとなり、大きなグラフに対しては適当ではない。

幅優先探索に用いる主な変数
・color[n]:頂点iの訪問状態をWHITE,GRAY,BLACKのいずれかで表す
・M[n][n]:頂点iから頂点jに辺がある場合M[i][j]がtrueとなるような隣接行列
・Queue Q:次に訪問するべき頂点を記録しておくキュー
・d[n]:始点sから各頂点iまでの最短距離をd[i]に記録しておく。sからiへ到達不可能な場合はd[i]にINFTY(大きな値)とする。


入力例:
4
1 2 2 4
2 1 4
3 0
4 1 3

出力例:
1 0
2 1
3 2
4 1
*/

#include <iostream>
#include <queue>

using namespace std;
static const int N = 100;
static const int INFTY = (1 << 21);

int n, M[N][N];
int d[N]; //距離で訪問状態(color)を管理する

void bfs(int s)
{
    queue<int> q; //標準ライブラリのqueueを使用
    q.push(s);
    for (int i = 0; i < n; i++)
    {
        d[i] = INFTY;
    }
    d[s] = 0;
    int u;
    while (!q.empty())
    {
        u = q.front();
        q.pop();
        for (int v = 0; v < n; v++)
        {
            if (M[u][v] == 0)
            {
                continue;
            }
            if (d[v] != INFTY) //すでに他の頂点が探索済み
            {
                continue;
            }
            d[v] = d[u] + 1;
            q.push(v);
        }
    }

    for (int i = 0; i < n; i++)
    {
        cout << i + 1 << " " << ((d[i] == INFTY) ? (-1) : d[i]) << endl;
    }
}

int main()
{
    int u, k, v;

    cin >> n;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            M[i][j] = 0;
        }
    }

    for (int i = 0; i < n; i++)
    {
        cin >> u >> k;
        u--;
        for (int j = 0; j < k; j++)
        {
            cin >> v;
            v--;
            M[u][v] = 1;
        }
    }

    bfs(0);
    return 0;
}