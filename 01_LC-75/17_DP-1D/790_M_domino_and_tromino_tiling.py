class Solution:
    def numTilings(self, n: int) -> int:
        """
        1. Recursion (pure brute force)
        - f(n) = # ways to tile a 2xn board
        - at col n you cna place:
        -- a vertical domino: covers 2x1
        -- two horizontal dominos: covers 2x2
        -- a tromino (L-shape): creates "gap" state
        => we get two states: 
        ASK YOURSELF: "what choices do I have at column n"
            i:  full(n) or f(n): ways to tile a full 2xn board
            ii: gap(n) or f(n): ways to tile a 2xn board with a gap at col n
                == gap(n): everything up to col n-1 is fully filed but there's
                a gap in column n (dangling cell) 
                --> # ways to tile 2xn board where the TOP OR Bottom cell of
                    column n is missing
                    1. XX   OR  XX
                       X_       _X
        DERIVING f(n): to get a fully filled column n (3 ways)
        1. place vertical domino at column n
        -> covers column n, so the rest MUST be a full 2x(n-1): 
        ==> f(n-1)
        2. place two horizontal dominoes covering col n-1 AND n: 
        -> covers columns n AND n-1, rest must be a full 2x(n-2):
        ==> f(n-2)
        3. Place a tromino that "fix" a gap at column n-1 AND end full at n
        - if at col n-1 we have a gap: gap(n-1)
        -- use 1 tromino that covers col n-1 and n and removes the gap AND 
            ending full at n
        - 2 possible orientations: top gap + bottom gap
        ==> 2*gap(n-1)
        ======>f(n) = f(n-1) + f(n-2) + 2*g(n-1)

        DERIVING g(n): ways to end with a gap at column n
        TWO POSSIBILITIES:
        1. extend a previous gap with a horizontal domino
        - suppose at col n-1 we already have a gap: gap(n-1)
        - use horizontal domino:
        -- covers missing cell at col n-1
        -- creates new gap on the other row at col n
        ==> gap(n-1)
        2. create a fresh gap using a tromino from full(n-2)
        n-2 n-1  n  => leaves a gap at col n
         X   X   _  => 2 orientations to do this gap (top gap or bot gap at col n)
         X   X   X  ===> 2*full(n-2)
        ======>g(n) = g(n-1) + 2*f(n-2)


        ==> full on recursion: exponential
        f(n) = f(n-1) + f(n-2) + 2*g(n-1)   # full board
        g(n) = g(n-1) + f(n-2)              # gap board
        
        BASE cases
        f(0) = 1 (empty board)
        f(1) = 1 (only vertical domino)
        g(0) = 0, g(1) = 0 (can't have a single column board with
        exactly one cell missing and still be tilable)


        2. Recursion + memoization (top‑down DP)
        ==> adding memoization makes it linear

        3. Tabulation (bottom‑up DP)

        4. Space optimization (if possible)
        """
        MOD = 10**9 + 7
        # For memoization we can either use 2 dicts OR 2 arrays (one for f, one for g).
        #
        # Arrays are faster because:
        #   - indexing (f[n]) is O(1) with no hashing
        #   - memory is contiguous, so CPU caching is better
        #   - Python lists are optimized for repeated integer access
        #
        # BUT: using arrays requires a sentinel value (like None or -1) so we can check
        # whether we already solved this subproblem. Without that check, we'd recompute
        # the same n many times.
        #
        # Dicts are slower (hash lookup) but:
        #   - they don't need sentinel values
        #   - they grow dynamically
        #   - they avoid the “did I compute this?” problem because we just check `if k in cache`
        #
        # So:
        #   - arrays = faster but require careful initialization + sentinel checks
        #   - dicts = simpler and safer, but slightly slower
        f_cache = {}  # full
        g_cache = {}  # gap

        def f(n):
            if n == 0: return 1
            if n == 1: return 1
            if n in f_cache:
                return f_cache[n]
            f_cache[n] = (f(n-1) + f(n-2) + 2*g(n-1)) % MOD
            return f_cache[n]
        def g(n):
            if n <= 1: return 0
            if n in g_cache:
                return g_cache[n]
            g_cache[n] = g(n-1) + f(n-2)
            return g_cache[n]

        return f(n)