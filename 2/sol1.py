with open('in') as f:
	lines = f.readlines()
horiz = 0
depth = 0
for x in lines:
    x = x.strip().split(' ')
    cmd = x[0]
    amt = int(x[1])
    if cmd == 'forward':
        horiz += amt
    elif cmd == 'down':
        depth += amt
    elif cmd == 'up':
        depth -= amt
print(horiz*depth)
