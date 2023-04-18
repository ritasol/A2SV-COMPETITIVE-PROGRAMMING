from collections import defaultdict
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i in range(len(edges)):
            n1 = edges[i][0]
            n2 = edges[i][1]
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        for node in graph:
            if len(graph[node]) == (len(edges)):
                return node
