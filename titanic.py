# -*- coding: utf-8 -*-
"""titanic.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ePrOwyPIXU3ohxh_pTWkfXeIrR0O_cG4
"""

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic_data = pd.read_csv(url)

# Display basic information about the dataset
print(titanic_data.info())

# Display the first few rows of the dataset
print(titanic_data.head())

# Handle missing values
titanic_data.dropna(subset=['Embarked'], inplace=True)  # Drop rows with missing 'Embarked'
titanic_data['Age'].fillna(titanic_data['Age'].median(), inplace=True)  # Fill missing 'Age' values with median

# Remove irrelevant columns
irrelevant_columns = ['PassengerId', 'Name', 'Ticket', 'Cabin']
titanic_data.drop(columns=irrelevant_columns, inplace=True)

# Convert data types
titanic_data['Pclass'] = titanic_data['Pclass'].astype('category')
titanic_data['Sex'] = titanic_data['Sex'].astype('category')
titanic_data['Embarked'] = titanic_data['Embarked'].astype('category')

# Verify the changes
print(titanic_data.info())

# Summary statistics
print(titanic_data.describe())

# Visualize the distribution of age
plt.figure(figsize=(8, 6))
sns.histplot(data=titanic_data, x='Age', bins=20, kde=True)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Compare survival rates between genders
plt.figure(figsize=(6, 4))
sns.barplot(data=titanic_data, x='Sex', y='Survived', ci=None)
plt.title('Survival Rate by Gender')
plt.ylabel('Survival Rate')
plt.xlabel('Gender')
plt.show()

# Compare survival rates across passenger classes
plt.figure(figsize=(6, 4))
sns.barplot(data=titanic_data, x='Pclass', y='Survived', ci=None)
plt.title('Survival Rate by Passenger Class')
plt.ylabel('Survival Rate')
plt.xlabel('Passenger Class')
plt.show()

# Explore age distribution within passenger classes
plt.figure(figsize=(8, 6))
sns.boxplot(data=titanic_data, x='Pclass', y='Age')
plt.title('Age Distribution by Passenger Class')
plt.ylabel('Age')
plt.xlabel('Passenger Class')
plt.show()



