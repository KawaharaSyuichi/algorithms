/*
互いに素な集合

Disjoint Setsは、データを互いに素な集合に分類して管理するためのデータ構造。このデータ構造は、動的に以下の操作を効率的に処理する。
1. makeSet(x) : 要素がxただ1つである新しい集合を作る
2. findSet(x) : 要素xが属する集合の代表の要素を求める
3. unite(x,y) : 指定された2つの要素x,yを合併する

入力例:
5 12
0 1 4
0 2 3
1 1 2
1 3 4
1 1 4
1 3 2
0 1 3
1 2 4
1 3 0
0 0 4
1 0 2
1 3 0

出力例:
0
0
1
1
1
0
1
1
*/
#include <iostream>
#include <vector>

using namespace std;

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

int main()
{
    int n, a, b, q;
    int t;

    cin >> n >> q;
    DisjointSet ds = DisjointSet(n);

    for (int i = 0; i < q; i++)
    {
        cin >> t >> a >> b;
        if (t == 0)
        {
            ds.unite(a, b);
        }
        else if (t == 1)
        {
            if (ds.same(a, b))
            {
                cout << 1 << endl;
            }
            else
            {
                cout << 0 << endl;
            }
        }
    }

    return 0;
}