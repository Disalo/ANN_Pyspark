import pandas as pd

movies = pd.read_csv('data/movies.csv')

'''
rocmmender
'''
def recommend_random(samples):
    '''
    rocmmender
    '''
    user_movies = movies.sample(samples)
    return user_movies
