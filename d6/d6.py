d = 6 # day problem number
with open('inputd{}.txt'.format(d), 'r') as f:
    lines = f.readlines()

def marker(msg, n):
    for i in range(0, len(msg)-n-1):
        if len(set(line[i:i+n])) == n: # controllo i possibili marker
            return i+n 

s=0
s2=0
line = lines[0]

s4=[]

# part one
s = marker(line, 4)

# part two
s2 = marker(line, 14)
    
print('Part one:')
print(s)

print('*-'*30)

print('Part Two:')
print(s2)
