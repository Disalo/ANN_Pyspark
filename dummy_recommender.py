'''
rocmmender
'''
import pandas as pd

movies = pd.read_csv('data/movies.csv')

'''
rocmmender
'''
def recommend_random(samples):
    '''
    samples of movies
    '''
    user_movies = movies.sample(samples)
    return user_movies
