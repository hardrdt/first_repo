size = 5
for raw in range(size):
    col = size - raw - 1
    if raw == 0 or raw == size - 1:
        print(' ' * col + '#' * (raw + 1))
    else:
        print(' ' * col + '#' * raw)

for _ in range(size - 2):
    print()

for raw in range(size - 1, 0, -1):
    col = size - raw - 1
    if raw == 0 or raw == size - 1:
        print(' ' * col + '#' * (raw + 1))
    else:
        print(' ' * col + '#' * raw)

print('#######')