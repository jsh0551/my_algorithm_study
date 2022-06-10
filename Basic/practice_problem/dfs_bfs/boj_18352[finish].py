from collections import deque

def bfs(graph,node,visited,queue,k_list):
    visited[node] = True
    queue.append(node)
    distance = 0
    k_list[node] = distance
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                k_list[i] = k_list[node]+1
                queue.append(i)



n,m,k,x = map(int,input().split(" "))

graph = [[] for _ in range(n+1)]
k_list=[-1]*(n+1)
for j in range(m):
    i,v = map(int,input().split(" "))
    graph[i].append(v) 

visited = [False]*(n+1)
queue=deque()
bfs(graph,x,visited,queue,k_list)

result = []
for i in range(1,len(k_list)):
    if k_list[i] == k:
        result.append(i)

if result:
    for r in result:print(r)
else:
    print(-1)

