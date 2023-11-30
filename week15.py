import seaborn as sns
import matplotlib.pyplot as plt
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

# first_survived = titanic[(titanic['survived'] == 1) & (titanic['pclass'] == 1)]['survived'].count()
# second_survived = titanic[(titanic['survived'] == 1) & (titanic['pclass'] == 2)]['survived'].count()
# third_survived = titanic[(titanic['survived'] == 1) & (titanic['pclass'] == 3)]['survived'].count()
# print(first_survived, second_survived, third_survived)
# pclass_survived = titanic.groupby('pclass')['survived'].sum()
# print(pclass_survived)

#teenager_survived = titanic.groupby(pd.cut(titanic['age'], bins=[0,10,20,30,40,50,60,70,80]))['survived'].sum()
#print(teenager_survived)


#사망자와 생존자 시각화
titanic.dropna()
survived_ages = titanic[titanic['survived'] == 1]['age'].dropna()
dead_ages = titanic[titanic['survived'] == 0]['age'].dropna()
print(survived_ages, dead_ages)

plt.hist(survived_ages, bins=20, label='survived',alpha=0.3)
plt.hist(dead_ages, bins=20, label='dead', alpha=0.5)
plt.xlabel('Age')
plt.ylabel('Count')
plt.legend()
plt.plot()
plt.show()

