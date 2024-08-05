# Logistic Regression:
This program utilizes a logistic regression model to evaluate the relationship between the diagnosis of heart disease and various paitents health characteristics. 

## Installation:
-Using Python in Jupyter Notebook import the following libraries:

      import pandas as pd
      import numpy as np
      import warnings 
      import matplotlib.pyplot as plt
      from sklearn.linear_model import LogisticRegression
      from sklearn.model_selection import train_test_split
      from sklearn.metrics import classification_report, confusion_matrix

## Loading Data:
-Import the heart disease prediction csv file provided using pandas. 

-To confirm they have loaded successfully use the head function to preview each dataset.

-Using isna().sum() check for missing values in the following datasets.

-Drop irrelevant columns and filter 'Heart Disease' column to only include those with heart disease present.

-Lastly convert qualitative data to integers.


## Code:
-To begin the analysis load independent and dependent variables into x and y dataframes.

-Utilize tran_test_split to split x and y into training and test sets.

-Fit and apply logistic regression.

### Example:

      #assigning the model to a variable 
      log_regression = LogisticRegression(max_iter = 1000)
      #fitting the training data to the model
      log_regression.fit(x_train, y_train)
      
-Create predictions for the x test set. 

-Print and evaluate classification report and confusion matrix. 
plt.show()

-Repeat using the Apple and Tesla datasets. 
