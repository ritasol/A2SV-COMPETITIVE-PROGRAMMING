class Solution:
    def generateParenthesis(self, n: int) -> List[str]:       
        # Memo to store the already visited combinaison of the rest of parentheses to open (named r for rest) and already opened parentheses (named o for opened)
        memo = [[[] for _ in range(n + 1)] for _ in range(n + 1)]
        # Base value
        memo[0][0] = ["", ]
        memo[0][1] = [")",]
        memo[1][0] = ["()",]
        
        
        def f(r, o): # r  rest  o opened    
            if memo[r][o]:
                return memo[r][o]
            if o == 0:  # if there is no resting parentheses, then close the ones already openend
                memo[r][o] = ["("+e for e in f(r-1, o+1)]
            elif r == 0:  # if there is no opened parentheses, then open one 
                memo[r][o] = [")"+e for e in f(r, o-1)]
            else:  # If there is opened and resting combinaison, then it is the combinaison of two
                memo[r][o] = ["("+e for e in f(r-1, o+1)] + [")"+e for e in f(r, o-1)]
            
            return memo[r][o]
        
        return f(n, 0)
