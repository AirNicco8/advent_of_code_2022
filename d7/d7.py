from anytree import Node, RenderTree

d = 7 # day problem number
with open('inputd{}.txt'.format(d), 'r') as f:
    lines = f.readlines()

def recsum(root):
    if(root.children):
        return sum(root.files)+sum(list(map(recsum,list(root.children))))
    else:
        return sum(root.files)

s=0
s2=0
sl=[]
possible_deletions=[]
stack=[]
disk_space = 70000000
free_space_needed = 30000000

# populate the tree
for line in lines:
    line = line[:-1]

    if(line[0].isdigit()):
        stack[-1].files.append(int(''.join(filter(str.isdigit, line))))

    if(line[0] == '$'):
        com = line.split(' ')
        if(com[1] == 'cd'):
            if(com[2] == '/'):
                root = Node('root', files=[])
                stack.append(root)
            elif(com[2] != '..'):
                newnode = Node(com[2], parent=stack[-1], files=[])
                stack.append(newnode)
            else:
                stack.pop()

# part one
for pre, _, node in RenderTree(stack[0]):
    ss = recsum(node)
    sl.append(ss)
    if ss <= 100000:
        s+=ss

# part two
current_free_space=disk_space-sl[0]
for i in sl:
    if current_free_space+i >= free_space_needed:
        possible_deletions.append(i)
s2 = min(possible_deletions)

print('Part one:')
print(s)

print('*-'*30)

print('Part Two:')
print(s2)