


# ワーシャル–フロイド法（Warshall–Floyd Algorithm）

## 概要
**ワーシャル–フロイド法**は、全点対間最短路（APSP: All-Pairs Shortest Path）を求めるアルゴリズム。
負辺も扱えるが、負閉路がある場合は最短距離が定義できない。

- 対象: 有向／無向、重み付き（負辺可、負閉路検出可）
- 計算量: **O(N^3)**（N=頂点数）

---

## アルゴリズムの流れ
1. 距離行列 `dist` を初期化
   - `dist[i][i] = 0`
   - 辺 (u,v) がある場合は `dist[u][v] = cost`
   - それ以外は `INF`
2. 3重ループで中間点 k を固定し、全ペア (i,j) の距離を更新

更新式：
$$
\text{dist}[i][j] = \min(\text{dist}[i][j],\ \text{dist}[i][k] + \text{dist}[k][j])
$$

---

## 実装例（Python）

```python
import sys
input = sys.stdin.readline

def LMI():
    return list(map(int, input().split()))

n, m = LMI()
INF = 10**18
dist = [[INF] * n for _ in range(n)]
for i in range(n):
    dist[i][i] = 0

for _ in range(m):
    u, v, c = LMI()
    u -= 1; v -= 1
    dist[u][v] = min(dist[u][v], c)  # 複数辺対策
    # 無向なら dist[v][u] も更新

for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][k] == INF or dist[k][j] == INF:
                continue
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
```

---

## 負閉路検出

```python
has_neg_cycle = False
for v in range(n):
    if dist[v][v] < 0:
        has_neg_cycle = True
        break
```

---

## 計算量
- O(N^3) と重く、大きな N では実用不可
- N ≈ 400 程度までが現実的（10^8 操作程度）

---

## 注意点
- 複数辺がある場合は初期化時に最小コストを設定
- 無向グラフなら対称成分も初期化
- 負閉路がある場合、最短距離は定義不能（影響範囲は -∞ とみなす）

---

## 応用
- 経路復元: `next` 行列を用いることで可能
- 最小巡回路（TSP）の前処理
- 任意2点間の距離クエリ高速化（静的グラフ）