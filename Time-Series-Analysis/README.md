# SARIMAX model:
This program utilizes Seasonal AutoRegressive Integrated Moving Average with eXogenous regressors (SARIMAX) to forecast sales for the upcoming year for a local pizza parlor. 

## Installation:
-Using Python in Jupyter Notebook import the following libraries:

      import pandas as pd 
      import numpy as np
      import statsmodels.api as sm
      import warnings 
      import matplotlib.pyplot as plt
      import plotly.express as px
      from statsmodels.tsa.stattools import adfuller
      from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

## Loading Data:
-Import the pizza dataset provided using pandas. 

-To confirm they have loaded successfully use the head function to preview each dataset.

-Using isna().sum() check for missing values in the following datasets.


## Code:
-Format and resample date to datetime format.

### Example:

      #formatting datetime to a singular column
      pizza['datetime'] = pd.to_datetime(pizza['order_date'] + ' ' + pizza['order_time'], format='%d/%m/%Y %H:%M:%S')
      #setting datetime as index
      pizza.set_index('datetime', inplace=True)
      #removing all columns aside from total price column
      pizza = pizza[['total_price']]
      #resampling data to daily frequency
      pizza = pizza.resample('D').sum() 

-Evaluate whether the data is stationnary and plot acf/pacf to determine p and q values.

-Define SARIMAX model and print results summary.

### Example:

      #defining SARIMAX model
      sarimax = SARIMAX(pizza['total_price'], 
                order=(0, 1, 1),       # ARIMA order
                seasonal_order=(0, 1, 1, 12),  # Seasonal order (p,d,q,s) - weekly seasonality
                enforce_stationarity=False,
                enforce_invertibility=False)
      #fitting model
      results = sarimax.fit(disp=False)

-Establish forecasted values and plot the results using matplotlib.

### Example:

      #forecasting next year values
      forecast = results.get_forecast(steps=365)  
      #getting mean forecasted values
      forecast_mean = forecast.predicted_mean
      #getting forecast confidence intervals
      forecast_conf_int = forecast.conf_int()

### Conclusion:

At this time, I certainly do not believe this model is ready to be rolled out to the public. While we 
were able to deliver a forecasted range to the pizza parlor it is far less centralized than I would like when 
offering services to small business. The end goal is to be able to help small business cut on costs and not 
waste their time with under or over hiring. Our current results could help them in a general sense
however, I want to have the integrity to deliver stronger results than the one given. I had a lot of trouble 
utilizing this specific data set with the ARMIA, ARMIAX, and SARIMAX models. While I could try and 
troubleshoot even further or try out different models, ultimately this data set may have not been the 
compatible with the goals I was trying to achieve with this research.
