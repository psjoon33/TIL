import sys
sys.stdin = open('1.txt', 'r')

for tc in range(1, int(input())+1):
	N, M = map(int, input().split())
	arr = [list(map(int, input().split())) for _ in range(N)]

	highests = []
	h = 0
	for i in range(N):
		for j in range(N):
			s = arr[i][j]
			if h < s:
				h = s
				highests = [[i, j]]
			elif h == s:
				highests.append([i, j])
	print(highests)



	