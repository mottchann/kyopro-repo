


# クラスカル法（Kruskal's Algorithm）

## 概要
**クラスカル法**は、**最小全域木（MST: Minimum Spanning Tree）** を求めるアルゴリズムの1つで、辺を重みの昇順に追加していく手法。

- 対象: 無向グラフ、重み付き（非負）
- 計算量: **O(M log M)**（M=辺数）
- データ構造: **Union-Find（Disjoint Set Union, DSU）** を使用

---

## アルゴリズムの流れ
1. 辺を重みの昇順にソート
2. Union-Find を初期化（全頂点が別集合）
3. 辺を順に見て、両端が異なる集合なら MST に追加（Union 操作）
4. N-1 本の辺が追加されたら終了

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
    def same(self, x, y):
        return self.find(x) == self.find(y)

n, m = LMI()
edges = []
for _ in range(m):
    u, v, w = LMI()
    u -= 1; v -= 1
    edges.append((w, u, v))

# 1. 重み順にソート
edges.sort()

uf = UnionFind(n)
mst_cost = 0
mst_edges = []

# 2. 辺を順に確認
for w, u, v in edges:
    if uf.unite(u, v):
        mst_cost += w
        mst_edges.append((u, v, w))
    if len(mst_edges) == n - 1:
        break

# mst_cost: 最小全域木の総コスト
# mst_edges: MSTに含まれる辺のリスト
```

---

## 計算量
- 辺のソート: **O(M log M)**
- Union-Find 操作: **O(α(N))**（ほぼ定数時間）
- 合計: **O(M log M)**

---

## 注意点
- 無向グラフ専用（有向の場合は MST 概念が異なる）
- 複数の MST が存在する場合もある（同コスト）
- グラフが非連結の場合、MST ではなく**最小全域森**になる

---

## 応用
- 最大全域木（辺を降順にソート）
- 最小全域木の唯一性判定
- クラスカル法＋Kruskal再構築法（第二最小全域木）