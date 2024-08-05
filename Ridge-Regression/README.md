# Ridge Regression:
This program utilizes ridge regression model to predict stock prices. 

## Installation:
-Using Python in Jupyter Notebook import the following libraries:

    import pandas as pd
    import numpy as np 
    import warnings 
    import matplotlib.pyplot as plt 
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.linear_model import Ridge
    from sklearn.metrics import mean_squared_error, r2_score

## Loading Data:
-Import the Google, Apple, and Tesla datasets provided using pandas. 

-To confirm they have loaded successfully use the head function to preview each dataset.

-Using isna().sum() check for missing values in the following datasets.


## Code:
-To begin the analysis load independent and dependent variables into x and y dataframes.

-Utilize tran_test_split to split x and y into training and test sets.

-Fit and Scale the data using Standard Scaler and apply ridge regression.

### Example:

    #fitting and scaling data
    scaler = StandardScaler()
    x_train_scaled = scaler.fit_transform(x_train)
    x_test_scaled = scaler.transform(x_test)
    #creating ridge model
    ridge_reg = Ridge(alpha=1.0)
    ridge_reg.fit(x_train_scaled, y_train)

-Create predictions for the y datasets and find your Mean Squared Error and R squared scores. 

-Plot linear regression graph using matplotlib

### Example:

    #plotting linear regression graph 
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, y_pred_test, color='blue', label='Predicted vs Actual Values')
    plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', label='Ideal fit')
    plt.xlabel('Actual Values')
    plt.ylabel('Predicted Values')
    plt.title('Google Stock Predicted vs Actual Closing Prices')
    plt.legend()
    plt.show()

-Repeat using the Apple and Tesla datasets. 
