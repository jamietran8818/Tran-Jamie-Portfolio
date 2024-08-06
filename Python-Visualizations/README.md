# Python Visualizations:
This program utilizes matplotlib and seaborn libraries to generate a histogram, box plot, bullet chart, and grouped bar chart. 

## Installation:
-Using Python in Jupyter Notebook import the following libraries:

    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    import plotly.graph_objects as go

## Loading Data:
-Import the birth rate, crime rates by state, and education csv files provided using pandas. 

-To confirm they have loaded successfully use the head function to preview each dataset.

## Code:
-Assign needed colums to variable to generate the following graphs 

### Example:

    #assigning column to variable 
    countries = birth['Country']
    y_2000 = birth['2000']
    y_2008 = birth['2008']

### Histogram Example:

    #plotting histogram
    plt.hist(dropouts, bins = 5, edgecolor = 'black')
    plt.xlabel('Dropout rates of students')
    plt.ylabel('Frequency')
    plt.title('Dropout Rates by State')
    plt.show()
      
### Boxplot Example:

    #plotting box plot 
    sns.boxplot(assault)
    plt.xlabel('Aggravated Assault')
    plt.ylabel('Values')
    plt.title('Aggravated Assault Across the United States')
    plt.show()

### Bullet Graph Example:

    #plotting bullet chart
    fig = go.Figure(go.Indicator(
        mode = "number+gauge+delta",
        value = avg,
        domain = {'x': [0.1, 1], 'y': [0, 1]},
        title = "Robberies",
        #adding indicator to show the difference from the max value 
        delta = {'reference': max},
        gauge = {
            'shape': "bullet",
            'axis': {'range': [0, max +50]},
            'threshold': {
                'line': {'color': "red", 'width': 2},
                'thickness': 0.75,
                'value': max},
           'steps': [
                {'range': [0, max / 2], 'color': "lightgray"},
                {'range': [max / 2, max], 'color': "gray"}]}))
    fig.update_layout(height = 250)
    fig.show()

### Grouped Bar Chart Example:

    #creating grouped bar chart
    x = np.arange(len(countries))
    bar_width = 0.35
    #creating figure and axes of chart
    fig, ax = plt.subplots()
    #plotting year values and position
    bar1 = ax.bar(x - bar_width/2, y_2000, bar_width, label='Year 2000')
    bar3 = ax.bar(x + bar_width/2, y_2008, bar_width, label='Year 2008')
    ax.set_xlabel('Countries')
    ax.set_ylabel('Birth Rates')
    ax.set_title('Birth Rates by Country')
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.legend()
    plt.show()
