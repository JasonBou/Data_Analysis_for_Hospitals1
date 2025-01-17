

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#def gender_clean(row):
 #   if df_dropped ['gender'] == 'man'or df_dropped ['gender'] == 'male'):
 #       return 'm'
 #   if df_dropped ['gender'] == 'woman'or df_dropped ['gender'] =='female':
 #       df_dropped['gender']= 'f'

pd.set_option('display.max_columns', 8)
# reading data files
#'test/general.csv'
#'/Users/jb/Downloads/test/general.csv'

general_set = pd.read_csv('test/general.csv')
prenatal_set = pd.read_csv('test/prenatal.csv')
sports_set = pd.read_csv('test/sports.csv')

# renaming hospital and gender for prenatal and sports
prenatal_set.rename(columns={'HOSPITAL': 'hospital', 'Sex': 'gender'}, inplace=True)
sports_set.rename(columns={'Hospital': 'hospital', 'Male/female': 'gender'}, inplace=True)

# Concat the three data sets
combined_df = pd.concat([general_set, prenatal_set, sports_set],ignore_index=True)
# Drop Columns Unamed: 0
combined_df.drop(columns=['Unnamed: 0'], inplace=True)

# Delete all empty rows
df_dropped = combined_df.dropna(axis = 0, how = 'all')

# replace gender column with f and m respectively
df_dropped["gender"] = df_dropped["gender"].replace(["male", "man"], "m")
df_dropped["gender"] = df_dropped["gender"].replace(["woman", "female"], "f")

# replace na with f
df_dropped['gender'] = df_dropped['gender'].fillna('f')


#fill remaining Na s with O
df_dropped[['bmi', 'diagnosis','blood_test','ecg','ultrasound','mri','xray','children','months']] = df_dropped[['bmi', 'diagnosis','blood_test','ecg','ultrasound','mri','xray','children','months']].fillna(value=0)
#df_dropped.fillna(0, inplace=True)


#print shape and random rows for data frame
#print(f'Data shape: {df_dropped.shape}')
#print(df_dropped.sample(n=20, random_state=30))



# What hospital has the highest number of patients
no_pantients = df_dropped.hospital.value_counts().index[0]
# what share of patients in the general hospital suffers from stomach related lissues ?
share_stomach = (df_dropped[df_dropped['hospital'] =='general'].diagnosis.value_counts().loc['stomach'] /df_dropped[df_dropped['hospital'] =='general'].diagnosis.count()).round(3)
#What share of the patients in the sports hospital suffers from dislocation-related issues?
dislo_issues = (df_dropped[df_dropped['hospital'] =='sports'].diagnosis.value_counts().loc['dislocation'] /df_dropped[df_dropped['hospital'] =='sports'].diagnosis.count()).round(3)
# What is the difference in the median ages of the patients in the general and sports hospitals?
age_general = df_dropped[df_dropped['hospital'] =='general'].age.median()
age_sports = df_dropped[df_dropped['hospital'] =='sports'].age.median()
#print(age_general - age_sports)
#print(df_dropped.pivot_table(index =['blood_test','hospital'],aggfunc='count'))
hos_tests = df_dropped[df_dropped['blood_test']=='t'].hospital.value_counts().index[0]
no_test = df_dropped[df_dropped['blood_test']=='t'].hospital.value_counts().iloc[0]

#print statemnts
#print(f'The answer to the 1st question is {no_pantients}')
#print(f'The answer to the 2nd question is {share_stomach}')
#print(f'The answer to the 3rd question is {dislo_issues}')
#print(f'The answer to the 4th question is {age_general - age_sports}')
#print(f'The answer to the 5th question is {hos_tests}, {no_test} blood tests')

#question 1
#What is the most common age of a patient among all hospitals? Plot a histogram and choose one of the following age ranges: 0-15, 15-35, 35-55, 55-70, or 70-80.
bins = [0,15,35,55,70,80]
fig, axes = plt.subplots()
plt.hist(df_dropped['age'], bins=bins, color="orange", edgecolor='white')
count, edges, bars = plt.hist(df_dropped['age'], color="orange", edgecolor='white',bins=bins)
plt.bar_label(bars)
plt.xticks(bins)

# Question 2
#What is the most common diagnosis among patients in all hospitals? Create a pie chart.
fig, axes = plt.subplots()
plt.pie(df_dropped['diagnosis'].value_counts())
ax= df_dropped['diagnosis'].value_counts().plot(kind="pie",autopct='%1.1f%%', ylabel='', legend=True)
ax.legend(bbox_to_anchor=(1, 1.02), loc='upper left')
#plt.show()
#plt.show()

#Question 3
#Build a violin plot of height distribution by hospitals. Try to answer the questions. What is the main reason for the gap in values? Why there are two peaks, which correspond to the relatively small and big values? No special form is required to answer this question.
data_list =[df_dropped[df_dropped['hospital'] =='general'].height,df_dropped[df_dropped['hospital'] =='sports'].height,df_dropped[df_dropped['hospital'] =='prenatal'].height]
fig, axes = plt.subplots()
plt.violinplot(data_list)
axes.set_xticks((1, 2,3))
axes.set_xticklabels(("General","Sports",'prenatal'))
axes.set_yticks(np.arange(1, 8, step=.5))
axes.set_ylabel("height")
axes.set_title('Violin plot')

plt.show()

print('The answer to the 1st question: 15-35')
print('The answer to the 2nd question: pregnancy')
print("The answer to the 3rd question: It's because different levels of measurement")
