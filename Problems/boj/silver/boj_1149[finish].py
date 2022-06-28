import sys
sys.setrecursionlimit(10**6)

n = int(input())
house_list = [[0,0,0]]
for i in range(n):
    color_price = list(map(int,input().split(" ")))
    house_list.append(color_price)

dp = [[0,0,0]]
for i in range(n):
    dp.append([0,0,0])

def sum_prices(dp,n):
    if n==1:
        dp[n] = house_list[n][:]
        return dp[n]
    pre_prices = sum_prices(dp,n-1)
    dp[n][0] = house_list[n][0] + min(pre_prices[1],pre_prices[2])
    dp[n][1] = house_list[n][1] + min(pre_prices[0],pre_prices[2])
    dp[n][2] = house_list[n][2] + min(pre_prices[0],pre_prices[1])

    return dp[n]
    
results = sum_prices(dp,n)
print(min(results))