


# 深さ優先探索（DFS: Depth-First Search）

## 概要
**深さ優先探索**は、グラフ探索の基本手法の一つで、可能な限り深く進み、行き止まりに到達したら直前の分岐まで戻って探索を続ける方法。
- 使用データ構造: **再帰呼び出し（スタック）** または 明示的な **スタック**
- 無向グラフ、有向グラフどちらにも対応

---

## 特徴
- 実装が簡単（特に再帰版）
- 到達可能な全頂点を訪問可能
- 探索の順番はBFSと異なり、深く潜る順になる

---

## 再帰版と反復版
### 再帰版（Python例）
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
    G[v].append(u)  # 無向グラフ

visited = [False] * n

def dfs(u):
    visited[u] = True
    for v in G[u]:
        if not visited[v]:
            dfs(v)

dfs(0)  # 頂点0から探索
```

### 反復版（スタック使用）
```python
from collections import deque

def dfs_iter(start):
    stack = deque([start])
    visited[start] = True
    while stack:
        u = stack.pop()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                stack.append(v)
```

---

## 行きがけ順と帰りがけ順
- **行きがけ順**: 頂点に初めて到達した時点で処理（前順処理）
- **帰りがけ順**: すべての隣接頂点の探索が終わった後で処理（後順処理）

これにより、様々なアルゴリズム（トポロジカルソート、橋・関節点検出など）が実装可能。

---

## 計算量
- 時間計算量: **O(N + M)**（N=頂点数, M=辺数）
- 空間計算量: **O(N)**（訪問配列 + 再帰スタック）

---

## 用途
- グラフの連結成分分解
- トポロジカルソート（DAG）
- サイクル検出
- 二部グラフ判定
- 橋・関節点検出（Low-Link法）
- 木DPや部分木サイズ計算