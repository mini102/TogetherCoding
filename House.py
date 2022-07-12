import sys
from collections import deque
input=sys.stdin.readline

N = int(input())

answer =[]

graph = []
visited = [[] for _ in range(N)]

for _ in range(N):
    graph.append(list(str(input()[:-1])))
    for p in range(N):
        visited[_].append(False)

# print(graph)
# print(visited)

countOfArea = 0

nx = [-1, 1, 0, 0] 
ny = [0, 0, -1, 1]
queue = deque()

for k in range(N):
    for j in range(N):
        if graph[k][j]=='1'and visited[k][j]==False:
            countOfArea+=1
            queue.append([k,j])
            visited[k][j]=True
            cnt =0 
            while queue:
                x,y = queue.popleft()
                for i in range(4):
                    dx = x+nx[i]
                    dy = y+ny[i]
                    if 0<=dx<N and 0<=dy<N and graph[dx][dy]=='1' and visited[dx][dy]==False:
                        visited[dx][dy]=True
                        queue.append([dx,dy])
                cnt+=1
            answer.append(cnt)
        
answer.sort()
answer.insert(0,countOfArea)
for a in answer:
    print(a)
