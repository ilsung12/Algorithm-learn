a, b = map(int, input().strip().split(' '))


# for j in range(b):
#     print()
#     for i in range(a):
#         print('*', end='')    

stars = '*' * a 
for i in range(b):
    print(stars)
print()