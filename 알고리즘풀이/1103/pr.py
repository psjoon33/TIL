A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

B = [1]


cnt = 0
for goal in B:
    if goal not in A:
        continue
    
    a = A[:]

    if a[(len(a)-1)//2] == goal:
        result = 1
        break

    elif a[(len(a)-1)//2] > goal:
        while True:
            # 왼쪽으로 자르기
            a = a[:(len(a)-1)//2]
            # a = [1 2 3 4 5 6 7]
            if goal == a[(len(a)-1)//2]:
                result = 1
                break
            elif goal > a[(len(a)-1)//2]:
                # 오른쪽으로 자르기
                a = a[(len(a)-1)//2+1:]
                if a[(len(a)-1)//2] == goal:
                    result = 1
                    break
                elif a[(len(a)-1)//2] > goal:
                    continue
                else:
                    result = 0
                    break
            else:
                result = 0
                break
    else:
        while True:
            # 오른쪽으로 자르기
            a = a[(len(a)-1)//2 +1:]
            # [9 10 11 12 13 14 15]
            if goal == a[(len(a)-1)//2]:
                result = 1
                break
            elif goal < a[(len(a)-1)//2]:
                # 왼쪽으로 자르기
                a = a[:(len(a)-1)//2]
                if a[(len(a)-1)//2] == goal:
                    result = 1
                    break
                elif a[(len(a)-1)//2] < goal:
                    continue
                else:
                    result = 0
                    break
    print(result)
    cnt = cnt + result
print(cnt)
    
