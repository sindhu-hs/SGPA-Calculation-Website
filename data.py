import pickle
import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("model.csv")
x = data.iloc[:,:-1]
y = data.iloc[:,-1]

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)

# Model initialization
regression_model = LinearRegression()
# Fit the data(train the model)
regression_model.fit(x_train, y_train)

with open("regression_model.pkl", "wb") as f:
    pickle.dump(regression_model, f)