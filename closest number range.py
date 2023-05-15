class Solution:
    def helper(self,a, b):
            pri = [True for i in range(b + 1)] 
            n = 2
            
            while(n * n <= b):
                if pri[n]:
                    for i in range(n**2, b + 1, n):
                        pri[i] = False 
                n += 1
            
            queue = deque()
            res = []
            
            for i in range(max(2, a), b + 1):
                if pri[i]:
                    queue.append(i)
                    if len(queue) == 2:
                        res.append((queue[1] - queue[0],  queue[0], queue[1]))
                        queue.popleft()
            res.sort()

            if res:
                return res[0][1],res[0][2]
            return [-1,-1]
           
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
        
        return self.helper(left, right)
    
