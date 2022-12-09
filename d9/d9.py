import numpy as np

def make_h_step(dir, pos):
    if dir == 'R':
        return (pos[0], pos[1]+1)
    elif dir == 'U':
        return (pos[0]-1, pos[1])
    elif dir == 'L':
        return (pos[0], pos[1]-1)
    elif dir == 'D':
        return (pos[0]+1, pos[1])

def make_d_step(dir, tpos, hpos):
    if dir == 'R':
        return (hpos[0], tpos[1]+1)
    elif dir == 'U':
        return (tpos[0]-1, hpos[1])
    elif dir == 'L':
        return (hpos[0], tpos[1]-1)
    elif dir == 'D':
        return (tpos[0]+1, hpos[1])

def make_dd_step(hdiff, wdiff, tpos):
    if hdiff==2 and wdiff==2:
        return (tpos[0]+1, tpos[1]+1)
    elif hdiff==-2 and wdiff==2:
        return (tpos[0]-1, tpos[1]+1)
    elif hdiff==-2 and wdiff==-2:
        return (tpos[0]-1, tpos[1]-1)
    else:
        return (tpos[0]+1, tpos[1]-1)

d = 9 # day problem number
with open('inputd{}.txt'.format(d), 'r') as f:
    lines = f.readlines()

s=0
s2=0
movstack=[]

for line in lines:
    line=line[:-1]
    movstack.append((line.split()[0], int(line.split()[1])))

max_wh = sum(list(zip(*movstack))[1])
st = int(max_wh/2)

visitmap = np.zeros((max_wh, max_wh)) # map for visited cells, height x width
visitmap[st,st]=1
visitstack=[]

movstack.reverse()
movstack2 = movstack.copy()
totmovs = len(movstack)

# part one
head_pos = (st,st)
tail_pos = (st,st)

for mov in range(totmovs):
    dir, steps = movstack.pop()

    for step in range(steps):
        head_pos = make_h_step(dir, head_pos)

        if(abs(head_pos[0]-tail_pos[0]) > 1) or (abs(head_pos[1]-tail_pos[1]) > 1):
            if head_pos[0]==tail_pos[0] or head_pos[1]==tail_pos[1]:
                tail_pos = make_h_step(dir, tail_pos)
            else:
                tail_pos = make_d_step(dir, tail_pos, head_pos)
            visitmap[tail_pos]=1

unique, counts = np.unique(visitmap, return_counts=True)
s=counts[1]

# part two
visitmap9 = np.zeros((max_wh, max_wh)) # map for visited cells, height x width
visitmap9[st,st]=1
snake_pos = [(st,st) for _ in range(10)]

for mov in range(totmovs):
    dir, steps = movstack2.pop()

    for step in range(steps):
        snake_pos[0] = make_h_step(dir, snake_pos[0])
        for knot in range(0, len(snake_pos[:-1])):

            if(abs(snake_pos[knot][0]-snake_pos[knot+1][0]) > 1) or (abs(snake_pos[knot][1]-snake_pos[knot+1][1]) > 1):
                if snake_pos[knot][0]==snake_pos[knot+1][0] or snake_pos[knot][1]==snake_pos[knot+1][1]:
                    if(snake_pos[knot][0]==snake_pos[knot+1][0]): # same height
                        tdir = 'L' if (snake_pos[knot][1]-snake_pos[knot+1][1])<0 else 'R'
                    if(snake_pos[knot][1]==snake_pos[knot+1][1]): # same width
                        tdir = 'U' if (snake_pos[knot][0]-snake_pos[knot+1][0])<0 else 'D'
                    snake_pos[knot+1] = make_h_step(tdir, snake_pos[knot+1])
                else:
                    hdiff = snake_pos[knot][0]-snake_pos[knot+1][0] # h increase down
                    wdiff = snake_pos[knot][1]-snake_pos[knot+1][1] # w increase right

                    if abs(hdiff) > 1:
                        tdir = 'D' if hdiff == 2 else 'U'
                    if abs(wdiff) > 1:
                        tdir = 'R' if wdiff == 2 else 'L'

                    if(abs(wdiff)==2 and abs(hdiff)==2):
                        snake_pos[knot+1] = make_dd_step(hdiff, wdiff, snake_pos[knot+1])
                    else:
                        snake_pos[knot+1] = make_d_step(tdir, snake_pos[knot+1], snake_pos[knot])
            if knot == 8:
                    visitmap9[snake_pos[knot+1]]=1

unique2, counts2 = np.unique(visitmap9, return_counts=True)
s2=counts2[1]


print('Part one:')
print(s)

print('*-'*30)

print('Part Two:')
print(s2)
