user_input = input().title().split()
new_list = []
#if user_input[0]:
#    user_input[0].lower().append()

#first_item = user_input[0]
for i in user_input:
    if user_input[0] == i:
        new_list = i.lower()
    else:
        new_list += i

"".join(new_list)

print(new_list)
