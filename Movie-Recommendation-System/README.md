# Movie Recommendation System:
This program evaluates movie reviews and makes specializted recommendations based on the user's previous reviews or similar movies. 

## Installation:
-Using Python in Jupyter Notebook import the following libraries:

    import pandas as pd
    import numpy as np
    import sklearn
    import matplotlib.pyplot as plt
    import seaborn as sns
    from scipy.sparse import csr_matrix
    from sklearn.neighbors import NearestNeighbors

## Loading Data:
-Import the ratings csv file provided using pandas. 

-To confirm they have loaded successfully use the head function to preview each dataset.

## Code:
-Begin with exploratory data analysis and find out the number of ratings, movies, and users their are. 

-Find the frequency of reviews each user submits. 

### Example:

    #finding how often each user leaves reviews
    user_freq = ratings[['userId', 'movieId']].groupby('userId').count().reset_index()
    user_freq.columns = ['userId', 'n_ratings']
    print(user_freq.head())

-Remove bias from movies with less reviews.

### Example:

    #removing bias from smaller movies
    movie_stats = ratings.groupby('movieId')[['rating']].agg(['count', 'mean'])
    movie_stats.columns = movie_stats.columns.droplevel()

-Create function that creates a matrix between users and various movies

### Example:

    def movie_matrix(data):
        #finding number of different users and movies
        uni_user = len(data['userId'].unique())
        uni_movie = len(data['movieId'].unique())
        #establishing dictionaries of unique users and movies
        user_mapper = dict(zip(np.unique(data['userId']), list(range(uni_user))))
        movie_mapper = dict(zip(np.unique(data['movieId']), list(range(uni_movie))))
        #mapping users and movies to matrix
        user_inv_mapper = dict(zip(list(range(uni_user)), np.unique(data['userId'])))
        movie_inv_mapper = dict(zip(list(range(uni_movie)), np.unique(data['movieId'])))
        #map corresponding indices
        user_index = [user_mapper[i] for i in data['userId']]
        movie_index = [movie_mapper[i] for i in data['movieId']]
        #making matrix with user and movies indices and ratings
        x = csr_matrix((data['rating'], (movie_index, user_index)), shape = (uni_movie,uni_user))

        return x, user_mapper, movie_mapper, user_inv_mapper, movie_inv_mapper

-Create function that reccomends similar movies.

### Example:

     def similar_movies(movie_id, x, k, metric = 'cosine', show_distance = False):
        #creating empty list where titles will be held 
        neighbor_ids = []
        #getting index of movie and corresponding user
        movie_ind = movie_mapper[movie_id]
        movie_vec = x[movie_ind]
        #using KNN to find most similar movies in range
        k+=1
        kNN = NearestNeighbors(n_neighbors = k, algorithm = 'brute', metric = metric)
        kNN.fit(x)
        movie_vec = movie_vec.reshape(1,-1)
        neighbor = kNN.kneighbors(movie_vec, return_distance = show_distance)
        #adding titles to empty list
        for i in range(0, k):
            n = neighbor.item(i)
            neighbor_ids.append(movie_inv_mapper[n])
        neighbor_ids.pop(0)
        return neighbor_ids
        
-Create final funtion that reccomend movie specific to user 

### Example:

    def recommend_movies_for_user(user_id, x, user_mapper, movie_mapper, movie_inv_mapper, k=10):
        #seeing if user has rating history
        user_retrevial = ratings[ratings['userId'] == user_id]
        #creating if statement for unknown values 
        if user_retrevial.empty:
            print('User ' + str(user_id) + ' does not exist.')
            return
        #filtering for movies with highest ratings 
        movie_id = user_retrevial[user_retrevial['rating'] == max(user_retrevial['rating'])]['movieId'].iloc[0]
        #finding titles in dictionary
        movie_titles = dict(zip(movies['movieId'], movies['title']))
        #finding similar movies to the highest rated
        similar_ids = similar_movies(movie_id, x, k)
        movie_title = movie_titles.get(movie_id, 'Movie not found')
        #if statement for movies not found
        if movie_title == 'Movie not found':
            print(str(movie_id) + ' is not found')
            return

        print('Since you watched ' + str(movie_title) + ', you might also like:')
        print('---------------------------------------------------------------')
        for i in similar_ids:
            print(movie_titles.get(i, 'Movies not found'))

-Test different values for the functions to get recommendations.

