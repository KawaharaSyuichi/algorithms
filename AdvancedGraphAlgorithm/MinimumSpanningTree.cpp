/*
最小全域木(無向グラフ)
最小全域木の辺の重みの総和を出力

クラスカルのアルゴリズム
1. グラフG=(V,E)の辺eiを、重みの昇順に整列する
2. 最小全域木の辺の集合をKとし、それを空に初期化する
3. i=1,2,...,|E| の順番に、|K| が |V|-1 になるまで、K U {ei}が閉路を作らないようなeiをKに追加する

クラスカルのアルゴリズムでは、辺の整列に最も時間を要するのでO(|E|log|E|)のアルゴリズム

入力例:
6 9
0 1 1
0 2 3
1 2 1
1 3 7
2 4 1
1 4 3
3 4 1
3 5 1
4 5 6

出力例:
5
*/
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

#define MAX 10000
#define INFTY (1 << 29)

class DisjointSet
{
public:
    vector<int> rank, p;

    DisjointSet() {}
    DisjointSet(int size)
    {
        rank.resize(size, 0);
        p.resize(size, 0);
        for (int i = 0; i < size; i++)
        {
            makeSet(i);
        }
    }

    void makeSet(int x)
    {
        p[x] = x;
        rank[x] = 0;
    }

    bool same(int x, int y)
    {
        return findSet(x) == findSet(y);
    }

    void unite(int x, int y)
    {
        link(findSet(x), findSet(y));
    }

    void link(int x, int y)
    {
        if (rank[x] > rank[y])
        {
            p[y] = x;
        }
        else
        {
            p[x] = y;
            if (rank[x] == rank[y])
            {
                rank[y]++;
            }
        }
    }

    int findSet(int x)
    {
        if (x != p[x])
        {
            p[x] = findSet(p[x]);
        }
        return p[x];
    }
};

class Edge
{
public:
    int source, target, cost;
    Edge(int source = 0, int target = 0, int cost = 0) : source(source), target(target), cost(cost) {}
    bool operator<(const Edge &e) const
    {
        return cost < e.cost;
    }
};

int kruskal(int N, vector<Edge> edges)
{
    int totalCost = 0;
    sort(edges.begin(), edges.end());
    DisjointSet dset = DisjointSet(N + 1);

    for (int i = 0; i < N; i++)
    {
        dset.makeSet(i);
    }

    int source, target;
    for (int i = 0; i < edges.size(); i++)
    {
        Edge e = edges[i];
        if (!dset.same(e.source, e.target))
        {
            //MST.push_back(e);
            totalCost += e.cost;
            dset.unite(e.source, e.target);
        }
    }

    return totalCost;
}

int main()
{
    int N, M, cost;
    int source, target;

    cin >> N >> M;

    vector<Edge> edges;
    for (int i = 0; i < M; i++)
    {
        cin >> source >> target >> cost;
        edges.push_back(Edge(source, target, cost));
    }

    cout << kruskal(N, edges) << endl;

    return 0;
}