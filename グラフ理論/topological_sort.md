


# トポロジカルソート（Topological Sort）

## 概要
**トポロジカルソート**は、有向非巡回グラフ（DAG: Directed Acyclic Graph）の頂点を、すべての辺 (u → v) が u が v より前に来るように並べる手法。

- 対象: 有向グラフ（DAGのみ）
- 計算量: **O(N + M)**（N=頂点数, M=辺数）
- 代表的な実装方法: **Kahnのアルゴリズム**、**DFSベース**

---

## アルゴリズムの流れ（Kahnのアルゴリズム）
1. 各頂点の入次数（in-degree）を数える
2. 入次数が0の頂点をキューに入れる
3. キューから頂点を取り出し、結果リストに追加
4. その頂点から出る辺を削除（行き先の頂点の入次数を1減らす）
5. 入次数が0になった頂点をキューに追加
6. キューが空になるまで3〜5を繰り返す

---

## 実装例（Kahnのアルゴリズム, Python）

```python
from collections import deque
import sys
input = sys.stdin.readline

def LMI():
    return list(map(int, input().split()))

n, m = LMI()
G = [[] for _ in range(n)]
indeg = [0] * n
for _ in range(m):
    u, v = LMI()
    u -= 1; v -= 1
    G[u].append(v)
    indeg[v] += 1

q = deque([i for i in range(n) if indeg[i] == 0])
order = []

while q:
    u = q.popleft()
    order.append(u)
    for v in G[u]:
        indeg[v] -= 1
        if indeg[v] == 0:
            q.append(v)

# order にトポロジカル順序が格納される
if len(order) != n:
    print("グラフに閉路が存在します")
else:
    print(order)
```

---

## 実装例（DFSベース, Python）

```python
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def LMI():
    return list(map(int, input().split()))

n, m = LMI()
G = [[] for _ in range(n)]
for _ in range(m):
    u, v = LMI()
    u -= 1; v -= 1
    G[u].append(v)

visited = [0] * n  # 0=未訪問, 1=探索中, 2=完了
order = []

cycle = False

def dfs(u):
    global cycle
    visited[u] = 1
    for v in G[u]:
        if visited[v] == 0:
            dfs(v)
        elif visited[v] == 1:
            cycle = True
    visited[u] = 2
    order.append(u)

for i in range(n):
    if visited[i] == 0:
        dfs(i)

if cycle:
    print("グラフに閉路が存在します")
else:
    order.reverse()
    print(order)
```

---

## 注意点
- DAG以外ではトポロジカルソートはできない（閉路があると不可能）
- 入次数法はBFS的、DFS法は帰りがけ順を利用

---

## 応用
- 依存関係解決（ビルド順、タスク順序）
- DAG上の最長経路・動的計画法