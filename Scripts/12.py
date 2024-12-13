from numpy import array, count_nonzero, unique
from scipy.ndimage import label
from scipy.signal import convolve2d

input = "data/12_data.txt"

G = array([list(l.strip()) for l in open(input)])

ans = array([0, 0])

labels_and_counts = []
for g in unique(G):
    L, n = label(G == g)
    labels_and_counts.append((L, n))

for L, n in labels_and_counts:
    for i in range(n):
        H = L == i + 1

        h = count_nonzero(convolve2d(H, [[1, -1]]))
        v = count_nonzero(convolve2d(H, [[1], [-1]]))
        x = abs(convolve2d(H, [[-1, 1], [1, -1]]))

        ans += H.sum() * array([h + v, x.sum()])

print(*ans)
