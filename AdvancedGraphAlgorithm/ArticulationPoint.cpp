/*
関節点
連結グラフGにおいて、頂点uと、uから出ている全てのエッジを削除して得られる部分グラフが、非連結になるとき、頂点uをグラフGの関節点と言う。

入力点:
4 4
0 1
0 2
1 2
2 3

出力点:
2
*/
#include <iostream>
#include <vector>
#include <set>
using namespace std;

#define MAX 100000

vector<int> G[MAX];
int N;
bool visited[MAX];
/*
prenum[u]:Gの任意の頂点を始点としてDFSを行い、各頂点uの訪問の順番をprenum[u]に記録
parent[u]:DFSによって生成される木におけるuの親をparent[u]に記録
lowest[u]:各頂点uに対して、以下のうちの最小値としてlowest[u]を計算
 1. prenum[u]
 2. GのBackedge(u,v)が存在するとき、頂点vにおけるprenum[v]
    (Backedge(u,v)とは、頂点uからTに属する頂点vに向かうTに属さないGのエッジ)
 3. Tに属する頂点uのすべての子xに対するlowest[x]
 これらの変数を基に、関節点は以下のように決定する。
 1. Tのルートrが2つ以上の子供を持つとき,rは関節点
 2. 各頂点uにおいて、uの親parent[u]をpとすると、prenum[p]<=lowest[u]ならば、pは関節点。(pがルートの場合は1.を適用)
 　 これは頂点u,Tにおけるuの子孫から頂点pの祖先へのエッジがないことを示す。
*/
int prenum[MAX], parent[MAX], lowest[MAX], timer;

void dfs(int current, int prev)
{
    //ノードcurrentを訪問した直後の処理
    prenum[current] = lowest[current] = timer;
    timer++;

    visited[current] = true;

    int next;

    for (int i = 0; i < G[current].size(); i++)
    {
        next = G[current][i];
        if (!visited[next])
        {
            //ノードcurrentからノードnextへ訪問する直前の処理
            parent[next] = current;

            dfs(next, current);

            //ノードnextの探索が終了した直後の処理
            lowest[current] = min(lowest[current], lowest[next]);
        }
        else if (next != prev)
        {
            //エッジcurrent-->nextがBack-edgeの場合の処理
            lowest[current] = min(lowest[current], prenum[next]);
        }
    }
    //ノードcurretの探索が終了した直後の処理
}

void art_points()
{
    for (int i = 0; i < N; i++)
    {
        visited[i] = false;
    }
    timer = 1;
    //lowestの計算
    dfs(0, -1); //0==root

    set<int> ap;
    int np = 0;
    for (int i = 1; i < N; i++)
    {
        int p = parent[i];
        if (p == 0)
        {
            np++;
        }
        else if (prenum[p] <= lowest[i])
        {
            ap.insert(p);
        }
    }
    if (np > 1)
    {
        ap.insert(0);
    }
    for (set<int>::iterator it = ap.begin(); it != ap.end(); it++)
    {
        cout << *it << endl;
    }
}

int main()
{
    int m;
    cin >> N >> m;
    for (int i = 0; i < m; i++)
    {
        int s, t;
        cin >> s >> t;
        G[s].push_back(t);
        G[t].push_back(s);
    }
    art_points();

    return 0;
}