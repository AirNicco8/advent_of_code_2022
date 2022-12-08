import numpy as np

d = 8 # day problem number
with open('inputd{}.txt'.format(d), 'r') as f:
    lines = f.readlines()

s=0
s2=[]
na = []
vs=0

for line in lines:
    ar = [c for c in list(line[:-1])]
    na.append([v for v in map(int, ar)])

m = np.matrix(na)
height = m.shape[0]
base = m.shape[1]

print(m)
# part one
for i in range(1, base-1):
    for j in range(1, height-1):
        val = m[i,j]
        rests=[m[i,:j], m[i,j+1:], m[:i,j], m[i+1:,j]] # left, right, up, down
        checks = [(r>=val).any() for r in rests] # controllo visibilità

        if not all(checks):
            vs+=1
        
s = base*2 + height*2 - 4 + vs 
# perimetro meno angoli + interiori

# part two
for i in range(base):
    for j in range(height):
        val = m[i,j]
        rests=[np.flip(m[i,:j].A1), m[i,j+1:].A1, np.flip(m[:i,j].A1), m[i+1:,j].A1] # left, right, up, down
        inds = {}
        er=[]
        azzera=False

        for n in range(len(rests)):
            if rests[n].any():
                wh = np.where(rests[n]>= val)[0]

                er.append(n)
                if(wh.size == 0):
                    inds[n]=len(rests[n])-1
                else:
                    inds[n]=wh[0]
            else:
                azzera=True

        if er:
            prevs = [len(np.split(rests[o], [inds[o]])[0])+1 for o in er]

            if azzera:
                s2.append(0)
            else:
                s2.append(np.prod(prevs))

print('Part one:')
print(s)

print('*-'*30)

print('Part Two:')
print(max(s2))