from time import perf_counter

def is_conflict(pos, r, c):
    for (pr, pc) in pos:
        if pr == r or pc == c or abs(pr - r) == abs(pc - c):
            return True
    return False

def find_solutions(N, K, max_solutions=100):
    solutions = []
    cells = [(r, c) for r in range(N) for c in range(N)]
    total_cells = N * N

    def dfs(start_idx, placed):
        if len(solutions) >= max_solutions:
            return
        if len(placed) == K:
            solutions.append(placed.copy())
            return
        remaining_needed = K - len(placed)
        if total_cells - start_idx < remaining_needed:
            return

        for i in range(start_idx, total_cells):
            r, c = cells[i]
            if not is_conflict(placed, r, c):
                placed.append((r, c))
                dfs(i + 1, placed)
                placed.pop()
            if len(solutions) >= max_solutions:
                return

    dfs(0, [])
    return solutions

def solve_nqueens(data):
    try:
        N = int(data.get('board_size', 8))
        K = int(data.get('queens', N))
        max_solutions = int(data.get('max_solutions', 50))
    except Exception:
        return {'error': 'Invalid parameters (must be integers).'}

    if N <= 0 or K <= 0 or K > N * N:
        return {'error': 'Invalid sizes: ensure 1 <= queens <= board_size^2 and board_size > 0'}

    start = perf_counter()
    sols = find_solutions(N, K, max_solutions)
    elapsed = perf_counter() - start

    sols_json = [[[r, c] for (r, c) in sol] for sol in sols]
    return {
        'board_size': N,
        'queens': K,
        'solutions_found': len(sols_json),
        'solutions': sols_json,
        'time_seconds': elapsed
    }