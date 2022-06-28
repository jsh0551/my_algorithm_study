from random import randint
list_A = []
list_B = []
n = int(input("데이터 갯수를 입력하세요 : "))
k = int(input("바꿔치기 횟수를 입력하세요 : "))
for i in range(n):
    list_A.append(randint(1,100))
    list_B.append(randint(1,100))
print("before : ")
print(" - A : ",list_A)
print(" - B : ",list_B)

def quick_sort(array):
    if len(array)<=1:
        return array
    pivot = array[0]
    tail = array[1:]
    left = [x for x in tail if x<=pivot]
    right = [x for x in tail if x>pivot]
    
    return quick_sort(left) + [pivot] +quick_sort(right)

list_A = quick_sort(list_A)
list_B = quick_sort(list_B)

print("after : ")
print(" - A : ",list_A)
print(" - B : ",list_B)
for i in range(k):
    list_A[i] = list_B[n-1-i]
print(" - switched A : ",list_A)
print(" - sum : ",sum(list_A))