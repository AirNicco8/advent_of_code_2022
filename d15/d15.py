import re
from tqdm import tqdm

numbers = re.compile('-?\d+')

def manhattan(a, b):
    distance = 0
    for x1, x2 in zip(a, b):
        difference = x2 - x1
        absolute_difference = abs(difference)
        distance += absolute_difference

    return distance

def tuning_freq(p):
    return p[0]*4000000+p[1]

def get_digit(s):
    return list(map(int, numbers.findall(s)))[0]

def inspect(starts, ends):
    if not 0 in starts:
        return 0
    if not maximum_area in ends: 
        return maximum_area
    
    for rr in ends:
        if rr != maximum_area:
            ok = True
            for idx, ss in enumerate(starts):
                if (ss <= rr) and (ends[idx] > rr):
                    ok=False
            if ok: 
                return rr+1
    
    return -1


d = 15 # day problem number
with open('inputd{}.txt'.format(d), 'r') as f:
    lines = f.readlines()

s=0
s2=0

sensors=[]
beacons=[]

for line in lines:
    sb = line[:-1].split(':')
    sens = sb[0].split(',')
    bea = sb[1].split(',')

    sensors.append([get_digit(sens[0]),get_digit(sens[1])])
    beacons.append([get_digit(bea[0]),get_digit(bea[1])])

# part one
line_to_check = 2000000
occupied_positions = set()
beacons_xs = set()

for i in range(len(sensors)):
    sensor = sensors[i]
    beacon = beacons[i]
    m = manhattan(sensor, beacon)

    if beacon[1] == line_to_check: # if there is already a beacon in the position we do not count it
        beacons_xs.add(beacon[0])

    if(line_to_check in range(sensor[1]-m, sensor[1]+m+1)): # if line intersect the rhombus
        diff = abs(line_to_check-sensor[1])
        occupied_positions.update(set(range(sensor[0]-m+diff, sensor[0]+m-diff+1))) # get the wideness of the luck in the given y

occupied_positions = occupied_positions - beacons_xs
s = len(occupied_positions) # number of positions

# part two
maximum_area = 4000000

for j in tqdm(range(maximum_area+1)):
    extremes = []
    for i in range(len(sensors)):
        sensor = sensors[i]
        beacon = beacons[i]
        m = manhattan(sensor, beacon)

        if (j in range(sensor[1]-m, sensor[1]+m+1)): # if line intersect the rhombus
            diff = abs(j-sensor[1])
            left_bound = sensor[0]-m+diff if (sensor[0]-m+diff) >= 0 else 0
            right_bound = sensor[0]+m-diff if (sensor[0]+m-diff) <= maximum_area else maximum_area

            extremes.append((left_bound, right_bound)) # get the extremes of the rhombus in the given y
    
    starts = list(zip(*extremes))[0]
    ends = list(zip(*extremes))[1]

    outcome = inspect(starts, ends) # returns the free x coordinate or -1

    if outcome != -1: break

free_point = (outcome, j)
s2 = tuning_freq(free_point)

print('Part one:')
print(s)

print('*-'*30)

print('Part Two:')
print(s2)
