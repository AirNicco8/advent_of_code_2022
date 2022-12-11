import math

def proc_line(line):
        return line[:-1].strip()

def Karatsuba(x, y):
    if x < 10 and y < 10:
        return x * y

    num1_len = len(str(x))
    num2_len = len(str(y))

    n = max(num1_len,num2_len)

    # round decides to be floor or ceil value
    # by this we can reduce some function calls
    # of ceil or floor recursively
    nby2 = round(n/2)

    num1 = x // (10 ** nby2)
    rem1 = x % (10 ** nby2)

    num2 = y // (10 ** nby2)
    rem2 = y % (10 ** nby2)

    ac = Karatsuba(num1, num2)
    bd = Karatsuba(rem1, rem2)
    ad_plus_bc = Karatsuba(num1 + rem1, num2 + rem2) - ac - bd

    return (10 ** (2*nby2))*ac + (10 ** nby2)*ad_plus_bc + bd

global monkeys, comdiv

class Monkey():
    def __init__(self, id, objects, operation, param1, param2, test, truem, falsem):
        self.id = id
        self.objects = objects
        self.operation = operation
        self.param1 = param1
        self.param2 = param2
        self.test = test
        self.true_monkey = truem
        self.false_monkey = falsem


        self.inspections = 0

    def execute_turn(self, pt):
        tmp_objs = range(len(self.objects))

        for obj in tmp_objs:
            curr_obj = self.objects.pop()
            self.inspections += 1

            curr_obj = self.worry_op(curr_obj)

            curr_obj = math.floor(curr_obj/3) if pt == 1 else curr_obj

            cond = bool(curr_obj % self.test == 0)

            if cond:
                monkeys[self.true_monkey].objects.insert(0, curr_obj)
            else:
                monkeys[self.false_monkey].objects.insert(0, curr_obj)

    def worry_op(self, curr):
        if self.param2 != 'old':
            if self.operation == '*':
                return Karatsuba(curr, self.param2) % comdiv
            else: # sum
                return curr + self.param2 % comdiv
        else:
            if self.operation == '*':
                return Karatsuba(curr, curr) % comdiv
            else: # sum
                return curr + curr % comdiv

d = 11 # day problem number
with open('inputd{}.txt'.format(d), 'r') as f:
    lines = f.readlines()

s=0

comdiv=1

monkeys=[]
ins=[]
lc=0

for line in lines: 
    if lc == 0:
        line=proc_line(line)
        mid = int(''.join(filter(str.isdigit, line.split()[1])))
        lc+=1
    elif lc == 1:
        line=proc_line(line)
        objs = list(map(int, line.split(':')[1].split(',')))
        objs.reverse()
        lc+=1
    elif lc == 2:
        line=proc_line(line)
        op = line.split('=')[1].split()
        if op[2] != 'old':
            op[2] = int(op[2])
        lc+=1
    elif lc == 3:
        line=proc_line(line)
        test = int( ''.join(filter(str.isdigit, line)))
        lc+=1
    elif lc == 4:
        line=proc_line(line)
        truem = int( ''.join(filter(str.isdigit, line)))
        lc+=1
    elif lc == 5:
        line=proc_line(line)
        falsem = int( ''.join(filter(str.isdigit, line)))
        lc+=1
    else:
        newmonkey = Monkey(mid, objs, op[1], op[0], op[2], test, truem, falsem)
        monkeys.append(newmonkey)
        comdiv*=test
        lc = 0

part = 2  # set to 1 for part one, 2 for part 2
rounds = range(10000) if part == 2 else range(20)

#part one/two
for rou in rounds:
    for monkey in monkeys:
        monkey.execute_turn(part)

for monkey in monkeys:
    ins.append(monkey.inspections)

ins.sort()
    
s = ins[-2]*ins[-1]


print('Part {}:'.format(part))
print(s)

print('*-'*30)
