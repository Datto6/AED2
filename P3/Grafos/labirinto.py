from collections import deque
def labirintoSolver(L,iS,jS,iT,jT):
    cols=len(L[0]) #numero de colunas
    rows=len(L)
    dist = [[-1 for _ in range(cols)] for _ in range(rows)]
     # Previous cell in the shortest path
    parent = [[None for _ in range(cols)] for _ in range(rows)]

    queue = deque()

    queue.append((iS, jS))
    dist[iS][jS] = 0

    # Up, down, left, right
    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        i, j = queue.popleft()
        for di, dj in direcoes:
            ni = i + di
            nj = j + dj

            # Check if inside the grid
            if 0 <= ni < rows and 0 <= nj < cols:
                # Check if it is free and hasn't been visited
                if L[ni][nj] != '#' and dist[ni][nj] == -1:
                    dist[ni][nj] = dist[i][j] + 1
                    parent[ni][nj] = (i, j)
                    queue.append((ni, nj))

    # T is unreachable
    if dist[iT][jT] == -1:
        return None
    # Reconstruct path
    path = []
    current = (iT, jT)
    while current != None:
        path.append(current)
        current = parent[current[0]][current[1]]
    path.reverse()
    return dist[iT][jT], path

L = [
    "S...",
    ".##.",
    "...T"
]


dist, path = labirintoSolver(L, 0, 0, 2, 3)

print("Movimentos:", dist)
print("Caminho:", path)