N,M = map(int, input().split())

num_list = [i+1 for i in range(N)]

check_list = [False]*N

arr = []

def dfs(k):
    if k == M:
        print(*arr)
        return

    for i in range(N):
        if check_list[i]:
            continue
        check_list[i] = True
        arr.append(num_list[i])
        dfs(k+1)
        arr.pop()
        check_list[i]=False

dfs(0)
