/*連結成分
グラフの連結成分を求める。
エッジの数が少ない疎なグラフでは、隣接リストによる表現が適している。

入力例:
10 9
0 1
0 2
3 4
5 7
5 6
6 7
6 8
7 8
8 9
3
0 1
5 9
1 3

出力例:
yes
yes
no
*/
#include <iostream>
#include <vector>
#include <stack>
using namespace std;
static const int MAX = 100000;
static const int NIL = -1;

int n;
vector<int> G[MAX];
int color[MAX];

void dfs(int r, int c) //深さ優先探索
{
    stack<int> S;
    S.push(r);
    color[r] = c;

    while (!S.empty())
    {
        int u = S.top();
        S.pop();
        for (int i = 0; i < G[u].size(); i++)
        {
            int v = G[u][i];
            if (color[v] == NIL)
            {
                color[v] = c;
                S.push(v);
            }
        }
    }
}

void assignColor()
{
    int id = 1;
    for (int i = 0; i < n; i++)
    {
        color[i] = NIL;
    }
    for (int u = 0; u < n; u++)
    {
        if (color[u] == NIL)
        {
            dfs(u, id++);
        }
    }
}

int main()
{
    int s, t, m, q;

    cin >> n >> m;

    for (int i = 0; i < m; i++)
    {
        cin >> s >> t;
        G[s].push_back(t);
        G[t].push_back(s);
    }

    assignColor();

    cin >> q;

    for (int i = 0; i < q; i++)
    {
        cin >> s >> t;
        if (color[s] == color[t])
        {
            cout << "yes" << endl;
        }
        else
        {
            cout << "no" << endl;
        }
    }
    return 0;
}