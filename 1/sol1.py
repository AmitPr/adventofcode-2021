with open('in') as f:
	lines = f.readlines()
	lines = [int(x.strip()) for x in lines]
inc = 0
for i in range(1,len(lines)):
	if lines[i] > lines[i-1]:
		inc+=1
print(inc)