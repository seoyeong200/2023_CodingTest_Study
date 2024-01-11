import heapq
import sys
input = sys.stdin.readline
V, E = map(int, input().strip().split())
st = int(input().strip())
adj = [[] for _ in range(V+1)]
while E:
    E -= 1
    u, v, w = map(int, input().strip().split())
    adj[u].append((w, v))
    
d = [int(1e9) for _ in range(V+1)]
d[st] = 0
pq = []
heapq.heappush(pq, (0, st))
while pq:
    weight, curV = heapq.heappop(pq)
    if d[curV] != weight:
        continue
    for nextWeight, nextV in adj[curV]:
        if d[nextV] <= d[curV] + nextWeight:
            continue
        d[nextV] = d[curV] + nextWeight
        heapq.heappush(pq, (d[nextV], nextV))

for i in range(1, V+1):
    if d[i] == int(1e9):
        print("INF")
        continue
    print(d[i])
