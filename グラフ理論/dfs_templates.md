

# DFS 入出力テンプレート集（Python）

競技プログラミングで頻出の **DFS（深さ優先探索）** を、典型的な入出力パターンごとに最小構成でまとめます。
入力は **1-indexed** を想定し、コード内では **0-indexed** に変換します。

まずは便利関数とお約束の import：

```python
import sys
sys.setrecursionlimit(1 << 25)
input = sys.stdin.readline

def LMI():
    """空白区切り整数をリストで返すショートハンド"""
    return list(map(int, input().split()))
```

---

## 1. 無向グラフ（重みなし）— 再帰 DFS（到達判定）

```python
n, m = LMI()
G = [[] for _ in range(n)]
for _ in range(m):
    u, v = LMI(); u -= 1; v -= 1
    G[u].append(v)
    G[v].append(u)

[s] = LMI(); s -= 1
seen = [False] * n

def dfs(v: int) -> None:
    seen[v] = True
    for to in G[v]:
        if not seen[to]:
            dfs(to)

dfs(s)
# seen[i] が True なら s から到達可能
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

## 2. 無向グラフ（重みなし）— 経路復元（親配列）

```python
n, m = LMI()
G = [[] for _ in range(n)]
for _ in range(m):
    u, v = LMI(); u -= 1; v -= 1
    G[u].append(v)
    G[v].append(u)

s, t = LMI(); s -= 1; t -= 1
par = [-1] * n
seen = [False] * n

def dfs(v: int, p: int) -> None:
    seen[v] = True
    par[v] = p
    for to in G[v]:
        if to == p:
            continue
        if not seen[to]:
            dfs(to, v)

dfs(s, -1)
# 復元
path = []
if seen[t]:
    cur = t
    while cur != -1:
        path.append(cur + 1)  # 1-index に戻す
        cur = par[cur]
    path.reverse()
```

---

## 3. 有向グラフ（重みなし）— 再帰 DFS + 行きがけ/帰りがけ時刻

```python
n, m = LMI()
G = [[] for _ in range(n)]
for _ in range(m):
    u, v = LMI(); u -= 1; v -= 1
    G[u].append(v)

ord = [-1] * n        # 行きがけ
low = [-1] * n        # 帰りがけ（終了時刻でもOKだが low は別用途で使うことも）
time = 0

seen = [False] * n

def dfs(v: int) -> None:
    global time
    seen[v] = True
    ord[v] = time; time += 1
    for to in G[v]:
        if not seen[to]:
            dfs(to)
    low[v] = time; time += 1

for v in range(n):
    if not seen[v]:
        dfs(v)
# ord[v], low[v] を使ってトポロジや根付き木などの処理に応用
```

---

## 4. 有向非巡回グラフ（DAG）のトポロジカルソート（DFS 後序順）

```python
n, m = LMI()
G = [[] for _ in range(n)]
for _ in range(m):
    u, v = LMI(); u -= 1; v -= 1
    G[u].append(v)

seen = [False] * n
order = []

cycle = False
state = [0] * n  # 0=未訪問,1=探索中,2=完了

def dfs(v: int) -> None:
    nonlocal_cycle = False
    state[v] = 1
    for to in G[v]:
        if state[to] == 0:
            dfs(to)
        elif state[to] == 1:
            # back edge -> cycle
            nonlocal_cycle = True
    state[v] = 2
    order.append(v)
    if nonlocal_cycle:
        raise RuntimeError("cycle detected")

try:
    for v in range(n):
        if state[v] == 0:
            dfs(v)
    order.reverse()  # トポ順
except RuntimeError:
    order = None  # サイクルあり
```

---

## 5. 無向グラフの連結成分数（DFS）

```python
n, m = LMI()
G = [[] for _ in range(n)]
for _ in range(m):
    u, v = LMI(); u -= 1; v -= 1
    G[u].append(v)
    G[v].append(u)

seen = [False] * n
cc = 0

