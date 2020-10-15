/*
深さ優先探索(DFS)

深さ優先探索では、スタックを用いて「まだ探索中の頂点」を一時的に保持。
スタックを用いた深さ優先探索のアルゴリズムは以下の通り。
1.一番最初に訪問する頂点をスタックに入れる
2.スタックに頂点が積まれている限り、以下の処理を繰り返す。
 a.スタックのトップにある頂点uを訪問
 b.現在訪問中の頂点uから次の頂点vへ移動するときに、vをスタックに入れる
   ただし、現在訪問中の頂点uに未訪問の隣接する頂点がなければuをスタックから削除する


入力例:
6
1 2 2 3
2 2 3 4
3 1 5
4 1 6
5 1 6
6 0

出力例:
1 1 12
2 2 11
3 3 8
4 9 10
5 4 7
6 5 6
*/
#include <iostream>
#include <stack>
using namespace std;
static const int N = 100;
static const int WHITE = 0;
static const int GRAY = 1;
static const int BLACK = 2;

int n, M[N][N];
int color[N], d[N], f[N], tt;
int nt[N];

int next(int u) //uに隣接するvを番号順に取得
{
    for (int v = nt[u]; v < n; v++)
    {
        nt[u] = v + 1;
        if (M[u][v])
        {
            return v;
        }
    }
    return -1;
}

void dfs_visit(int r) //スタックを用いた深さ優先探索
{
    for (int i = 0; i < n; i++)
    {
        nt[i] = 0;
    }

    stack<int> S;
    S.push(r);
    color[r] = GRAY;
    d[r] = ++tt;

    while (!S.empty())
    {
        int u = S.top();
        int v = next(u);
        if (v != -1)
        {
            if (color[v] == WHITE)
            {
                color[v] = GRAY;
                d[v] = ++tt;
                S.push(v);
            }
        }
        else
        {
            S.pop();
            color[u] = BLACK;
            f[u] = ++tt;
        }
    }
}

void dfs()
{
    //初期化
    for (int i = 0; i < n; i++)
    {
        color[i] = WHITE;
        nt[i] = 0;
    }
    tt = 0;

    //未訪問のuを始点として深さ優先探索
    for (int u = 0; u < n; u++)
    {
        if (color[u] == WHITE)
        {
            dfs_visit(u);
        }
    }

    for (int i = 0; i < n; i++)
    {
        cout << i + 1 << " " << d[i] << " " << f[i] << endl;
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

    dfs();

    return 0;
}