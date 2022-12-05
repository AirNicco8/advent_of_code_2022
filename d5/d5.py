import math
import re
import copy

d = 5 # day problem number
with open('inputd{}.txt'.format(d), 'r') as f:
    lines = f.readlines()

s=''
s2=''
div = False

nstacks = int(len(lines[0])/4) # numero di colonne di casse
stacks = {} # elemento i sarà una lista di casse [X]

for k in range(nstacks):
    stacks[k+1]=list()

for line in lines:
    c3=-1

    if(any(char.isdigit() for char in line) and not div):
            for lis in stacks:
                stacks[lis].reverse()
            stacks2 = copy.deepcopy(stacks)
            div = True

    if not div: # parte delle crates, popolo stacks
        for i in line[:-1]:
            c3+=1
            ind3 = math.floor(c3/4)
            if i != ' ' and i != '[' and i != ']':
                stacks[ind3+1].append(i)
    else: # parte delle actions
        if(any(char.islower() for char in line)): # bypasso righe non utili
            nums = list(map(int, re.findall('\d+', line)))

            nmove = nums[0]
            froms = nums[1]
            tos = nums[2]

            revmove = stacks[froms][-nmove:] # crates da muovere
            revmove2 = stacks2[froms][-nmove:] # crates da muovere

            # part two
            stacks2[tos].extend(revmove2)
            
            # part one
            revmove.reverse()
            stacks[tos].extend(revmove) # appendo a destinazione

            del stacks[froms][-nmove:] # rimuovo da partenza
            del stacks2[froms][-nmove:] # rimuovo da partenza

for st in stacks:
    s+=stacks[st][-1]

for st in stacks2:
    s2+=stacks2[st][-1]

print('Part one:')
print(s)

print('*-'*30)


print('Part Two:')
print(s2)
