import sys
num_steps = int(sys.argv[1])

for step in range(num_steps - 1, -1, -1):
    r = ''
    for n in range(0, num_steps):
        r += '#' if n >= step else ' '
    print(r)