with open('inputd1.txt', 'r') as f:
    lines = f.readlines()

a=0
d={}

for i in lines:
    if i != '\n':
        v = int(i.strip())
        try:
            d[a].append(v)
        except:
            d[a] = [v]
    else:
        a+=1

tots = [sum(v) for v in d.values()]

m = max(tots)

tots.sort()

print('Part One:')
print(m)

print('*-'*30)

print('Part Two:')
print(sum(tots[-3:]))
        