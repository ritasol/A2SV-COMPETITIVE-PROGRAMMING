# Enter your code here. Read input from STDIN. Print output to STDOUT
eng_num = int(input())
eng_stu = input().split()
fre_num = int(input())
fre_stu = input().split()

# create a set and add the roll numbers of the students in the set then retrun the length of the set created

container = set()

for student in eng_stu:
    container.add(student)
    
for student in fre_stu:
    container.add(student)
    
print(len(container))


