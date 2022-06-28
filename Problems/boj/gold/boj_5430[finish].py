from collections import deque

t = int(input())
orders = []
len_list = []
array_list = []
for i in range(t):
    orders.append(list(input()))
    len_list.append(int(input()))
    tmp_list = list(input()[1:-1].split(","))
    if len(tmp_list) == 1 and len(tmp_list[0]) == 0:
        tmp_list = []
    array_list.append(tmp_list)



for i,order in enumerate(orders):
    array = deque(array_list[i])
    direction = 0
    if order.count("D")>len_list[i]:
        print("error")
        continue

    for func in order:
        if func == "R":
            direction += 1
        else:
            if direction%2 == 0:
                array.popleft()
            else:
                array.pop()

    if direction%2 == 1:
        tmp_array = []
        while array:
            tmp_array.append(array.pop())
        array = tmp_array
    print("["+",".join(array)+"]")

