class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        length = len(graph)
        incoming=[0]*len(graph)
        graoh=[[] for i in range(length)]
        for i in range(len(graph)):
            incoming[i]=len(graph[i])
            for j in graph[i]:
                graoh[j].append(i)
        que=deque()
        ans=[]*length
        for i in range(length):
            if incoming[i]==0:
                que.append(i)
        while que:
            curr=que.popleft()
            ans.append(curr)
            for i in graoh[curr]:
                if incoming[i]!=0:
                    incoming[i]-=1
                if incoming[i]==0:
                    que.append(i)
        return sorted(ans)



