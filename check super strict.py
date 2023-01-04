# Enter your code here. Read input from STDIN. Print output to STDOUT
set_a = list(input().split())

n = int(input())
ans =[]
for i in range(n):
    set_n = list(input().split())
    
    if all(x in set_a for x in set_n) and len(set_a) != len(set_n):
        ans.append(True)
    else:
        ans.append(False)
        
if False in ans:
    print(False)

else:
    print(True)
