class Counter():
    def __init__(self):
        self.X = 1
        self.ticks = 0
        self.opmap={'noop':1, 'addx':2}
        self.sigsum=0
        self.line=0

    def op(self, op_tuple):
        if(self.opmap[op_tuple[0]] == 1):
            self.ticks+=1
            self.retcycle()
            self.printp()
        else:
            self.ticks+=1
            # print('Start cycle {} - X is {}'.format(self.ticks, self.X))
            self.retcycle()
            self.printp()

            self.ticks+=1
            # print('Start cycle {} - X is {}'.format(self.ticks, self.X))
            self.retcycle()   
            self.printp()

            self.X+=int(op_tuple[1]) # update after a cycle

    def retcycle(self): # part one
        if((self.ticks-20)%40==0):
            self.sigsum+=(self.ticks*self.X)

    def check_sprite(self):
        cond = (self.ticks-1-40*self.line) in range(self.X-1, self.X+2)
        return cond
        
    def printp(self): # part two
        if self.check_sprite():
            print('#', end='')
        else:
            print('.',end ='')

        if(self.ticks%40==0):
            self.line+=1
            print('')
            
d = 10 # day problem number
with open('inputd{}.txt'.format(d), 'r') as f:
    lines = f.readlines()

s=0
opstack=[]

for line in lines:
    line = line[:-1]
    opstack.append(line.split())
    
opstack.reverse()
totops = len(opstack)

counter = Counter()

print('Part Two:')

for op in range(totops):
    counter.op(opstack.pop())

s = counter.sigsum

print('*-'*30)
print('Part one:')
print(s)

