


# ダイクストラ法（Dijkstra's Algorithm）

## 概要
**ダイクストラ法**は、辺重みが **非負** のグラフにおける単一始点最短路（SSSP: Single Source Shortest Path）を求めるアルゴリズム。
優先度付きキュー（ヒープ）を用いることで **O((N+M) log N)** の計算量で動作する。

- 対象: 有向／無向、重み付き（非負）
- 出力: 始点から各頂点への最短距離、（必要なら）経路復元用の親配列
- 負辺が存在する場合は誤動作 → ベルマン–フォード法などを使う

---

## アルゴリズムの流れ
1. 始点の距離を 0、他の距離を ∞ で初期化。
2. ヒープに `(距離, 頂点)` を入れる。
3. ヒープから距離が最小の頂点を取り出す。
4. その頂点から行ける隣接頂点を調べ、**緩和（Relaxation）** を行う。
5. 更新があればヒープに新しい `(距離, 頂点)` を push。
6. ヒープが空になるまで繰り返す。

---

## 実装例（Python）

```python
import heapq
import sys
input = sys.stdin.readline

def LMI():
    return list(map(int, input().split()))

n, m = LMI()
G = [[] for _ in range(n)]  # (隣接頂点, コスト)
for _ in range(m):
    u, v, c = LMI()
    u -= 1; v -= 1
    G[u].append((v, c))
    # 無向なら G[v].append((u, c)) も追加

[s] = LMI(); s -= 1
INF = 10**18
dist = [INF] * n
par = [-1] * n  # 経路復元用

dist[s] = 0
pq = [(0, s)]  # (距離, 頂点)
while pq:
    d, v = heapq.heappop(pq)
    if d > dist[v]:
        continue
    for to, cost in G[v]:
        nd = d + cost
        if nd < dist[to]:
            dist[to] = nd
            par[to] = v
            heapq.heappush(pq, (nd, to))
```

---

## 経路復元

```python
def get_path(t):
    if dist[t] == INF:
        return []  # 到達不可
    path = []
    cur = t
    while cur != -1:
        path.append(cur + 1)  # 1-index に戻す
        cur = par[cur]
    path.reverse()
    return path
```

---

## 計算量
- ヒープ使用: **O((N+M) log N)**
- ヒープなし（隣接行列）: **O(N^2)**
- N: 頂点数、M: 辺数

---

## 注意点
- 負辺がある場合は使用不可（距離が無限ループで減少する可能性あり）
- 到達不可頂点は距離が INF のまま
- 無向グラフの場合は双方向に辺を追加

---

## 応用
- **多始点ダイクストラ**: 複数の始点を距離0でキューに入れて同時探索
- **経路復元**: `par` 配列を使って逆順に辿る
- **経路数計算**: 最短距離DPと組み合わせて経路数を数える