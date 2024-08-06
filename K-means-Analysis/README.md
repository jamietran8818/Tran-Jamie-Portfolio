# Rstudio K-means Analysis:
This program utilizes Rstudio to perform K-means analysis to evaluate models and metrics. 

## Installation:
-Using Rstuio import the following libraries:

    library(forecast)
    library(useful)

## Loading Data:
-Import the binary classifer, clustering, and trinary classifier csv files provided using read.csv. 

-To confirm they have loaded successfully use the head function to preview each dataset.

## Code:
-Begin by plotting the binary and trinary data using a scatter plot.

-Evaluate nearest points by calaculation Euclidean.

### Example:

    binary <- c(70.88469, 83.17702)
    trinary <- c(30.08387, 39.63094)
    euclidean <- function(a,b) sqrt(sum(a-b)^2)
    euclidean(binary, trinary)

-Fit a k nearest neighbors’ model for each dataset for k=3, k=5, k=10, k=15, k=20, and k=25. Compute the accuracy of the resulting models for each value of k. 

### Example:

    diff(binary_data$x, differences = 3)
    diff(binary_data$x, differences = 5)
    diff(binary_data$x, differences = 10)
    diff(binary_data$x, differences = 15)
    diff(binary_data$x, differences = 20)
    diff(binary_data$x, differences = 25)
    diff(binary_data$x, lag = 3)
    diff(binary_data$x, lag = 5)
    diff(binary_data$x, lag = 10)
    diff(binary_data$x, lag = 15)
    diff(binary_data$x, lag = 20)
    diff(binary_data$x, lag = 25)

-Plot the results in a graph where the x-axis is the different values of k and the y-axis is the accuracy of the model.

-Evaluate graph.

-Moving on to the clustering data set plot the data using a scatter plot. 

-Fit data using k-means algorithm from k=2 to k=12. 

    clusterK2 <- kmeans(x=clustering_data, centers = 10)

-Plot graph once more and evaluate output.

