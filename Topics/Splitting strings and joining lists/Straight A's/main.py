list_grades = input().upper().split()
# put your python code here
count_grades = 0
count_a = 0
for i in list_grades:
    count_grades += 1
    if i == 'A':
        count_a += 1


perc_agrades = count_a / count_grades
print(round(perc_agrades,2))





