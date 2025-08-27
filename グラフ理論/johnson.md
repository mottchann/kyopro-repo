


# ジョンソン法（Johnson's Algorithm）

## 概要
**ジョンソン法**は、全点対間最短路（APSP）を **負辺を含むグラフ** に対して効率的に求めるアルゴリズム。

- 対象: 有向／無向、重み付き（負辺可、負閉路不可）
- 計算量:
  - ダイクストラ法併用で **O(N M log N)**（ヒープ使用）
  - N: 頂点数, M: 辺数

---

## アルゴリズムの流れ
1. **新しい頂点 q** を追加し、全頂点への辺 (q → v) を重み 0 で追加
2. **ベルマン–フォード法**で q から各頂点への距離 `h[v]` を計算
   - 負閉路があれば終了（APSP 不可能）
3. 各辺 (u,v,w) の重みを再重み付け：
   $$ w' = w + h[u] - h[v] $$
   これにより負辺がなくなる
4. 各頂点を始点として **ダイクストラ法**を実行し、再重み付け後の最短距離を求める
5. 再重み付けを元に戻して元の距離を得る：
   $$ d_{uv} = d'_{uv} - h[u] + h[v] $$

---

## 実装例（Python）

```python
import heapq
import sys
input = sys.stdin.readline

def LMI():
    return list(map(int, input().split()))

n, m = LMI()
edges = []
G = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = LMI()
    u -= 1; v -= 1
    edges.append((u, v, w))
    G[u].append((v, w))

# 1. 仮想頂点 q を追加（index = n）
INF = 10**18
h = [INF] * (n + 1)
h[n] = 0
edges_bf = edges + [(n, v, 0) for v in range(n)]

# 2. ベルマン–フォードで h を求める
for _ in range(n):
    updated = False
    for u, v, w in edges_bf:
        if h[u] != INF and h[v] > h[u] + w:
            h[v] = h[u] + w
            updated = True
    if not updated:
        break
else:
    # N回目でも更新あり → 負閉路
    print("Negative cycle detected")
    sys.exit()

# 3. 再重み付け
new_G = [[] for _ in range(n)]
for u, v, w in edges:
    new_w = w + h[u] - h[v]
    new_G[u].append((v, new_w))

# 4. 各頂点を始点にダイクストラ
all_dist = [[INF] * n for _ in range(n)]
for s in range(n):
    dist = [INF] * n
    dist[s] = 0
    pq = [(0, s)]
    while pq:
        d, v = heapq.heappop(pq)
        if d > dist[v]:
            continue
        for to, cost in new_G[v]:
            nd = d + cost
            if nd < dist[to]:
                dist[to] = nd
                heapq.heappush(pq, (nd, to))
    # 5. 元の距離に戻す
    for t in range(n):
        if dist[t] < INF:
            all_dist[s][t] = dist[t] - h[s] + h[t]
```

---

## 計算量
- ベルマン–フォード: O(NM)
- ダイクストラ×N: O(N M log N)
- 疎グラフではワーシャル–フロイドより高速（N ≈ 1000, M ≈ 10000 程度でも実用的）

---

## 注意点
- 負閉路がある場合は利用不可
- 無向グラフで負辺がある場合は必ず負閉路が発生する

---

## 応用
- 大規模グラフでの全点対間最短路計算
- 差分制約系の解法（全点間版）