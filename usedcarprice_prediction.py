# -*- coding: utf-8 -*-
"""UsedCarPrice Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1T4IXjOuDx9YaMsd-cy-JBAlfnAXTDEj8

#Sprint 1
"""

#import necessory libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#import dataset
data=pd.read_csv('car data.csv')
data

#shape of the data
data.shape

"""301 rows and 9 coloumns"""

#Check the information of dataset
data.info()

#describe the dataset
data.describe()

"""#Data Preprocessing"""

#Checking Missing Values
data.isnull().sum()

#Correlation Matrix
corr=data.corr().style.background_gradient(cmap='gray')
corr

"""### **Visualization**"""

#Let's visualize the correlation matrix iin the seaborn
sns.set(rc={'figure.figsize':(15,10)})
sns.heatmap(data.corr(),annot=True,cmap='rainbow')

data.columns

#To visualize the year in the dataset
year=data['Year'].value_counts()
#to visualize the year in the seaborn barplot
ax=plt.axes()
#set the background color
ax.set(facecolor='yellow')
#set the figures size
sns.set(rc={'figure.figsize':(16,8)},style='darkgrid')
#set the title of the plot
ax.set_title("To visualize the which year most car sold",fontsize=32,fontweight=900)
#let's visualize the barplot
sns.barplot(x=year.index,y=year,palette='rainbow')
#on the x axis
plt.xlabel("Year")
#on the y_axis
plt.ylabel("Count")
#let's visualize the image
plt.show()

#Let's visualize the car names in the dataset
fuel_type=data['Fuel_Type'].value_counts()
#To visualize the top 20 car's sold
label=['Petrol','Diesel','CNG']
plt.figure(figsize=(16,9))
plt.pie(fuel_type,labels=label, autopct='%1.2f%%',explode=[0.03,0.05,0.07],colors=['green','yellow','orange'])
plt.title("To visualize the fuel_type in the dataset",fontsize=32,fontweight='bold')
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

# Set the background color
ax = plt.axes()
ax.set(facecolor='red')

# Set the figure size
sns.set(rc={'figure.figsize': (8, 6)}, style='darkgrid')

# Set the title of the plot
ax.set_title("To visualize the Selling_type", fontsize=32, fontweight=900)

# Visualize the countplot
sns.countplot(data=data, x='Selling_type', palette='rainbow')

# Label the x-axis
plt.xlabel("Selling_type")

# Label the y-axis
plt.ylabel("Count")

# Visualize the plot
plt.show()

#Let's check the car model with selling price
car_selling_price=data[['Car_Name','Selling_Price']].groupby(['Car_Name','Selling_Price']).sum().reset_index().sort_values(by='Selling_Price',ascending=False)
import plotly.express as px
fig=px.histogram(car_selling_price,x='Car_Name',y='Selling_Price',title="To visualize the car model with selling price")
fig.update_layout(bargap=0.2,bargroupgap=0.1,
    plot_bgcolor='black')

fig.show()

"""## Data Cleaning"""

final_data=data.drop(['Car_Name'],axis=1)
final_data.info()

# checking the distribution of categorical data
print(data.Fuel_Type.value_counts())
print(data.Selling_type.value_counts())
print(data.Transmission.value_counts())

from sklearn.preprocessing import LabelEncoder

# Initialize the LabelEncoder
label_encoder = LabelEncoder()

# Fit and transform the "Fuel_Type" column
final_data['Fuel_Type'] = label_encoder.fit_transform(final_data['Fuel_Type'])

# Now, the "Fuel_Type" column is label encoded

final_data.head()

from sklearn.preprocessing import LabelEncoder

# Initialize the LabelEncoder
label_encoder = LabelEncoder()

# Fit and transform the "Fuel_Type" column
final_data['Selling_type'] = label_encoder.fit_transform(final_data['Selling_type'])

# Now, the "Fuel_Type" column is label encoded

final_data.head()

from sklearn.preprocessing import LabelEncoder

# Initialize the LabelEncoder
label_encoder = LabelEncoder()

# Fit and transform the "Fuel_Type" column
final_data['Transmission'] = label_encoder.fit_transform(final_data['Transmission'])

# Now, the "Fuel_Type" column is label encoded

#final data after label encoding
final_data.head()

"""#Sprint 2

###Split the data set for train and test
"""

#import train_test_split
from sklearn.model_selection import train_test_split

features = final_data.drop(columns=['Selling_Price'])
target = final_data['Selling_Price']

#normalize the data
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
#Let's normalize the train dataset
X=scaler.fit_transform(features)

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.3, random_state=42)

features

target

"""###Import Random forest Regression"""

#Install the RandomForestRegressor model to the sklearn
from sklearn.ensemble import RandomForestRegressor
#install the RandomForestRegressor
random=RandomForestRegressor()
#Let's fit the train data to the model
random.fit(X_train,y_train)
#Prediction to the test dataset
random_pred=random.predict(X_test)

#Check the test score and train score to the RandomForestRegressor algorithm
print(f'The Test_accuracy: {random.score(X_test,y_test)*100:.2f}')
#Train score for the data
print(f'The Train_accuracy: {random.score(X_train,y_train)*100:.2f}')

#RandomForestRegressor algorithms mean_squared_error and r2_score
from sklearn.metrics import mean_squared_error,r2_score,mean_absolute_error
mse=mean_squared_error(y_test,random_pred)
rmse=np.sqrt(mse)
print("Root_mean_squred_error RandomForestRegressor {:.4f}".format(rmse))
print("R2_score RandomForestRegressor {:4f}".format(r2_score(y_test,random_pred)))
print("mean_absolute_error RandomForestRegressor {:4f}".format(mean_absolute_error(y_test,random_pred)))

user_input_features = []

# Ask the user to input the features one by one
print("Enter the following details for prediction:")
for feature_name in features.columns:
    value = input(f"Enter {feature_name}: ")
    user_input_features.append(float(value))

# Convert the user input to a numpy array
user_input = np.array(user_input_features).reshape(1, -1)

# Use the trained model to predict based on user input
predicted_price = random.predict(user_input)
print(f"The predicted price based on the input is: {predicted_price[0]:.2f}")

pip install joblib

from joblib import dump

# Save the trained model to a file
dump(random, 'random_forest_model.pkl')

import sklearn
print(sklearn.__version__)