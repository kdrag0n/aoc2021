import sys

with open(sys.argv[1], 'r') as f:
    file_lines = [l for l in f.read().strip().split('\n')]

di = -1
progs = [[] for i in range(14)]
for l in file_lines:
    parts = l.split()
    inst = parts[0]
    var = parts[1]
    if inst == 'inp':
        di += 1
        progs[di] += [f'{var} = d;']
        continue
    v2 = parts[2]
    if inst == 'add':
        progs[di] += [f'{var} += {v2};']
    elif inst == 'mul':
        progs[di] += [f'{var} *= {v2};']
    elif inst == 'div':
        progs[di] += [f'{var} /= {v2};']
    elif inst == 'mod':
        progs[di] += [f'{var} %= {v2};']
    elif inst == 'eql':
        progs[di] += [f'{var} = {var} == {v2} ? 1 : 0;']
    else:
        raise ValueError(l)

for i, lines in enumerate(progs):
    print(f'''static int run_prog{i}(int z, int d) {'{'}
    int x = 0;
    int y = 0;
    int w = 0;
''')
    for l in lines:
        print(l)
    print('''    return z;
}
''')
