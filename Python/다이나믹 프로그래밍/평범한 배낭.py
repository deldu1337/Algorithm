#냅색 알고리즘
#① 현재 배낭의 허용 무게보다 넣을 물건의 무게가 더 크다면 넣지 않는다.
#② 그렇지 않다면, 다음 중 더 나은 가치를 선택하여 넣는다
#    2-1) 현재 넣을 물건의 무게만큼 배낭에서 뺀다. 그리고 현재 물건을 넣는다.
#    2-2) 현재 물건을 넣지않고 이전 배낭 그대로 가지고 간다.

#① j < weight : d[i][j] = d[i-1][j]
#② d[i][j] = max( d[i-1][ j-weight ]+value ), d[i-1][j] )

from sys import stdin
input = stdin.readline
N, K = map(int, input().split())
stuff = [[0,0]]
knapsack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
    stuff.append(list(map(int, input().split())))


#냅색 알고리즘
for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight = stuff[i][0] 
        value = stuff[i][1]
       
        if j < weight:
            knapsack[i][j] = knapsack[i - 1][j] #weight보다 작으면 위의 값을 그대로 가져온다
        else:
            knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])

print(knapsack[N][K])

