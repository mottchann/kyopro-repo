

# SPFA（Shortest Path Faster Algorithm）

## 概要
**SPFA** は Bellman–Ford 法をキューを使って高速化したアルゴリズム。
平均計算量は O(M) に近くなることもあるが、最悪計算量は **O(NM)** で Bellman–Ford と同じ。

- 対象: 有向／無向、重み付き（負辺可）
- 負閉路検出可能
- 実用上はグラフが疎かつ負辺が少ない場合に有効

---

## アルゴリズムの流れ
1. 始点の距離を 0、他を ∞ に初期化
2. キューに始点を入れる
3. キューから頂点を取り出し、そこからの全辺を緩和
4. 更新があれば、その頂点をキューに入れる（未登録時のみ）
5. キューが空になるまで繰り返す

Bellman–Ford との違い：
- 更新があった頂点のみ再処理するため、平均的に高速

---

## 実装例（Python）

```python
from collections import deque
import sys
input = sys.stdin.readline

def LMI():
    return list(map(int, input().split()))

n, m = LMI()
G = [[] for _ in range(n)]  # (to, cost)
for _ in range(m):
    u, v, c = LMI()
    u -= 1; v -= 1
    G[u].append((v, c))
    # 無向なら G[v].append((u, c)) も追加

[s] = LMI(); s -= 1
INF = 10**18
dist = [INF] * n
in_queue = [False] * n
count = [0] * n  # 緩和回数（負閉路検出用）

q = deque()
dist[s] = 0
q.append(s)
in_queue[s] = True

neg_cycle = False
while q:
    v = q.popleft()
    in_queue[v] = False
    for to, cost in G[v]:
        if dist[to] > dist[v] + cost:
            dist[to] = dist[v] + cost
            count[to] += 1
            if count[to] >= n:
                neg_cycle = True
                break
            if not in_queue[to]:
                q.append(to)
                in_queue[to] = True
    if neg_cycle:
        break
```

---

## 負閉路検出
上記実装の `count[to] >= n` 判定で、負閉路に到達可能かを検出できる。

---

## 計算量
- 平均: O(M) に近い（疎グラフで有効）
- 最悪: O(NM)（密グラフや特定ケースで遅くなる）

---

## 注意点
- 無向グラフで負辺がある場合、必ず負閉路が存在する
- ダイクストラ法より遅い場合も多く、用途は限定的

---

## 応用
- 負辺を含む単一始点最短路の高速化
- 負閉路検出