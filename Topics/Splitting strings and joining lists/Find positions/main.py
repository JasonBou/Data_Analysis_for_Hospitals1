# put your python code here
x = input()
y = input()
index_list = list()
x =x.split(" ")

for i, num in enumerate(x):
    if num == y:
        index_list.append(str(i))

if not index_list:
    print('not found')
else:
    print(' '.join(index_list))
#    print(index_list)


