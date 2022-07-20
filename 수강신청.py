import sys
input=sys.stdin.readline

N,M = input().split()
graph = {}
for _ in range(int(M)):
    studentId = input().rstrip()
    graph[studentId] = _
sorted_dict = dict(sorted(graph.items(), key = lambda item: item[1]))

for i in list(sorted_dict.keys())[:int(N)]:
    print(i)
