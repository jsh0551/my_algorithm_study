from collections import deque

n = int(input())

room_list = []
max_num = 0
check_list = [0]*n
for i in range(n):
    tmp_room = list(map(int,input().split(" ")))
    room_list.append(tmp_room)
    
room_list.sort()
room_list.sort(key = lambda x : x[1])

start,end = room_list[0]
count = 1
for i in range(1,n):
    if room_list[i][0]>=end:
        start,end = room_list[i]
        count += 1

print(count)