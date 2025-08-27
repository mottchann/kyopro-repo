


# ボルフカ法（Borůvka's Algorithm）

## 概要
**ボルフカ法**は、**最小全域木（MST: Minimum Spanning Tree）** を求める最古のアルゴリズムの1つで、各連結成分から最小コストの辺を一斉に追加していく手法。

- 対象: 無向グラフ、重み付き（非負）
- 計算量: **O(M log N)**（M=辺数, N=頂点数）
- データ構造: **Union-Find**

---

## アルゴリズムの流れ
1. 各頂点を別々の集合（Union-Find）にする
2. 各集合ごとに、外部に出る最小コストの辺を探す
3. それらの辺を一斉に MST に追加（Union 操作）
4. 集合数が1になるまで繰り返す

---

## 実装例（Python）

```python
import sys
input = sys.stdin.readline

def LMI():
    return list(map(int, input().split()))

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        return True

n, m = LMI()
edges = []
for _ in range(m):
    u, v, w = LMI()
    u -= 1; v -= 1
    edges.append((w, u, v))

uf = UnionFind(n)
mst_cost = 0
components = n

while components > 1:
    min_edge = [-1] * n  # 各集合の最小辺のインデックス
    for i, (w, u, v) in enumerate(edges):
        ru, rv = uf.find(u), uf.find(v)
        if ru == rv:
            continue
        if min_edge[ru] == -1 or edges[min_edge[ru]][0] > w:
            min_edge[ru] = i
        if min_edge[rv] == -1 or edges[min_edge[rv]][0] > w:
            min_edge[rv] = i

    for idx in min_edge:
        if idx != -1:
            w, u, v = edges[idx]
            if uf.unite(u, v):
                mst_cost += w
                components -= 1

print(mst_cost)
```

---

## 計算量
- 各ステップで少なくとも集合数が半減する
- 全体で O(M log N)

---

## 注意点
- 無向グラフ専用
- 複数の MST が存在する場合もある

---

## 応用
- 並列計算に向いている
- 大規模グラフでの分散処理MST構築