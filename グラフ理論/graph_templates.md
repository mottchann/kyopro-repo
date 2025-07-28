# グラフ入力テンプレート集

競技プログラミングで頻繁に使うグラフ入力スニペットをまとめました。  
入力は **1-indexed** を想定し、コード内では **0-indexed** に変換します。  
まずは便利関数 `LMI()` を定義しておくと入力を簡潔に記述できます。

```python
def LMI():
    """空白区切り整数をリストで返すショートハンド"""
    return list(map(int, input().split()))
```

---

## 1. 無向グラフ（重みなし）

```python
n, m = LMI()
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = LMI()
    u -= 1  # 0-index へ変換
    v -= 1
    graph[u].append(v)
    graph[v].append(u)
```

**入力形式**

```
n m
u_1 v_1
...
u_m v_m
```

---

## 2. 無向グラフ（重みあり）

```python
n, m = LMI()
graph = [[] for _ in range(n)]          # (隣接頂点, コスト) のタプルを格納
for _ in range(m):
    u, v, c = LMI()
    u -= 1
    v -= 1
    graph[u].append((v, c))
    graph[v].append((u, c))
```

**入力形式**

```
n m
u_1 v_1 c_1
...
u_m v_m c_m
```

---

## 3. 有向グラフ（重みなし）

```python
n, m = LMI()
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = LMI()
    u -= 1
    v -= 1
    graph[u].append(v)  # 片方向のみ
```

**入力形式**

```
n m
u_1 v_1
...
u_m v_m
```

---

## 4. 有向グラフ（重みあり）

```python
n, m = LMI()
graph = [[] for _ in range(n)]          # (隣接頂点, コスト) のタプル
for _ in range(m):
    u, v, c = LMI()
    u -= 1
    v -= 1
    graph[u].append((v, c))
```

**入力形式**

```
n m
u_1 v_1 c_1
...
u_m v_m c_m
```

---

### 使い分けメモ

- **無向 vs 有向**: 双方向に追加するか片方向か。
- **重みなし vs 重みあり**: `graph[u].append(v)` と `graph[u].append((v, c))` の違いのみ。
- 実行高速化が必要な場合は `input()` を `sys.stdin.readline` や `sys.stdin.buffer.read()` に置き換えると良いです。