def dfs(s: int) -> None:
    seen[s] = True
    for to in G[s]:
        if not seen[to]:
            dfs(to)

for v in range(n):
    if not seen[v]:
        cc += 1
        dfs(v)
# cc に連結成分数
```

---

## 6. 木 DFS — 根付き木の深さ/親/部分木サイズ

```python
n = int(input())
G = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = LMI(); u -= 1; v -= 1
    G[u].append(v)
    G[v].append(u)

root = 0
parent = [-1] * n
depth = [0] * n
subsz = [1] * n

def dfs(v: int, p: int) -> None:
    parent[v] = p
    for to in G[v]:
        if to == p:
            continue
        depth[to] = depth[v] + 1
        dfs(to, v)
        subsz[v] += subsz[to]

dfs(root, -1)
# parent, depth, subsz が利用可能
```

---

## 7. グリッド DFS（4 近傍）— 壁 `#` を避ける

```python
H, W = LMI()
S = [list(input().strip()) for _ in range(H)]

sys.setrecursionlimit(1 << 25)

seen = [[False] * W for _ in range(H)]

def dfs(r: int, c: int) -> None:
    seen[r][c] = True
    for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
        nr, nc = r + dr, c + dc
        if not (0 <= nr < H and 0 <= nc < W):
            continue
        if S[nr][nc] == '#':
            continue
        if not seen[nr][nc]:
            dfs(nr, nc)

# 例：S/G が文字で埋め込まれているときの起点探索
sr = sc = gr = gc = -1
for i in range(H):
    for j in range(W):
        if S[i][j] == 'S': sr, sc = i, j
        if S[i][j] == 'G': gr, gc = i, j

dfs(sr, sc)
# seen[gr][gc] で到達判定
```

---

## 8. 反復（スタック）DFS — 再帰を避ける

```python
n, m = LMI()
G = [[] for _ in range(n)]
for _ in range(m):
    u, v = LMI(); u -= 1; v -= 1
    G[u].append(v)
    G[v].append(u)

[s] = LMI(); s -= 1
seen = [False] * n
st = [s]
while st:
    v = st.pop()
    if seen[v]:
        continue
    seen[v] = True
    for to in G[v]:
        if not seen[to]:
            st.append(to)
```

---

## 9. 橋（bridge）と関節点（articulation point）— Low-Link（無向）

```python
n, m = LMI()
G = [[] for _ in range(n)]
for _ in range(m):
    u, v = LMI(); u -= 1; v -= 1
    G[u].append(v)
    G[v].append(u)

ord = [-1] * n
low = [-1] * n
time = 0
bridges = []
arts = set()

def dfs(v: int, p: int) -> None:
    global time
    ord[v] = low[v] = time; time += 1
    child = 0
    for to in G[v]:
        if to == p:
            continue
        if ord[to] == -1:
            child += 1
            dfs(to, v)
            low[v] = min(low[v], low[to])
            if ord[v] < low[to]:
                bridges.append((v, to))
            if p != -1 and ord[v] <= low[to]:
                arts.add(v)
        else:
            low[v] = min(low[v], ord[to])
    if p == -1 and child >= 2:
        arts.add(v)

for v in range(n):
    if ord[v] == -1:
        dfs(v, -1)
# bridges: 橋の辺集合、arts: 関節点集合
```

---

### 使い分けメモ
- **再帰 vs 反復**: Python は再帰が遅め＆スタック制限があるため、深い木/グラフでは `sys.setrecursionlimit` や反復 DFS を検討。
- **無向/有向**: 無向は双方向に辺を張る。有向は片方向。
- **木 DFS**: 親・深さ・部分木サイズが典型。根は 0（1-index の頂点 1）に置くことが多い。
- **トポロジカルソート**: DAG 前提。サイクル検出と組み合わせると安全。
- **グリッド**: 壁文字・近傍（4/8）に注意。見つけた S/G の座標から開始。