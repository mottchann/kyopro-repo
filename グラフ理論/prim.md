


# プリム法（Prim's Algorithm）

## 概要
**プリム法**は、**最小全域木（MST: Minimum Spanning Tree）** を求めるアルゴリズムの1つで、頂点集合を広げながら辺を追加していく手法。

- 対象: 無向グラフ、重み付き（非負）
- 計算量:
  - ヒープ使用: **O(M log N)**（疎グラフで高速）
  - 配列のみ: **O(N^2)**（密グラフ向き）

---

## アルゴリズムの流れ
1. 任意の始点を選び、MST に追加
2. その時点で MST に含まれる頂点と、含まれない頂点を結ぶ最小コストの辺を選択
3. 選んだ辺を MST に追加し、頂点集合を拡大
4. 全頂点が含まれるまで繰り返す

---

## 実装例（ヒープ使用, Python）

```python
import heapq
import sys
input = sys.stdin.readline

def LMI():
    return list(map(int, input().split()))

n, m = LMI()
G = [[] for _ in range(n)]  # (コスト, 行き先)
for _ in range(m):
    u, v, w = LMI()
    u -= 1; v -= 1
    G[u].append((w, v))
    G[v].append((w, u))  # 無向

visited = [False] * n
pq = []

# 始点は0
visited[0] = True
for cost, to in G[0]:
    heapq.heappush(pq, (cost, to))

mst_cost = 0
mst_edges = []

while pq and len(mst_edges) < n - 1:
    cost, v = heapq.heappop(pq)
    if visited[v]:
        continue
    visited[v] = True
    mst_cost += cost
    mst_edges.append(cost)
    for nc, to in G[v]:
        if not visited[to]:
            heapq.heappush(pq, (nc, to))

# mst_cost: MST の総コスト
# mst_edges: MST に含まれる辺コストのリスト
```

---

## 実装例（配列版, Python, O(N^2)）

```python
import sys
input = sys.stdin.readline

def LMI():
    return list(map(int, input().split()))

n, m = LMI()
INF = 10**18
dist = [[INF] * n for _ in range(n)]
for _ in range(m):
    u, v, w = LMI()
    u -= 1; v -= 1
    dist[u][v] = min(dist[u][v], w)
    dist[v][u] = min(dist[v][u], w)

used = [False] * n
mincost = [INF] * n
mincost[0] = 0
mst_cost = 0

for _ in range(n):
    v = -1
    for u in range(n):
        if not used[u] and (v == -1 or mincost[u] < mincost[v]):
            v = u
    if mincost[v] == INF:
        break
    used[v] = True
    mst_cost += mincost[v]
    for u in range(n):
        if not used[u] and dist[v][u] < mincost[u]:
            mincost[u] = dist[v][u]
```

---

## 計算量
- ヒープ使用: O(M log N)（疎グラフ向き）
- 配列版: O(N^2)（密グラフ向き）

---

## 注意点
- 無向グラフ専用
- グラフが非連結の場合、MST ではなく**最小全域森**になる

---

## 応用
- 最大全域木（辺の符号反転）
- 部分グラフからの MST 拡張