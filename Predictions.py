import pandas as pd
import joblib
import numpy as np
from joblib import load
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PowerTransformer
# Loading model
model = load('joblib_save/The_best_model_final.joblib')

# Reading CSV file
# data = pd.read_csv('samples/Pre/DIR-880_ARM_binary_combined.csv')
data = pd.read_csv('samples/DWR-932_combined.csv')

features = ['src', 'fname', 'funcaddr']
X = data.drop(columns=features) 

# Checks the data type and converts it to a numeric type
for column in X.columns:
    if X[column].dtype == 'object':
        X[column] = pd.to_numeric(X[column], errors='coerce')

# Process missing values and fill them with 0
X.fillna(0, inplace=True)

transformer = PowerTransformer(method='yeo-johnson')
X_scaled = transformer.fit_transform(X)

# predictions
predictions = model.predict(X_scaled)

# print result
print(predictions)

name_list = []

for i in predictions:
    name_list.append(i)
data["label"] = name_list
# data1.to_csv('Predictions_samples_1.csv',encoding = 'utf-8')
data.to_csv('samples/DWR-932_Pre_best_model.csv', index=False, encoding = 'utf-8')


