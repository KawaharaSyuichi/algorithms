/*
DSL_2_A：P.334
要素の値が動的に変化する数列に対して、指定された範囲内の最小の要素を高速に求める

問題URL：https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_A
解法参考URL：https://tjkendev.github.io/procon-library/cpp/range_query/rmq_segment_tree.html
*/

/*
実装する機能
update(i,x)：a(i)をxに変更
find(s,t)：a(s),a(s+1),...,a(t)の最小値を出力
ただし、すべての要素は2^(31)-1で初期化

入力形式:
n q
com0 x0 y0
com1 x1 y1
...
comq−1 x(q−1) y(q−1)

１行目にAの要素数n, クエリの数qが与えられる。続くq行にクエリが与えられる。comは、クエリの種類を示し、'0'がquery(xi,yi)、'1'がfind(xi,yi)を表す。


入力例1:
3 5
0 0 1
0 1 2
0 2 3
1 0 2
1 1 2

出力例1:
1
2

入力例2:
1 3
1 0 0
0 0 5
1 0 0

出力例:
2147483647
5
*/
#include <iostream>
#include <algorithm>
using namespace std;
using ll = long long;

#define N 100007

class SegmentTree
{
    const static ll inf = (1LL << 31) - 1;
    int n, n0;
    ll data[4 * N];

public:
    SegmentTree(int n)
    {
        n0 = 1;
        while (n0 < n)
            n0 <<= 1;
        for (int i = 0; i < 2 * n0; ++i)
            data[i] = inf;
    }

    void update(int k, ll x)
    {
        k += n0 - 1;
        data[k] = x;
        while (k > 0)
        {
            k = (k - 1) / 2;
            data[k] = min(data[2 * k + 1], data[2 * k + 2]);
        }
    }

    ll query(int l, int r)
    {
        int l0 = l + n0, r0 = r + n0;
        ll s = inf;
        while (l0 < r0)
        {
            if (r0 & 1)
            {
                --r0;
                s = min(s, data[r0 - 1]);
            }
            if (l0 & 1)
            {
                s = min(s, data[l0 - 1]);
                ++l0;
            }
            l0 >>= 1;
            r0 >>= 1;
        }
        return s;
    }
};

int n, q;

int main()
{
    cin >> n >> q;
    SegmentTree st(n);

    for (int i = 0; i < q; i++)
    {
        int t, x, y;
        cin >> t >> x >> y;

        if (t == 0)
        {
            st.update(x, y);
        }
        else
        {
            cout << st.query(x, y + 1) << endl;
        }
    }

    return 0;
}