import string
import numpy as np
import networkx as nx
from networkx.classes.function import path_weight

global m

def get_node_name(i, j):
    if i<10:
        a = '0'+str(i)
    else:
        a = str(i)
    if j<10:
        b = '0'+str(j)
    else:
        b = str(j)
    return a+b

def get_adjacent_indices(point, m, n):
    i = point[0]
    j = point[1]
    adjacent_indices = []
    if i > 0:
        adjacent_indices.append((i-1,j))
    if i+1 < m:
        adjacent_indices.append((i+1,j))
    if j > 0:
        adjacent_indices.append((i,j-1))
    if j+1 < n:
        adjacent_indices.append((i,j+1))
    return adjacent_indices
    vm.append(point)
    if starting_point in get_adjacent_indices(point, height, base):
        del vm
        return 1
    else:
        feasible_moves=[]
        for adj in get_adjacent_indices(point, height, base):
            if check_feasible_move(point, adj, vm):
                feasible_moves.append(adj)

        if not feasible_moves:
            del vm
            return 999
        else:
            return 1 + min([get_min_path(poss, vm.copy()) for poss in feasible_moves])

d = 12 # day problem number
with open('inputd{}.txt'.format(d), 'r') as f:
    lines = f.readlines()

s=0
s2=0
lower = list(string.ascii_lowercase)
t1 = dict(zip(lower, list(range(1,len(lower)+1))))
t1['S']=0
t1['E']=27
na=[]
acount=0

for line in lines:
    for char in line:
        if char=='a': acount+=1
    na.append([t1[c] for c in list(line[:-1])])

m = np.matrix(na)
height = m.shape[0]
base = m.shape[1]

G = nx.DiGraph()

finish_point = np.where(m==t1['E'])[0], np.where(m==t1['E'])[1]
starting_point = np.where(m==t1['S'])[0], np.where(m==t1['S'])[1]

finish_point_s = get_node_name(finish_point[0].item(), finish_point[1].item()) 
starting_point_s = get_node_name(starting_point[0].item(), starting_point[1].item())

m[starting_point] = 1
m[finish_point] = 26

for i in range(0, height):
    for j in range(0, base):
        val = m[i,j]
        name = get_node_name(i,j)
        G.add_node(name)

        for ad in get_adjacent_indices((i,j), height, base):
            if m[ad] <= val+1:
                w = 1.0
            else:
                w = 999999.0
            G.add_edge(name, get_node_name(ad[0], ad[1]), weight=w)

# part one
sp = nx.shortest_path(G, source=starting_point_s, target=finish_point_s, weight='weight')
s = len(sp)-1

# part two
starting_choices = np.where(m==1)
zipped_choices = list(zip(starting_choices[0], starting_choices[1]))
starting_node_choices = [get_node_name(sts[0].item(), sts[1].item()) for sts in zipped_choices]

assert acount+1 == len(starting_node_choices)
assert starting_point_s in starting_node_choices

tye = [nx.shortest_path(G, source=choice, target=finish_point_s, weight='weight') for choice in starting_node_choices]

min_w = min([path_weight(G, rrr, weight="weight") for rrr in tye])

for uu in tye:
    if path_weight(G, uu, weight="weight") == min_w:
        s2 = len(uu)-1

print('Part one:')
print(s)

print('*-'*30)

print('Part Two:')
print(s2)
