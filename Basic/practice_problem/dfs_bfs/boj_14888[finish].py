from ast import operator


n = int(input())
number_list = list(map(int,input().split(" ")))
operater_list = list(map(int,input().split(" ")))

operators =  {}
for i,op in enumerate(operater_list):
    operators[i] = op

min_num = 1000000001
max_num = -1000000001

def do_operation(n1,n2,op):
    if op == 0:
        return n1+n2
    elif op == 1:
        return n1-n2
    elif op == 2:
        return n1*n2
    elif op == 3:
        if n1*n2 <0:
            result = abs(n1)//abs(n2)
            return -result
        else:
            result = n1//n2
            return result

test_op = {0:"+",1:"-",2:"*",3:"/"}

def dfs(idx,result):
    global min_num, max_num, operators, number_list
    if idx == n-1:
        if min_num>result:
            min_num = result
        if max_num<result:
            max_num = result
        return
    else:
        for i in range(4):
            if operators[i] != 0:
                next_result = do_operation(result,number_list[idx+1],i)
                operators[i] -= 1
                dfs(idx+1,next_result)
                operators[i] += 1

dfs(0,number_list[0])


print(max_num,min_num)