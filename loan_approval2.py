# -*- coding: utf-8 -*-
"""Copy of loan .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1C890Ul4ijFIpoKV6tkgoDmYQmXh2uwCG
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns
!pip install opendatasets
import opendatasets as od
import os
import plotly.express as px
import kagglehub

od.download('https://www.kaggle.com/datasets/abhishekmishra08/loan-approval-datasets?select=loan_data.csv')

url = pd.read_csv('/content/loan-approval-datasets/loan_data.csv')

url.info()

url

url.columns

url.head()

loan = url[['Income', 'Credit_Score', 'Loan_Amount','Employment_Status', 'Approval']].copy()
# we only take this Columns To predict Data
print(loan)

loan = loan.dropna(subset =['Income', 'Credit_Score', 'Loan_Amount','Employment_Status','Approval'])

print(loan)

loan.info()

loan.duplicated().sum()

loan.describe()

url.describe()

url['Employment_Status']=url['Employment_Status'].replace({'unemployed': 0, 'employed': 1}).astype(int)
url['Approval'] = url['Approval'].replace({'Rejected' :0, 'Approved':1}).astype(int)

url["Employment_Status"].value_counts()

url['Approval'].value_counts()

print(url)

plt.figure(figsize=(15,5))
plt.subplot(1,2,1)
sns.countplot(x='Employment_Status',data=url)
plt.title('Distribution of employment status')
plt.subplot(1,2,2)
sns.countplot(x='Approval',data=url)
plt.title('Distribution of loan approval')
plt.show()
plt.tight_layout()

px.scatter(url,x='Income',y='Credit_Score',color='Approval')

url.Approval.corr(url.Income)

url.Credit_Score.corr(url.Income)

url.Credit_Score.corr(url.Loan_Amount)

url.Income.corr(url.Approval)

url.Employment_Status.corr(url.Approval)

url.Credit_Score.corr(url.Approval)

#url.Income.corr(url.Approval)
url.Loan_Amount.corr(url.Approval)

url

sns.scatterplot(x='Income',y='Credit_Score',data=url,hue='Approval')

inputs = url [[ "Income"]]
targets = url['Approval']
print("input.shapes", inputs.shape)
print("targets.shapes", targets.shape)

inputs

sns.barplot(data= url, x='Income', y='Approval')

sns.barplot(data= url, x='Employment_Status', y='Approval')

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X = url[['Income', 'Credit_Score', 'Loan_Amount', 'Employment_Status']]
y = url['Approval']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy of the Decision Tree model: {accuracy}")

"""Here we can see that **decision tree runs good**"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

x = url[['Income', 'Credit_Score', 'Loan_Amount', 'Employment_Status']]
y = url['Approval']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy of the Random Forest model: {accuracy}")

"""Now we can see that** Random forest** runs **Good** more than **Decision tree**"""



