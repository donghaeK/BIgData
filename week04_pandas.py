import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

# csv file download and prepare the data
# data_root = "https://github.com/ageron/data/raw/main/"
life_satisfaction = pd.read_csv("https://github.com/ageron/data/raw/main/" + "lifesat/lifesat.csv")
# print(life_satisfaction.head(5))
# print(life_satisfaction.shape)
# print(life_satisfaction.describe())

X = life_satisfaction[["GDP per capita (USD)"]].values #return 2darray
y = life_satisfaction[["Life satisfaction"]].values #return 2darray


# print(X)
# print(y)


# draw scatter diagram
life_satisfaction.plot(kind='scatter', grid=True, x="GDP per capita (USD)", y="Life satisfaction")
plt.axis([23_500, 62_500, 4, 9])
plt.show()
#
# model choice
model = LinearRegression()
#
# # Train the model
model.fit(X, y)

# predict new GDP per capita (South Korea 2020)
X_new = [[31700]]  # South Korea' GDP per capita in 2020
print(model.predict(X_new))
# outputs [[6.30165767]]
