def fibfib(n: int) -> int:
    """The FibFib (tribonacci) sequence:
    fibfib(0)=0, fibfib(1)=0, fibfib(2)=1, fibfib(n)=fibfib(n-1)+fibfib(n-2)+fibfib(n-3).
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1

    def mat_mult(A, B):
        return [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]

    def mat_pow(mat, exp):
        # identity
        res = [[1 if i == j else 0 for j in range(3)] for i in range(3)]
        while exp:
            if exp & 1:
                res = mat_mult(res, mat)
            mat = mat_mult(mat, mat)
            exp >>= 1
        return res

    M = [[1, 1, 1],
         [1, 0, 0],
         [0, 1, 0]]

    P = mat_pow(M, n - 2)
    # v2 = [fibfib(2)=1, fibfib(1)=0, fibfib(0)=0]; multiplying P by v2 picks P's first column
    return P[0][0]

