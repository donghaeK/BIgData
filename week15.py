import seaborn as sns
import pandas as pd

titanic = sns.load_dataset('titanic')
#print(titanic.describe())

# survived_people = titanic[titanic['survived'] == 1]['survived'].count()
# dead_people = titanic[titanic['survived'] == 0]['survived'].count()
# print(f"생존자수는 {survived_people}명이고 죽은사람수는 {dead_people}입니다.")

# male_survived = titanic[(titanic['survived'] == 1) & (titanic['sex'] == 'male')]['survived'].count()
# female_survived = titanic[(titanic['survived'] == 1) & (titanic['sex'] == 'female')]['survived'].count()
# male_count = titanic[titanic['sex'] == 'male']['sex'].count()
# female_count = titanic[titanic['sex'] == 'female']['sex'].count()
# print(male_survived, male_count, female_survived, female_count)
# print(male_survived/male_count , female_survived/female_count)

#print(titanic.head(10))
first_survived = titanic[(titanic['survived'] == 1) & (titanic['pclass'] == 1)]['survived'].count()
second_survived = titanic[(titanic['survived'] == 1) & (titanic['pclass'] == 2)]['survived'].count()
third_survived = titanic[(titanic['survived'] == 1) & (titanic['pclass'] == 3)]['survived'].count()
print(first_survived, second_survived, third_survived)

pclass_survived = titanic.groupby('pclass')['survived'].sum()
print(pclass_survived)

