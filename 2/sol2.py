with open('in') as f:
	lines = f.readlines()
horiz = 0
depth = 0
aim = 0
for x in lines:
    x = x.strip().split(' ')
    cmd = x[0]
    amt = int(x[1])
    if cmd == 'forward':
        horiz += amt
        depth += aim*amt
    elif cmd == 'down':
        aim += amt
    elif cmd == 'up':
        aim -= amt
print(horiz*depth)
