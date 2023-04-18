import re
grid = []
n = int(input())
for i in range(n):
    s = input()
    grid.append(re.sub('[\s+]', '', s))
not_sources = []
sources = []
sinks = []
for i in range(len(grid)):
    if "1" not in grid[i]:
        sinks.append(i+1)

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "1":
            not_sources.append(j+1)


for i in range(1,n+1):
    if i not in not_sources:
        sources.append(i)
print(len(sources),*sources)
print(len(sinks),*sinks)
