

# ベルマン–フォード法（Bellman–Ford Algorithm）

## 概要
**ベルマン–フォード法**は、単一始点最短路（SSSP）を求めるアルゴリズムで、**負辺を含むグラフにも対応**可能。

- 対象: 有向／無向、重み付き（負辺可）
- 計算量: **O(NM)**（N=頂点数, M=辺数）
- 負閉路（Negative Cycle）の検出も可能

---

## アルゴリズムの流れ
1. 始点の距離を 0、他の距離を ∞ で初期化。
2. N-1 回のループで全辺を走査し、緩和（Relaxation）を行う。
3. N 回目のループで更新があれば、負閉路が存在すると判定。

---

## 実装例（Python）

```python
import sys
input = sys.stdin.readline

def LMI():
    return list(map(int, input().split()))

n, m = LMI()
edges = []
for _ in range(m):
    u, v, c = LMI()
    u -= 1; v -= 1
    edges.append((u, v, c))

[s] = LMI(); s -= 1
INF = 10**18
dist = [INF] * n
dist[s] = 0

# N-1 回の緩和
for _ in range(n - 1):
    updated = False
    for u, v, cost in edges:
        if dist[u] != INF and dist[v] > dist[u] + cost:
            dist[v] = dist[u] + cost
            updated = True
    if not updated:
        break

# 負閉路検出
neg_cycle = False
for u, v, cost in edges:
    if dist[u] != INF and dist[v] > dist[u] + cost:
        neg_cycle = True
        break
```

---

## 負閉路の影響範囲特定
負閉路に到達可能な頂点、または負閉路から到達可能な頂点は「距離が -∞ とみなされる」。

```python
# N 回目でも更新された頂点を記録
neg_nodes = set()
for u, v, cost in edges:
    if dist[u] != INF and dist[v] > dist[u] + cost:
        neg_nodes.add(v)

# 負閉路影響範囲を BFS / DFS で拡張可能
```

---

## 計算量
- O(NM) と重い → M が多い場合や N が大きい場合は注意
- 負辺がなければダイクストラ法の方が高速

---

## 注意点
- 無向グラフに負辺がある場合は、負閉路が必ず存在する（その辺を往復するだけで距離が減少する）
- 負閉路がある場合は「最短距離が定義できない」ため、問題文に応じた対応が必要

---

## 応用
- 負閉路検出
- 最短経路木の構築（負閉路がない場合）
- 差分制約系の解法（系: Bellman–Ford で可否判定）