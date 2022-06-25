from collections import deque
from tabnanny import check

n = int(input())
hallway_map = []
for i in range(n):
    tmp_row = list(input().split(" "))
    hallway_map.append(tmp_row)

def where_teacher(hallway_map):
    teachers = []
    for i,row in enumerate(hallway_map):
        for j,p in enumerate(row):
            if p == 'T':
                teachers.append((i,j))
    return teachers

move = [(-1,0),(1,0),(0,-1),(0,1)]

def check_student(hallway_map,i,j):
    # global hallway_map
    is_student = False
    loop_end = False
    for m in move:
        for scale in range(1,n):
            ni = i + scale*m[0]
            nj = j + scale*m[1]
            if 0<=ni<n and 0<=nj<n:
                if hallway_map[ni][nj] == 'S':
                    is_student = True
                    loop_end = True
                    break
                elif hallway_map[ni][nj] == 'O':
                    break
        if loop_end:
            break
    
    return is_student

answer = 0

teachers = where_teacher(hallway_map)
def dfs(row,col,count):
    global hallway_map,answer,teachers
    if count == 3:
        ## check student
        check_answer = False
        for teacher in teachers:
            i,j = teacher
            if check_student(hallway_map,i,j):
                check_answer = True
                break
        if not check_answer:
            answer+=1
        return
    else:
        for i in range(n):
            for j in range(n):
                ni = i
                nj = j
                if hallway_map[ni][nj] == 'X':
                    count+=1
                    hallway_map[ni][nj] = 'O'
                    dfs(ni,nj,count)
                    hallway_map[ni][nj] = 'X'
                    count-=1

dfs(0,0,0)
if answer==0:
    print("NO")
else:
    print("YES")