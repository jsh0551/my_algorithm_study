from collections import deque

n,k = map(int,input().split(" "))
virus_map = []
for _ in range(n):
    tmp_row = list(map(int,input().split(" ")))
    virus_map.append(tmp_row)
time,x,y = map(int,input().split(" "))
move_list = [(-1,0),(1,0),(0,-1),(0,1)]

data = deque()

for virus_type in range(1,k+1):
    for i in range(n):
        for j in range(n):
            if virus_map[i][j] == virus_type:
                data.append((virus_map[i][j],0,i,j))


while data:
    virus_type,t,i,j = data.popleft()

    if t == time:
        break
    for di,dj in move_list:
        ni=i+di
        nj=j+dj
        if 0<=ni<n and 0<=nj<n:
            if virus_map[ni][nj] == 0:
                virus_map[ni][nj] = virus_type
                data.append((virus_type,t+1,ni,nj))


print(virus_map[x-1][y-1])
