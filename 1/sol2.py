with open('in') as f:
	lines = f.readlines()
	lines = [int(x.strip()) for x in lines]

inc = 0
for i in range(1,len(lines)-2):
    if sum(lines[i:i+3]) > sum(lines[i-1:i+2]):
        inc += 1
print(inc)