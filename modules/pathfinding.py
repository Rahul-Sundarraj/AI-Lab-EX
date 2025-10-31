from collections import deque
import heapq
import math

# Tamil Nadu districts graph
TN_DISTRICTS = {
    'Chennai': {'coords': (13.0827, 80.2707), 'neighbors': ['Kanchipuram', 'Tiruvallur', 'Chengalpattu']},
    'Kanchipuram': {'coords': (12.8342, 79.7036), 'neighbors': ['Chennai', 'Vellore', 'Tiruvannamalai', 'Chengalpattu']},
    'Tiruvallur': {'coords': (13.1067, 79.9078), 'neighbors': ['Chennai', 'Vellore', 'Ranipet']},
    'Chengalpattu': {'coords': (12.6919, 79.9758), 'neighbors': ['Chennai', 'Kanchipuram', 'Villupuram']},
    'Vellore': {'coords': (12.9165, 79.1325), 'neighbors': ['Tiruvallur', 'Kanchipuram', 'Tiruvannamalai', 'Ranipet']},
    'Ranipet': {'coords': (12.9249, 79.3308), 'neighbors': ['Tiruvallur', 'Vellore', 'Tirupattur']},
    'Tirupattur': {'coords': (12.4962, 78.5726), 'neighbors': ['Ranipet', 'Krishnagiri', 'Dharmapuri']},
    'Tiruvannamalai': {'coords': (12.2253, 79.0747), 'neighbors': ['Kanchipuram', 'Vellore', 'Villupuram', 'Kallakurichi']},
    'Villupuram': {'coords': (11.9401, 79.4861), 'neighbors': ['Chengalpattu', 'Tiruvannamalai', 'Kallakurichi', 'Cuddalore']},
    'Kallakurichi': {'coords': (11.7401, 78.9597), 'neighbors': ['Tiruvannamalai', 'Villupuram', 'Salem']},
    'Cuddalore': {'coords': (11.7480, 79.7714), 'neighbors': ['Villupuram', 'Ariyalur', 'Perambalur']},
    'Salem': {'coords': (11.6643, 78.1460), 'neighbors': ['Kallakurichi', 'Dharmapuri', 'Namakkal', 'Erode']},
    'Dharmapuri': {'coords': (12.1211, 78.1582), 'neighbors': ['Tirupattur', 'Krishnagiri', 'Salem']},
    'Krishnagiri': {'coords': (12.5186, 78.2137), 'neighbors': ['Tirupattur', 'Dharmapuri']},
    'Namakkal': {'coords': (11.2189, 78.1677), 'neighbors': ['Salem', 'Erode', 'Karur', 'Tiruchirappalli']},
    'Erode': {'coords': (11.3410, 77.7172), 'neighbors': ['Salem', 'Namakkal', 'Coimbatore', 'Tiruppur']},
    'Coimbatore': {'coords': (11.0168, 76.9558), 'neighbors': ['Erode', 'Tiruppur', 'Nilgiris', 'Dindigul']},
    'Tiruppur': {'coords': (11.1075, 77.3398), 'neighbors': ['Erode', 'Coimbatore', 'Karur']},
    'Nilgiris': {'coords': (11.4102, 76.6950), 'neighbors': ['Coimbatore']},
    'Karur': {'coords': (10.9571, 78.0766), 'neighbors': ['Namakkal', 'Tiruppur', 'Dindigul', 'Tiruchirappalli']},
    'Tiruchirappalli': {'coords': (10.7905, 78.7047), 'neighbors': ['Namakkal', 'Karur', 'Perambalur', 'Ariyalur', 'Thanjavur', 'Pudukkottai']},
    'Perambalur': {'coords': (11.2320, 78.8801), 'neighbors': ['Cuddalore', 'Ariyalur', 'Tiruchirappalli']},
    'Ariyalur': {'coords': (11.1401, 79.0770), 'neighbors': ['Cuddalore', 'Perambalur', 'Tiruchirappalli']},
    'Thanjavur': {'coords': (10.7870, 79.1378), 'neighbors': ['Tiruchirappalli', 'Nagapattinam', 'Tiruvarur', 'Pudukkottai']},
    'Nagapattinam': {'coords': (10.7658, 79.8448), 'neighbors': ['Thanjavur', 'Tiruvarur']},
    'Tiruvarur': {'coords': (10.7727, 79.6345), 'neighbors': ['Thanjavur', 'Nagapattinam', 'Mayiladuthurai']},
    'Mayiladuthurai': {'coords': (11.1025, 79.6519), 'neighbors': ['Tiruvarur', 'Cuddalore']},
    'Pudukkottai': {'coords': (10.3833, 78.8200), 'neighbors': ['Tiruchirappalli', 'Thanjavur', 'Sivaganga']},
    'Dindigul': {'coords': (10.3673, 77.9803), 'neighbors': ['Coimbatore', 'Karur', 'Madurai', 'Theni']},
    'Madurai': {'coords': (9.9252, 78.1198), 'neighbors': ['Dindigul', 'Theni', 'Virudhunagar', 'Sivaganga']},
    'Theni': {'coords': (10.0104, 77.4777), 'neighbors': ['Dindigul', 'Madurai']},
    'Sivaganga': {'coords': (9.8438, 78.4809), 'neighbors': ['Pudukkottai', 'Madurai', 'Ramanathapuram']},
    'Virudhunagar': {'coords': (9.5810, 77.9624), 'neighbors': ['Madurai', 'Tenkasi', 'Ramanathapuram']},
    'Ramanathapuram': {'coords': (9.3639, 78.8377), 'neighbors': ['Sivaganga', 'Virudhunagar', 'Thoothukudi']},
    'Tenkasi': {'coords': (8.9604, 77.3152), 'neighbors': ['Virudhunagar', 'Tirunelveli']},
    'Tirunelveli': {'coords': (8.7139, 77.7567), 'neighbors': ['Tenkasi', 'Thoothukudi', 'Kanyakumari']},
    'Thoothukudi': {'coords': (8.7642, 78.1348), 'neighbors': ['Ramanathapuram', 'Tirunelveli']},
    'Kanyakumari': {'coords': (8.0883, 77.5385), 'neighbors': ['Tirunelveli']}
}

