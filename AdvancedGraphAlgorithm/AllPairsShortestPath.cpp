/*
全点対間最短経路(APSP)
重み付き有向グラフG=(V,E)の全点対間最短経路の距離を列挙する
負の閉路(その閉路を成す辺の重みの合計が負となっている閉路)が存在する場合、NEGATIVE CYCLEと出力。

入力例1：
4 6
0 1 1
0 2 5
1 2 2
1 3 4
2 3 1
3 2 7

出力例1：
0 1 3 4
INF 0 2 3
INF INF 0 1
INF INF 7 0

入力例2：
4 6
0 1 1
0 2 -5
1 2 2
1 3 4
2 3 1
3 2 7

出力例2：
0 1 -5 -4
INF 0 2 3
INF INF 0 1
INF INF 7 0

入力例3：
4 6
0 1 1
0 2 5
1 2 2
1 3 4
2 3 1
3 2 -7

出力例3：
NEGATIVE CYCLE
*/
#include <iostream>
#include <algorithm>
#include <vector>
#include <climits>
using namespace std;

static const int MAX = 100;
static const long long INFTY = (1LL << 32);

int n;
long long d[MAX][MAX];

void floyd()
{
    for (int k = 0; k < n; k++)
    {
        for (int i = 0; i < n; i++)
        {
            if (d[i][k] == INFTY)
            {
                continue;
            }
            for (int j = 0; j < n; j++)
            {
                if (d[k][j] == INFTY)
                {
                    continue;
                }
                d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
            }
        }
    }
}

int main()
{
    int e, u, v, c;
    cin >> n >> e;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            d[i][j] = ((i == j) ? 0 : INFTY);
        }
    }

    for (int i = 0; i < e; i++)
    {
        cin >> u >> v >> c;
        d[u][v] = c;
    }

    floyd();

    bool negative = false;
    for (int i = 0; i < n; i++)
    {
        if (d[i][i] < 0)
        {
            negative = true;
        }
    }

    if (negative)
    {
        cout << "NEGATIVE CYCLE" << endl;
    }
    else
    {
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (j)
                {
                    cout << " ";
                }
                if (d[i][j] == INFTY)
                {
                    cout << "INF";
                }
                else
                {
                    cout << d[i][j];
                }
            }
            cout << endl;
        }
    }
}