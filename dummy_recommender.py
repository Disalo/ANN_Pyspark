import random
import pandas as pd

movies = pd.read_csv('data/movies.csv')

'''
rocmmender
'''

def recommend_random(samples):
    user_movies = movies.sample(samples)
    movie_ids = [random.randint(1,9741) for i in range(0,5) if random.randint(1,9741) not in user_movies]
    recs = [movies['title'][i] for i in movie_ids if i in movies['movieId']]
    return dict(zip(movie_ids,recs))
