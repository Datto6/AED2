def greedyInterval(A):
    A.sort(key=lambda x: x[1])
    print(A)
    pontos=[]
    n=len(A)
    j=0
    for i in range(n):
        if len(pontos)==0:
            pontos.append(A[i][1])
        elif pontos[-1]<A[i][0]:
            pontos.append(A[i][1])
    return pontos

tests = [
    ([[1, 4], [2, 5], [3, 6], [7, 9], [8, 10]], [4, 9]),
    ([[1, 5], [2, 6], [3, 4], [1, 10]], [4]),
    ([[1, 2], [3, 4], [5, 6], [7, 8]], [2, 4, 6, 8]),
    ([[1, 3], [3, 5], [5, 7]], [3, 7]),
    ([[1, 10], [2, 3], [4, 5], [6, 7]], [3, 5, 7]),
    ([[2, 6], [2, 6], [2, 6], [2, 6]], [6]),
    ([[5, 12]], [12]),
    ([[4, 4]], [4]),
    ([[1, 20], [2, 15], [3, 10], [4, 8]], [8]),
    ([[1, 4], [2, 5], [3, 6],
      [8, 11], [9, 12], [14, 16], [15, 18]], [4, 11, 16]),
    ([[-10, -5], [-8, -3], [-2, 1], [0, 4]], [-5, 1]),
    ([[10, 12], [5, 9], [1, 4], [2, 3]], [3, 9, 12]),
    ([[1, 2], [2, 3], [3, 4], [4, 5]], [2, 4]),
    ([], [])
]

for i, (intervals, expected) in enumerate(tests, start=1):
    result = greedyInterval(intervals.copy())
    print(result)
    assert result == expected, (
        f"Test {i} failed: expected {expected}, got {result}"
    )

print("All tests passed!")