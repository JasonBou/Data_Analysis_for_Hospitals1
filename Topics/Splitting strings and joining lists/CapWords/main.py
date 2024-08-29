user_word = input().split("_")
empty_list = ''

for i in user_word:
    empty_list += i.capitalize()

print(empty_list)
#"".join(empty_list)
#print(empty_list)