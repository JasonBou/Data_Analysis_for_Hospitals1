dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']

user_input = input().lower().split()
word_incorrect =[]

for i in user_input:
    if i not in dictionary:
        word_incorrect.append(i)


if not word_incorrect:
   print('OK')
else:
    for z in word_incorrect:
        print(z)
