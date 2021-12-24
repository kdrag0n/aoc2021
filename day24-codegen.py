import sys

with open(sys.argv[1], 'r') as f:
    file_lines = [l for l in f.read().strip().split('\n')]
print('''static __attribute__((noinline)) int run_prog(int d0, int d1, int d2, int d3, int d4, int d5, int d6, int d7, int d8, int d9, int d10, int d11, int d12, int d13) {
    int x = 0;
    int y = 0;
    int z = 0;
    int w = 0;
''')
ds = [f'd{i}' for i in range(14)]
vars = {'x', 'y', 'z', 'w'}
for l in file_lines:
    parts = l.split()
    inst = parts[0]
    var = parts[1]
    if inst == 'inp':
        v2 = ds[0]
        ds = ds[1:]
        print(f'{var} = {v2};')
        continue
    v2 = parts[2]
    if inst == 'add':
        print(f'{var} += {v2};')
    elif inst == 'mul':
        print(f'{var} *= {v2};')
    elif inst == 'div':
        print(f'{var} /= {v2};')
    elif inst == 'mod':
        print(f'{var} %= {v2};')
    elif inst == 'eql':
        print(f'{var} = {var} == {v2} ? 1 : 0;')
    else:
        raise ValueError(l)

print('''   return z;
}
''')
