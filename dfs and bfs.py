import sys
import time
from collections import deque

# Увеличиваем лимит рекурсии с запасом
sys.setrecursionlimit(20000)

def bfs(graph, start):
    start_time = time.perf_counter()
    visited = {start}
    queue = deque([start])
    while queue:
        v = queue.popleft()
        # Используем .get(v, []), чтобы не упасть, если у узла нет соседей
        for neighbor in graph.get(v, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return time.perf_counter() - start_time

def dfs(graph, start):
    start_time = time.perf_counter()
    visited = set()

    def run_dfs(v):
        visited.add(v)
        for neighbor in graph.get(v, []):
            if neighbor not in visited:
                run_dfs(neighbor)
    
    run_dfs(start)
    return time.perf_counter() - start_time

def generate_graph(n):
    # Генерируем "линейный" граф (цепочку), чтобы DFS уходил на максимальную глубину
    return {i: [i + 1] for i in range(n)}

# Тестируемые размеры
sizes = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]

print(f"{'Вершин':<10} | {'BFS (сек)':<12} | {'DFS (сек)':<12}")
print("-" * 40)

for n in sizes:
    graph = generate_graph(n)
    
    # Уменьшим количество повторений до 100 для скорости, 
    # так как 1000 повторов для 10000 узлов будет идти долго.
    iterations = 100
    
    t_bfs = sum(bfs(graph, 0) for _ in range(iterations)) / iterations
    t_dfs = sum(dfs(graph, 0) for _ in range(iterations)) / iterations
    
    print(f"{n:<10} | {t_bfs:<12.8f} | {t_dfs:<12.8f}")
