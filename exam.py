# n = int(input())
# a=[]
# for i  in range(n):
#     r=int(input())
#     a.append(r)
# b=max(a)
# print(sum(a)/(b*3)*100)

# a = input()
# b=[]
# for i in a:
#     b.append(a.count(i))
# if b.count() == list(set(b)):
#     print(a.index(max(b)))
# else:
#     print('?')

# n,m = map(int, input().split())
# basket = [i for i in range(1,n+1)]
# temp = 0
# for x in range(m):
#   i,j = map(int, input().split())
#   temp = basket[i-1:j]
#   temp.reverse()
#   basket[i-1:j] = temp
#
# for x in range(n):
#   print(basket[x],end=" ")

# a,b = input().split()
# a=int(a[::-1])
# b=int(b[::-1])
# if a>b:
#     print(a)
# else:
#     print(b)

# a = input()
# b=0
# dic = {'ABC':2,'DEF':3,'GHI':4,'JKL':5,'MNO':6,'PQRS':7,'TUV':8,'WXYZ':9}
# di = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
# for i in range(len(a)):
#     for j in di:
#         if a[i] in j:
#             b+=di.index(j)+3
# print(b)

# a = int(input())
# for i in range(a):
#     b,c =input().split()
#     for j in c:
#         print(int(b)*j,end='')
#     print()

# while True:
#     try:
#         print(input())
#     except EOFError:
#         break

# print('         ,r\'"7')
# print("r`-_   ,'  ,/")
# print(" \\. \". L_r'")
# print('   `~\\/')
# print('      |')
# print('      |')

# c = [1, 1, 2, 2, 2, 8]
# a =list(map(int,input().split()))
# for i in range(6):
#     print(c[i]-a[i],end='')

# a=int(input())
# for i in range(1,a+1):
#     print('******''*'*i)

# a=list(str(input()))
# if list(reversed(a))==a:
#     print(1)
# else:
#     print(0)

# a = int(input())
# b =[]
# for i in range(a):
#     b.append(int(input()))
# for i in range(a):
#     c=b.pop()
#     print(c)

# n = int(input())
# for i in range(1, n):
#     print(' '*(n-i) + '*'*(2*i-1))
# for i in range(n, 0, -1):
#     print(' '*(n-i) + '*'*(2*i-1))

# dic =['c=','c-','dz=','d-','lj','nj','s=','z=']
# a = input()
# b=0
# for i in dic:
#     a=a.replace(i,'!')
# print(len(a))

# n = int(input())
# group_word = 0
# for _ in range(n):
#     word = input()
#     error = 0
#     for index in range(len(word)-1):
#         if word[index] != word[index+1]:
#             new_word = word[index+1:]
#             if new_word.count(word[index]) > 0:
#                 error += 1
#     if error == 0:
#         group_word += 1
# print(group_word)

#C:\Users\PC\work\python\AI_intel_S2\exam16_calculator.py
# array= [1,5,2,6,3,7,4]
# c=[[2, 5, 3], [4, 4, 1], [1, 7, 3]]
# def s(array,c):
#     answer=[]
#     for i in c:
#         answer = sorted(array[c[0] - 1:c[1]],reverse=True)
#         print(answer)
#     return answer
#
# s(array,c)

# rate = 0
# scoreSum = 0
# rating = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}
# for i in range(20):
#     subject, score, grade = input().split()
#     if grade == "P":
#         continue
#     rate += float(score) * rating[grade]
#     scoreSum += float(score)
# print(rate / scoreSum)

# A, B = [], []
#
# N, M = map(int, input().split())
#
# for row in range(N):
#     row = list(map(int, input().split()))
#     A.append(row)
#
# for row in range(N):
#     row = list(map(int, input().split()))
#     B.append(row)
#
# for row in range(N):
#     for col in range(M):
#         print(A[row][col] + B[row][col], end=' ')
#     print()

# x=0
# for _ in range(9):
#     for i in range(9):
#         a=int(input())
#         if a>x:
#             x=a
# print(x)

# table = [list(map(int,input().split())) for _ in range(9)]
# max = 0
# x , y = 0
# for i in range(9):
#     for j in range(9):
#         if max<=table[x][y]:
#             x=i+1
#             y=j+1
#             max=table[x][y]
#
# print(max)
# print(x, y)

# A = input()
# B = input()
# C = input()
# D = input()
# E = input()
# x = max(len(A),len(B),len(C),len(D),len(E))
# for i in range(x+1):
#     print(A[i]+B[i]+C[i]+D[i]+E[i])

# for _ in range(10):
#     print('*')
#
# for i in range(10):
#     print('*'*i)

# N = int(input())
# x = []
# for i in range(1, N+1, -1):
#     x.append(i)
# print(x)
# while len(x)==2:
#     x.pop()
#     a = x.pop()
#     x.insert(0, a)
# print(x)

# word = [input() for _ in range(5)]
# for i in range(15):
#     for j in range(5):
#         if i<len(word[j]):
#             print(word[j][i], end='')

