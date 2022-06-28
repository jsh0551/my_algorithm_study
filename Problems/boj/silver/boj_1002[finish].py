
n = int(input())

answer = []

for i in range(n):
    x1,y1,r1,x2,y2,r2 = list(map(int,input().split(" ")))
    distance = int((x1-x2)**2 + (y1-y2)**2)
    large_r = int((r1 + r2)**2)
    small_r = int((r1 - r2)**2)
    if r1==r2:
        if distance>large_r:
            answer.append("0")
        elif distance==large_r:
            answer.append("1")
        else:
            if x1==x2 and y1==y2:
                answer.append("-1")
            else:
                answer.append("2")
    else:
        if distance>large_r:
            answer.append("0")
        elif distance==large_r:
            answer.append("1")
        elif large_r>distance>small_r:
            answer.append("2")
        elif distance==small_r:
            answer.append("1")
        else:
            answer.append("0")

for n in answer:
    print(n)