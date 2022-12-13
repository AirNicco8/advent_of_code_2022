from parsimonious.grammar import Grammar
from parsimonious.nodes import NodeVisitor
from functools import cmp_to_key

grammar = Grammar(
    r"""
    document   = line*
    line       = whitespace? item (whitespace item)* whitespace? eol
    item       = group / number / empty
    group      = "[" item (comma item)* whitespace? "]"
    comma      = whitespace? "," whitespace?
    number     = "NaN" / ~"[0-9.]+"
    whitespace = ~" +"
    empty      = ""
    eol        = ~"\r?\n" / eof
    eof        = ~"$"
    """)

class DataExtractor(NodeVisitor):
    @staticmethod
    def concat_items(first_item, remaining_items):
        """ helper to concat the values of delimited items (lines or goups) """
        return first_item + list(map(lambda i: i[1][0], remaining_items))

    def generic_visit(self, node, processed_children):
        """ in general we just want to see the processed children of any node """
        return processed_children

    def visit_line(self, node, processed_children):
        """ line nodes return an array of their processed_children """
        _, first_item, remaining_items, _, _ = processed_children
        return self.concat_items(first_item, remaining_items)

    def visit_group(self, node, processed_children):
        """ group nodes return an array of their processed_children """
        _, first_item, remaining_items, _, _ = processed_children
        return self.concat_items(first_item, remaining_items)

    def visit_number(self, node, processed_children):
        """ number nodes return floats (nan is a special value of floats) """
        return int(node.text)

    def visit_empty(self, node, processed_children):
        """ number nodes return floats (nan is a special value of floats) """
        return ''

def check_int(v1,v2):
    return (isinstance(v1, int) and isinstance(v2, int))

def check_list(v1,v2):
    return (isinstance(v1, list) and isinstance(v2, list))

def check_diff(v1,v2):
    return (isinstance(v1, list) and isinstance(v2, int))

def check_empty(v1,v2):
    return (v1 == '') or (v2 == '')

def compare(l): # compare lists
    left = l[0]
    right = l[1]

#    print(left, right)
    # 1 is correct input, 2 is incorrect
    if check_int(left, right):
        if left < right: return 1
        elif left > right: return 2
        else: return 0
    elif check_list(left,right):
        cum=[]
        for j in range(min(len(left), len(right))):
            cum.append(compare((left[j], right[j]))) 
            if cum[-1] > 0: break
        if cum[-1] == 0:
            if len(left) != len(right):
                return 1 if len(left) < len(right) else 2
            else:
                return 0
        else:
            return cum[-1]
    else:
        if left =='' and right == '':
            return 0
        if left == '':
            return 1
        if right == '':
            return 2
        if check_diff(left, right):
            return compare((left, [right]))
        else:
            return compare(([left], right))

def custom_comp(item1, item2):
    if compare([item1,item2]) == 1: #item1) < fitness(item2):
        return -1
    elif compare([item1,item2]) == 2: #fitness(item1) > fitness(item2):
        return 1
    else:
        return 0


d = 13 # day problem number
# with open('inputd{}.txt'.format(d), 'r') as f:
#     lines = f.readlines()

with open('inputd{}.txt'.format(d), encoding='utf-8') as f:
    text = f.read().split()

# with open('duminput.txt', encoding='utf-8') as f:
#     text = f.read().split()

s=0
s2=0
prog=1
correctness=[]
all_packets=[]

# part one
for i in range(0, len(text), 2):
    tp = text[i]+'\n'+text[i+1]
    de = DataExtractor()

    tree = grammar.parse(tp)
    data = de.visit(tree)

    all_packets.append(data[0][0])
    all_packets.append(data[1][0])

    pair = [data[0][0], data[1][0]]

    if compare(pair) == 1:
        correctness.append(prog)

    prog+=1
    
s = sum(correctness)

# part two
prog=1
all_packets.append([[2]])
all_packets.append([[6]])

all_packets = sorted(all_packets, key=cmp_to_key(custom_comp))

for aa in all_packets:
    if aa == [[2]]:
        s2=prog
    if aa == [[6]]:
        s2*=prog
        break
    prog+=1

print('Part one:')
print(s)

print('*-'*30)

print('Part Two:')
print(s2)
