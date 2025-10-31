import heapq
import random
from typing import Tuple, List, Dict, Optional

State = Tuple[int, ...]
GOAL: State = (1, 2, 3, 4, 5, 6, 7, 8, 0)

MOVES = {
    'up': -3,
    'down': 3,
    'left': -1,
    'right': 1
}

def index_to_rc(i: int) -> Tuple[int, int]:
    return divmod(i, 3)

def neighbors(state: State) -> List[Tuple[State, str]]:
    zero = state.index(0)
    zr, zc = index_to_rc(zero)
    results = []
    for name, d in MOVES.items():
        ni = zero + d
        if name == 'left' and zc == 0: continue
        if name == 'right' and zc == 2: continue
        if name == 'up' and zr == 0: continue
        if name == 'down' and zr == 2: continue
        new_list = list(state)
        new_list[zero], new_list[ni] = new_list[ni], new_list[zero]
        results.append((tuple(new_list), name))
    return results

def is_solvable(state: State) -> bool:
    arr = [x for x in state if x != 0]
    inv = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                inv += 1
    return inv % 2 == 0

def h_manhattan(state: State) -> int:
    dist = 0
    for i, v in enumerate(state):
        if v == 0: continue
        goal_index = v - 1
        r1, c1 = index_to_rc(i)
        r2, c2 = index_to_rc(goal_index)
        dist += abs(r1 - r2) + abs(c1 - c2)
    return dist

def h_misplaced(state: State) -> int:
    return sum(1 for i, v in enumerate(state) if v != 0 and v != GOAL[i])

def a_star(start: State, heuristic='manhattan') -> Optional[List[State]]:
    if not is_solvable(start):
        return None
    h_func = h_manhattan if heuristic == 'manhattan' else h_misplaced

    open_heap = []
    g_score: Dict[State, int] = {start: 0}
    f_score = h_func(start)
    heapq.heappush(open_heap, (f_score, 0, start))
    came_from: Dict[State, Optional[State]] = {start: None}

    while open_heap:
        f, g_tie, current = heapq.heappop(open_heap)
        if current == GOAL:
            path = []
            s = current
            while s is not None:
                path.append(s)
                s = came_from[s]
            path.reverse()
            return path

        g_current = g_score[current]
        for nbr, _move in neighbors(current):
            tentative_g = g_current + 1
            if nbr not in g_score or tentative_g < g_score[nbr]:
                came_from[nbr] = current
                g_score[nbr] = tentative_g
                f_n = tentative_g + h_func(nbr)
                heapq.heappush(open_heap, (f_n, tentative_g, nbr))
    return None

def random_shuffle(steps: int = 30) -> State:
    s = list(GOAL)
    for _ in range(steps):
        valid = neighbors(tuple(s))
        s, _ = random.choice(valid)
        s = list(s)
    return tuple(s)

def move_tile(state: State, tile: int) -> Dict:
    zero = state.index(0)
    if tile == 0:
        return {'error': 'Cannot move blank tile'}
    
    try:
        ti = state.index(tile)
    except ValueError:
        return {'error': 'Invalid tile'}
    
    zr, zc = index_to_rc(zero)
    tr, tc = index_to_rc(ti)
    
    if abs(zr - tr) + abs(zc - tc) != 1:
        return {'error': 'Tile not adjacent to blank'}
    
    new_list = list(state)
    new_list[zero], new_list[ti] = new_list[ti], new_list[zero]
    new_state = tuple(new_list)
    
    return {
        'state': list(new_state),
        'solved': new_state == GOAL
    }

def solve_puzzle(state: State, heuristic: str = 'manhattan') -> Dict:
    path = a_star(state, heuristic)
    
    if path is None:
        return {'error': 'Unsolvable state'}
    
    return {
        'path': [list(s) for s in path],
        'moves': len(path) - 1
    }