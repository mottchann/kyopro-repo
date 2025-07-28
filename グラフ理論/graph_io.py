"""
競技プログラミングでよく使うグラフ入力テンプレート集。

- `LMI()` は `list(map(int, input().split()))` を短く書くためのヘルパ関数。
- 入力は 1-indexed を想定し、コード内では 0-indexed に変換する。
- 各セクションで `graph = [[] for _ in range(n)]` を用いて隣接リストを構築する。
"""

# 空白区切り整数列を読み込む短縮関数
def LMI():
    return list(map(int, input().split()))

# 1. 無向グラフ（重みなし）
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    # 0-index へ変換
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)

# 2. 無向グラフ（重みあり）
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v, c = map(int, input().split())
    # 0-index へ変換
    u -= 1
    v -= 1
    graph[u].append((v, c))
    graph[v].append((u, c))

# 3. 有向グラフ（重みなし）
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    # 0-index へ変換
    u -= 1
    v -= 1
    graph[u].append(v)

# 4. 有向グラフ（重みあり）
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v, c = map(int, input().split())
    # 0-index へ変換
    u -= 1
    v -= 1
    graph[u].append((v, c))
