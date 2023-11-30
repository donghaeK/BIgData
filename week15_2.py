import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

titanic = sns.load_dataset('titanic')
titanic = titanic.drop(['who','deck','embark_town','alive','class','adult_male','alone'],axis=1)
#print(titanic.info())
titanic = titanic.dropna() #결측치 행 제거
#수치데이터가 아닌 피처를 정수형 숫자로 변환
titanic['sex'] = titanic['sex'].map({'male':0,'female':1})
titanic['embarked'] = titanic['embarked'].map({'S':0, 'C':1,'Q':2})
#특성, 타겟분리
X = titanic.drop('survived', axis=1)
y = titanic['survived']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=1)
model = LogisticRegression(solver='liblinear')
model.fit(X_train,y_train)

y_pred = model.predict(X_test)
print(f"정확도 : {accuracy_score(y_test, y_pred)}")