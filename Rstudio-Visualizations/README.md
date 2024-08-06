# Rstudio Visualizations:
This program utilizes ggplot2 and treemap libraries to generate a tree map, area map, and a stacked area map.

## Installation:
-Using Rstuio import the following libraries:

    library(ggplot2)
    library(treemap)

## Loading Data:
-Import the unemployment rate 1948-2010 csv file provided using read.csv. 

-To confirm they have loaded successfully use the head function to preview each dataset.

## Code:

### Tree map Example:

    treemap(unemployed, index = 'Year', vSize = 'Value', title = 'Unemployment Percentage by Year')
      
### Area map Example:

    ggplot(data = unemployed, 
           aes(x = Year, 
               y = Value)) +
        geom_area(aes(colour = Value, fill = Value)) +
        labs(title = 'Unemployment Over the Years')

### Stacked area map Example:

     ggplot(data = unemployed, 
         aes(x = Year, 
             y = Value,
             fill = Period)) +
      geom_area(aes(colour = Period, fill = Period)) +
      labs(title = 'Unemployment Over the Years')
      
