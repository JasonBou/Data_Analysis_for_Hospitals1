user_input = input().split()
list_together = []

for i in user_input:
    if i[-1] == 's':
        list_together.append(i)

#new_list = "_".split(list_together)
print("_".join(list_together))
