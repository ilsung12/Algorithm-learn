n = int(input())
l = list(map(int, input().split()))
s = list()

for i in range(len(l)):
    s.append(l[i])
    s.sort()
print(s[0])