def heuristic(district1, district2):
    lat1, lon1 = TN_DISTRICTS[district1]['coords']
    lat2, lon2 = TN_DISTRICTS[district2]['coords']
    return math.sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2)

def bfs(start, goal):
    queue = deque([(start, [start])])
    visited = {start}
    explored = []
    
    while queue:
        node, path = queue.popleft()
        explored.append(node)
        
        if node == goal:
            return {'path': path, 'explored': explored, 'cost': len(path) - 1}
        
        for neighbor in TN_DISTRICTS[node]['neighbors']:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return {'path': [], 'explored': explored, 'cost': float('inf')}

def dfs(start, goal):
    stack = [(start, [start])]
    visited = set()
    explored = []
    
    while stack:
        node, path = stack.pop()
        
        if node in visited:
            continue
            
        visited.add(node)
        explored.append(node)
        
        if node == goal:
            return {'path': path, 'explored': explored, 'cost': len(path) - 1}
        
        for neighbor in reversed(TN_DISTRICTS[node]['neighbors']):
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))
    
    return {'path': [], 'explored': explored, 'cost': float('inf')}

def ucs(start, goal):
    heap = [(0, start, [start])]
    visited = set()
    explored = []
    
    while heap:
        cost, node, path = heapq.heappop(heap)
        
        if node in visited:
            continue
            
        visited.add(node)
        explored.append(node)
        
        if node == goal:
            return {'path': path, 'explored': explored, 'cost': cost}
        
        for neighbor in TN_DISTRICTS[node]['neighbors']:
            if neighbor not in visited:
                heapq.heappush(heap, (cost + 1, neighbor, path + [neighbor]))
    
    return {'path': [], 'explored': explored, 'cost': float('inf')}

def depth_limited_dfs(start, goal, limit):
    def dls_recursive(node, goal, depth, path, visited, explored):
        explored.append(node)
        
        if node == goal:
            return path, True
        
        if depth == 0:
            return None, False
        
        visited.add(node)
        for neighbor in TN_DISTRICTS[node]['neighbors']:
            if neighbor not in visited:
                result, found = dls_recursive(neighbor, goal, depth - 1, path + [neighbor], visited.copy(), explored)
                if found:
                    return result, True
        
        return None, False
    
    explored = []
    result, found = dls_recursive(start, goal, limit, [start], set(), explored)
    
    if found:
        return {'path': result, 'explored': explored, 'cost': len(result) - 1}
    return {'path': [], 'explored': explored, 'cost': float('inf')}

def iterative_deepening(start, goal):
    explored = []
    
    for depth in range(len(TN_DISTRICTS)):
        result = depth_limited_dfs(start, goal, depth)
        explored.extend(result['explored'])
        
        if result['path']:
            return {'path': result['path'], 'explored': explored, 'cost': result['cost']}
    
    return {'path': [], 'explored': explored, 'cost': float('inf')}

def greedy(start, goal):
    heap = [(heuristic(start, goal), start, [start])]
    visited = set()
    explored = []
    
    while heap:
        _, node, path = heapq.heappop(heap)
        
        if node in visited:
            continue
            
        visited.add(node)
        explored.append(node)
        
        if node == goal:
            return {'path': path, 'explored': explored, 'cost': len(path) - 1}
        
        for neighbor in TN_DISTRICTS[node]['neighbors']:
            if neighbor not in visited:
                heapq.heappush(heap, (heuristic(neighbor, goal), neighbor, path + [neighbor]))
    
    return {'path': [], 'explored': explored, 'cost': float('inf')}

def a_star(start, goal):
    heap = [(heuristic(start, goal), 0, start, [start])]
    visited = {}
    explored = []
    
    while heap:
        f, g, node, path = heapq.heappop(heap)
        
        if node in visited and visited[node] <= g:
            continue
            
        visited[node] = g
        explored.append(node)
        
        if node == goal:
            return {'path': path, 'explored': explored, 'cost': g}
        
        for neighbor in TN_DISTRICTS[node]['neighbors']:
            new_g = g + 1
            if neighbor not in visited or new_g < visited.get(neighbor, float('inf')):
                new_f = new_g + heuristic(neighbor, goal)
                heapq.heappush(heap, (new_f, new_g, neighbor, path + [neighbor]))
    
    return {'path': [], 'explored': explored, 'cost': float('inf')}

def ao_star(start, goal):
    return a_star(start, goal)

def execute_search(data):
    algorithm = data.get('algorithm')
    start = data.get('start')
    goal = data.get('goal')
    
    if start not in TN_DISTRICTS or goal not in TN_DISTRICTS:
        return {'error': 'Invalid district names'}
    
    algorithms = {
        'bfs': bfs,
        'dfs': dfs,
        'ucs': ucs,
        'depth_limited': lambda s, g: depth_limited_dfs(s, g, 5),
        'iterative_deepening': iterative_deepening,
        'greedy': greedy,
        'a_star': a_star,
        'ao_star': ao_star
    }
    
    if algorithm not in algorithms:
        return {'error': 'Invalid algorithm'}
    
    result = algorithms[algorithm](start, goal)
    result['districts'] = TN_DISTRICTS
    
    return result