from random import randint
test = []
n = int(input("데이터 갯수를 입력하세요 : "))
for i in range(n):
    tmp_data = input().split(" ")
    test.append((tmp_data[0],int(tmp_data[1])))
print("before : ",test)

result = sorted(test,key=lambda student:student[1])

print(result)