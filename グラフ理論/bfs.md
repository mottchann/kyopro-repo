


# 幅優先探索（BFS: Breadth-First Search）

## 概要
**幅優先探索**は、グラフ探索の基本アルゴリズムの1つで、始点からの距離が近い順に探索を進める手法。
- 探索順序: **階層的（レベル順）**
- 使用データ構造: **キュー（FIFO）**
- 無向グラフ、有向グラフいずれにも対応

---

## 特徴
- 最短経路: **辺の重みがすべて等しい**（例: 重みなしグラフ）場合、BFSで最短距離が求まる
- 全頂点を訪問可能（連結成分の特定にも使える）
- 深さ優先探索（DFS）よりも探索順が予測しやすい

---

## 計算量
- 時間計算量: **O(N + M)**（N=頂点数, M=辺数）
- 空間計算量: **O(N)**（訪問管理 + キュー）

---

## 実装例（Python, 無向グラフの最短距離）

```python
from collections import deque
import sys
input = sys.stdin.readline

def LMI():
    return list(map(int, input().split()))

n, m = LMI()
G = [[] for _ in range(n)]
for _ in range(m):
    u, v = LMI()
    u -= 1; v -= 1
    G[u].append(v)
    G[v].append(u)  # 無向グラフ

INF = 10**9
dist = [INF] * n
q = deque()

start = 0
q.append(start)
dist[start] = 0

while q:
    u = q.popleft()
    for v in G[u]:
        if dist[v] == INF:
            dist[v] = dist[u] + 1
            q.append(v)

print(dist)
```

---

## 典型用途
- 無向グラフ・有向グラフでの最短距離計算（重みなし）
- 迷路探索
- 最小ステップ数の計算（パズル、状態遷移）
- 多源BFS（複数始点からの同時探索）

---

## 亜種
- **多源BFS**: 複数の始点を同時にキューに入れて探索開始
- **01-BFS**: 辺の重みが0か1の場合にdequeを使い分けて高速化
- **双方向BFS**: 始点と終点から同時に探索して探索範囲を縮小