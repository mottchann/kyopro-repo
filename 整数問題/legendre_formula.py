def legendre(n: int, p: int) -> int:
    """
    ルジャンドルの公式を用いて n! に含まれる素数 p の指数を返す。

    Parameters
    ----------
    n : int
        階乗の上限 (n ≥ 0)
    p : int
        素数 (p ≥ 2)

    Returns
    -------
    int
        n! を素因数分解したときの p の指数 e_p(n!)
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if p < 2:
        raise ValueError("p must be an integer ≥ 2 (preferably prime)")

    exponent = 0
    power = p
    while power <= n:
        exponent += n // power
        power *= p
    return exponent


if __name__ == "__main__":
    # デモ: いくつかの値で確認
    tests = [(10, 2), (100, 5), (25, 5), (1_000_000, 2)]
    for n, p in tests:
        print(f"e_{p}({n}!) = {legendre(n, p)}")