import sys
from math import log2, e
from typing import Tuple
from collections import defaultdict, deque


def task(s: str, root: str) -> Tuple[float, float]:
    edges = []
    for line in s.strip().splitlines():
        parts = [x.strip() for x in line.split(',') if x.strip()]
        if len(parts) >= 2:
            edges.append((parts[0], parts[1]))

    if not edges:
        return 0.0, 0.0

    nodes = sorted(set([u for u, v in edges] + [v for u, v in edges]))
    n = len(nodes)

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    level = {root: 0}
    q = deque([root])
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if nxt not in level:
                level[nxt] = level[cur] + 1
                q.append(nxt)

    r1 = set(edges)
    r2 = {(v, u) for (u, v) in edges}
    r3 = {(u, w) for u, v in edges for w in graph[v] if (u, w) not in edges}
    r4 = {(w, u) for (u, w) in r3}
    r5 = {(a, b) for a in nodes for b in nodes if a != b and level.get(a) == level.get(b)}

    relations = [r1, r2, r3, r4, r5]

    h_total = 0.0
    for m in nodes:
        for r in relations:
            l_ij = sum(1 for (u, v) in r if u == m)
            if l_ij == 0:
                continue
            p = l_ij / (n - 1)
            h_total += -p * log2(p)

    c = 0.53
    h_ref = c * n * len(relations)
    h_norm = h_total / h_ref

    return round(h_total, 1), round(h_norm, 1)


def main() -> Tuple[float, float]:
    if len(sys.argv) < 3:
        print("Использование: python script.py путь_к_csv корневой_узел")
        sys.exit(1)

    csv_file_path = sys.argv[1]
    root_id = sys.argv[2]

    with open(csv_file_path, encoding='utf-8') as f:
        csv_data = f.read()

    result = task(csv_data, root_id)
    print(result)
    return result


if __name__ == "__main__":
    main()
