nums =  [[1,2],[3,4]]
r = 2
c = 4
new_ans = []
container = []
for i in range(len(nums)):
    for j in range(len(nums[i])):
        container.append(nums[i][j])
print(container)
if len(container) != r*c:
    print(nums)
else:
    for i in range(r):
        new_ans.append(container[i*c:(i*c)+c])
    print(new_ans)