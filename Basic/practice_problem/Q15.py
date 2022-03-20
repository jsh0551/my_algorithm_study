from collections import deque

def bfs(graph,node,visited,queue,k_dict):
    visited[node] = True
    queue.append(node)
    distance = 0
    while queue:
        node = queue.popleft()
        distance += 1
        for i in graph[node]:
            queue.append(i)
            if not visited[i]:
                visited[i] = True
                k_dict[i] = distance


n,m,k,x = map(int,input().split(" "))

graph = [[] for _ in range(n+1)]
k_dict={}
for j in range(m):
    i,v = map(int,input().split(" "))
    graph[i].append(v) 
    k_dict[j+1] = -1
visited = [False]*(n+1)
queue=deque()
bfs(graph,x,visited,queue,k_dict)

result = []
for key,value in k_dict.items():
    if value == k:
        result.append(str(key))
if result:
    print(" ".join(result))
else:
    print("-1")

