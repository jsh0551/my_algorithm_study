from collections import deque
n,m = map(int,input().split(" "))
virus_map = []
for i in range(n):
    virus_map.append(list(map(int,input().split(" "))))


dx = [1,0,-1,0]
dy = [0,1,0,-1]

start_map=[row.copy() for row in virus_map]
temp_map=[row.copy() for row in virus_map]
max_virus = 0
where_virus = []
for i in range(n):
    for j in range(m):
        if start_map[i][j] == 2:
            where_virus.append((i,j))


def virus(x,y):
    
    global temp_map
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if temp_map[nx][ny]==0:
                temp_map[nx][ny]=2
                virus(nx,ny)

def dfs(count):
    global max_virus,start_map,temp_map
    if count==3:
        for i in range(n):
            for j in range(m):
                temp_map[i][j] = start_map[i][j]
        for virus_start in where_virus:
            virus(virus_start[0],virus_start[1])
        max_virus = max(max_virus,sum([row.count(0) for row in temp_map]))
        
    else:
        for i in range(n):
            for j in range(m):
                if start_map[i][j] == 0:
                    count+=1
                    start_map[i][j] = 1
                    dfs(count)
                    count-=1
                    start_map[i][j] = 0
                else:
                    continue


dfs(0)
print(max_virus)



