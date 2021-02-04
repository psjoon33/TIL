arr = [1, 2, 3, 4]
N = len(arr)
sel = [0]*N
visited = [0]*N
sels = []

def perm(idx):
    if idx == N:
        print(sel)
        return
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = 1
                sel[i] = arr[idx]
                perm(idx+1)
                visited[i] = 0
perm(0)
