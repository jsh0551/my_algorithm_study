from random import randint
test = []
n = int(input("데이터 갯수를 입력하세요 : "))
for i in range(n):
    test.append(randint(1,100000))
print("before : ",test)

for i in range(n):
    max_index = i
    for j in range(i+1,n):
        if test[max_index]<=test[j]:
            max_index = j
    test[max_index],test[i] = test[i],test[max_index]

print("after : ",test)