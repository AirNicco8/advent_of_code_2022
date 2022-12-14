import numpy as np

global m, m2

def flatten(l):
    return [item for sublist in l for item in sublist]

def draw_rock_line(start, end): # draw line from point start to end in m
    if start[0]==end[0]: # the x changes
        if end[1] > start[1]:
            m[start[0],start[1]:(end[1]+1)] = 1
        else:
            m[start[0],end[1]:(start[1]+1)] = 1
    else: # the y changes
        if end[0] > start[0]:
            m[start[0]:(end[0]+1),start[1]] = 1
        else:
            m[end[0]:(start[0]+1),start[1]] = 1
    return m

def double_check(m, y, x): # check if it is a rest point
    y=y+1
    left = x-1
    right = x+1
    if (m[y,left] == 1) and (m[y,right] == 1):
        return 0
    elif (m[y,left] == 0):
        return 1
    else:
        return 2

def fall_from(m, y, x, xp_count, verb): # simulate a fall from given x and y
    if verb: print('falling from x {} y {} xpc {}'.format(y, x, xp_count))
    next_one_index = np.where(m[y+1:, x] == 1)[0]

    if next_one_index.size == 0:
        return 0

    next_one_index = next_one_index[0]

    tmp_count = xp_count+next_one_index

    next_one_index += xp_count

    if verb: print('checking left and right of x {} y {}'.format(next_one_index+1, x))
    place_check = double_check(m, next_one_index, x)

    if place_check == 0:
        if next_one_index == y: return 0 # blocking the source

        if verb: print('placing one on x {} y {}'.format(next_one_index, x))
        m[next_one_index, x]=1
        if verb: print(m)
        return 1
    elif place_check == 1: # go left
        if verb: print('going left on x {} y {}'.format(next_one_index, x))
        return fall_from(m, next_one_index, x-1, tmp_count, verb)
    else: # go right
        if verb: print('going right on x {} y {}'.format(next_one_index, x))
        return fall_from(m, next_one_index, x+1, tmp_count, verb)

d = 14 # day problem number
with open('inputd{}.txt'.format(d), 'r') as f:
    lines = f.readlines()
    
s=0
s2=1

verb=False # pass True to visualize (raw numpy)
subx=0
all_points=[]

for line in lines:
    tmp=[]
    for po in line.strip().replace(" ", "").split('->'):
        conved = list(map(int, po.split(',')))
        conved[0] = conved[0] - subx
        conved[0], conved[1] = conved[1], conved[0]
        tmp.append(tuple(conved))
    all_points.append(tmp)

xs = list(zip(*flatten(all_points)))[1]
ys = list(zip(*flatten(all_points)))[0]

base, height = max(xs)*2, max(ys)+3
m = np.zeros([height, base])

m[0, 500-subx] = 8 # sand falling point

for stl in all_points:
    for i in range(len(stl)-1):
        draw_rock_line(stl[i], stl[i+1])

m2 = m.copy()
m2[height-1, :] = 1

# part one
while fall_from(m, 0, 500-subx, 0, verb) == 1:
    s+=1
#part two
while fall_from(m2, 0, 500-subx, 0, verb) == 1:
    s2+=1

print('Part one:')
print(s)

print('*-'*30)

print('Part Two:')
print(s2)
