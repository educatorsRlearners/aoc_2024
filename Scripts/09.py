data = "data/09_data.txt"

F, S, p = [], [], 0
for i, c in enumerate(open(data).read().strip()):
    [F, S][i % 2] += [[*range(p, p := p + int(c))]]
S = sum(S, [])
for f in reversed(F):
    for x in reversed(range(len(f))):
        if len(S) and f[x] > S[0]:
            f[x] = S[0]
            S = S[1:]

pt_1 = sum((i * j) for i, f in enumerate(F) for j in f)

# Part 2
F, S, p = [], [], 0
for i, c in enumerate(open(data).read().strip()):
    [F, S][i % 2] += [[*range(p, p := p + int(c))]]
for y in reversed(range(len(F))):
    for x in range(len(S)):
        if len(S[x]) >= len(F[y]) and F[y][0] > S[x][0]:
            F[y] = S[x][: len(F[y])]
            S[x] = S[x][len(F[y]) :]

pt_2 = sum((i * j) for i, f in enumerate(F) for j in f)

print(f" The solution to part 1 is: {pt_1} and part 2 is: {pt_2}")
