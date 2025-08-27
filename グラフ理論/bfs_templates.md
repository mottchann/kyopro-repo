
# BFS 入出力テンプレート集（Python）

競技プログラミングで頻出の **BFS（幅優先探索）** を、典型的な入出力パターンごとに最小構成でまとめます。
入力は **1-indexed** を想定し、コード内では **0-indexed** に変換します。

まずは便利関数とお約束の import：

```python
from collections import deque
import sys
input = sys.stdin.readline

def LMI():
    """空白区切り整数をリストで返すショートハンド"""
    return list(map(int, input().split()))
```

---

## 1. 無向グラフ（重みなし）— 単一始点 BFS（距離と経路復元）

```python
n, m = LMI()
G = [[] for _ in range(n)]
for _ in range(m):
    u, v = LMI()
    u -= 1; v -= 1  # 0-index
    G[u].append(v)
    G[v].append(u)

# 始点 s を 1-index で受け取り 0-index 化する想定（固定で 1 始点なら s = 0 でOK）
[s] = LMI()
s -= 1

dist = [-1] * n
par = [-1] * n
q = deque([s])
dist[s] = 0
while q:
    v = q.popleft()
    for to in G[v]:
        if dist[to] != -1:
            continue
        dist[to] = dist[v] + 1
        par[to] = v
        q.append(to)

# 例：t までの経路を復元（到達不可なら空リスト）
[t] = LMI()
t -= 1
path = []
if dist[t] != -1:
    cur = t
    while cur != -1:
        path.append(cur)
        cur = par[cur]
    path.reverse()
    # 0-index -> 1-index に戻す
    path = [x + 1 for x in path]
# dist: 各頂点までの最短距離（辺数）、path: s→t の経路（1-index）
```

**入力形式例**
```
n m
u_1 v_1
...
u_m v_m
s
t
```

---

## 2. 有向グラフ（重みなし）— 到達判定/距離

```python
n, m = LMI()
G = [[] for _ in range(n)]
for _ in range(m):
    u, v = LMI()
    u -= 1; v -= 1
    G[u].append(v)  # 片方向のみ

[s] = LMI(); s -= 1

dist = [-1] * n
q = deque([s])
dist[s] = 0
while q:
    v = q.popleft()
    for to in G[v]:
        if dist[to] != -1:
            continue
        dist[to] = dist[v] + 1
        q.append(to)
# dist[i] == -1 なら未到達
```

**入力形式**
```
n m
u_1 v_1
...
u_m v_m
s
```

---

## 3. 複数始点 BFS（無向/有向どちらでも可）
複数頂点を同時に距離 0 として始めるパターン。各頂点の最短距離（最近の始点からの距離）を一括で求めます。

```python
n, m = LMI()
G = [[] for _ in range(n)]
for _ in range(m):
    u, v = LMI(); u -= 1; v -= 1
    G[u].append(v)
    G[v].append(u)  # 有向なら片側のみ

k = int(input())
sources = [x - 1 for x in LMI()]  # 長さ k

dist = [-1] * n
q = deque()
for s in sources:
    dist[s] = 0
    q.append(s)

while q:
    v = q.popleft()
    for to in G[v]:
        if dist[to] != -1:
            continue
        dist[to] = dist[v] + 1
        q.append(to)
```

**入力形式**
```
n m
u_1 v_1
...
u_m v_m
k
s_1 s_2 ... s_k
```

---

## 4. グリッド BFS（壁 `#`、4 近傍）— S/G 位置が座標で与えられる

```python
H, W = LMI()
sh, sw = LMI(); gh, gw = LMI()
sh -= 1; sw -= 1; gh -= 1; gw -= 1
S = [list(input().strip()) for _ in range(H)]

INF = -1
Dist = [[INF]*W for _ in range(H)]
q = deque([(sh, sw)])
Dist[sh][sw] = 0

for_d = [(1,0),(-1,0),(0,1),(0,-1)]

while q:
    r, c = q.popleft()
    for dr, dc in for_d:
        nr, nc = r + dr, c + dc
        if not (0 <= nr < H and 0 <= nc < W):
            continue
        if S[nr][nc] == '#':
            continue
        if Dist[nr][nc] != INF:
            continue
        Dist[nr][nc] = Dist[r][c] + 1
        q.append((nr, nc))

ans = Dist[gh][gw]  # 到達不可なら -1
```

**入力形式**
```
H W
sh sw
gh gw
row_1
...
row_H
```

---

## 5. グリッド BFS（S/G が文字として埋め込まれている）

```python
H, W = LMI()
S = [list(input().strip()) for _ in range(H)]
sh = sw = gh = gw = -1
for i in range(H):
    for j in range(W):
        if S[i][j] == 'S': sh, sw = i, j
        if S[i][j] == 'G': gh, gw = i, j

from collections import deque
Dist = [[-1]*W for _ in range(H)]
q = deque([(sh, sw)])
Dist[sh][sw] = 0

for_d = [(1,0),(-1,0),(0,1),(0,-1)]
while q:
    r, c = q.popleft()
    for dr, dc in for_d:
        nr, nc = r + dr, c + dc
        if not (0 <= nr < H and 0 <= nc < W):
            continue
        if S[nr][nc] == '#':
            continue
        if Dist[nr][nc] != -1:
            continue
        Dist[nr][nc] = Dist[r][c] + 1
        q.append((nr, nc))

print(Dist[gh][gw])
```

**入力形式**
```
H W
row_1  # 例: S..#.
...
row_H  # 例: ..#G.
```

---

## 6. 0-1 BFS（辺重み 0/1）— `deque` を使う最短距離
重みが 0 または 1 のときは Dijkstra ではなく **0-1 BFS** が高速。

```python
n, m = LMI()
G = [[] for _ in range(n)]  # (to, w) で w ∈ {0,1}
for _ in range(m):
    u, v, w = LMI(); u -= 1; v -= 1
    G[u].append((v, w))
    G[v].append((u, w))  # 有向なら片側のみ

[s] = LMI(); s -= 1
INF = 10**18
from collections import deque

dist = [INF] * n
q = deque([s])
dist[s] = 0
while q:
    v = q.popleft()
    for to, w in G[v]:
        nd = dist[v] + w
        if nd < dist[to]:
            dist[to] = nd
            if w == 0:
                q.appendleft(to)
            else:
                q.append(to)
```

**入力形式**
```
n m
u_1 v_1 w_1  # w_i は 0 か 1
...
u_m v_m w_m
s
```

---

## 7. 連結成分数（無向グラフ）— BFS で CC を数える

```python
n, m = LMI()
G = [[] for _ in range(n)]
for _ in range(m):
    u, v = LMI(); u -= 1; v -= 1
    G[u].append(v)
    G[v].append(u)

seen = [False] * n
cc = 0
for s in range(n):
    if seen[s]:
        continue
    cc += 1
    q = deque([s])
    seen[s] = True
    while q:
        v = q.popleft()
        for to in G[v]:
            if seen[to]:
                continue
            seen[to] = True
            q.append(to)
# cc: 連結成分の個数
```

---

### 使い分けメモ
- **無向/有向**: 辺の追加方向に注意。
- **グリッド**: 壁文字・近傍（4/8）・座標/S/G の与え方に応じて読み替え。
- **計測**: 距離は「辺数」。経路が必要なら `par` で復元。
- **高速入出力**: `input = sys.stdin.readline` を最初に設定。
- **境界/未訪問**: グラフは `dist = [-1]`、グリッドは `Dist = [[-1]*W for _ in range(H)]` を慣用に。