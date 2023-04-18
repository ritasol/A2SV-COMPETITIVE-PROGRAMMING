import re
from collections import defaultdict
grid = []
n = int(input())
for _ in range(n):
    s = input()
    grid.append(list((re.sub('[\s+]', '', s))))
graph = defaultdict(list)

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "1":
            graph[i+1].append(j+1)
for i in graph:
    print(len(graph[i]),*graph[i])
