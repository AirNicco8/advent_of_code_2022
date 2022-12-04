with open('inputd2.txt', 'r') as f:
    lines = f.readlines()

t1 = {'X':'A','Y':'B', 'Z':'C'} # rock, paper, scissors

t2 = {'X':0,'Y':3, 'Z':6} # lose, draw, win

val = {'A':1, 'B':2, 'C':3}

w = {'A':'C', 'B':'A', 'C':'B'}
los = {'A':'B', 'B':'C', 'C':'A'}

def res(a,b):
    if a == b:
        return 3
    if b == w[a]:
        return 6
    else:
        return 0

def revres(a,b): # devo tornare il valore che ha outcome b contro a
    if b == 3:
        return a
    if b == 6:
        return los[a]
    else:
        return w[a]

l=0
l2=0
for line in lines:
    outcomes = line.split()

    # part one
    dec = t1[outcomes[1]]
    
    out = res(dec, outcomes[0])

    l+=(out+val[dec])

    # part two
    dec2 = t2[outcomes[1]]

    top = revres(outcomes[0], dec2)

    l2+=(dec2+val[top])
    
print('Part one:')
print(l)

print('*-'*30)


print('Part Two:')
print(l2)