# ルジャンドルの公式 (Legendre's Formula)

## 目的
競技プログラミングで頻出する「n! に含まれる素数 p の個数」を高速に求める公式を理解し、実装に活かす。

## 定義（公式）
与えられた正整数 $n$ と素数 $p$ に対して  

$$
e_p(n!) \;=\; \sum_{k=1}^{\infty} \left\lfloor \frac{n}{p^k} \right\rfloor
$$  

ここで $e_p(n!)$ は $n!$ を素因数分解したときの $p$ の指数（何回現れるか）を表します。  
実際には $p^k > n$ となった時点で打ち切れば十分です。

## 例
| $n$ | $p$ | 計算 | 結果 |
| --- | --- | --- | --- |
| 10 | 2 | $\lfloor10/2\rfloor + \lfloor10/4\rfloor + \lfloor10/8\rfloor$ | **8** |
| 100 | 5 | $\lfloor100/5\rfloor + \lfloor100/25\rfloor$ | **24** |

## 直感的な説明
1. $n!$ には $1$〜$n$ の整数がすべて掛け合わされています。  
2. その中で **$p$ で割り切れる数** は $\lfloor n/p \rfloor$ 個あります。  
3. さらに **$p^2$ で割り切れる数** には追加でもう 1 つ $p$ が含まれています——よって $\lfloor n/p^2 \rfloor$ 個を加算します。  
4. このように $p^k$ が $n$ を超えるまで繰り返せば、$p$ が何回掛けられているかをすべて数え上げられます。

## 典型的な利用例
- $nCr$（組合せ数）を素数で割った余りを求める際の $p$ 進数解析  
- 多項係数や階乗を扱う整数問題（例：AtCoder ABC 200 “Factorial and Multiple”）  
- $n!$ の約数個数・桁数の計算

## Python 実装
実装サンプルは同ディレクトリの [`legendre_formula.py`](./legendre_formula.py) を参照してください。

## 参考文献
- Graham, Knuth, Patashnik *Concrete Mathematics*  
- AtCoder Library Practice Contest 解説