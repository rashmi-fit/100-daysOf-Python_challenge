'''used this data set to analyse https://www.kaggle.com/c/titanic'''
import pandas as pd
titanic_data = pd.read_csv("../input/titanic/train.csv")

# Show the first five rows of the data
titanic_data.head()
titanic_data.tail()
