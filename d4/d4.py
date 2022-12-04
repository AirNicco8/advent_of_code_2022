d = 4 # day problem number
with open('inputd{}.txt'.format(d), 'r') as f:
    lines = f.readlines()

s=0
s2=0
for line in lines:
    sections = line[:-1].split(',')

    # part one
    ext1 = list(map(int, sections[0].split('-'))) 
    ext2 = list(map(int, sections[1].split('-'))) 
    
    r1 = set(range(ext1[0], ext1[1]+1))
    r2 = set(range(ext2[0], ext2[1]+1))

    if (r1.issubset(r2) or r2.issubset(r1)):
        s+=1


    # part two
    if bool(r1.intersection(r2)):
        s2+=1

print('Part one:')
print(s)

print('*-'*30)


print('Part Two:')
print(s2)