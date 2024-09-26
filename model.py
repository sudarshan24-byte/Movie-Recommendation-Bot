import difflib
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


def recommend_movies(movie_name):
    moviedf = pd.read_csv('movies.csv')
    combined_features = moviedf['movie_title']+ ' ' + moviedf['genres']+ ' ' + moviedf['country']+ ' ' +moviedf['language']+ ' ' +moviedf['actor_1_name']

    vectorizer = TfidfVectorizer()
    feature_vectors = vectorizer.fit_transform(combined_features)

    similarity = cosine_similarity(feature_vectors)
    # print(moviedf.head(1))
    # print('Namaste')


    # movie_name = input(' Enter your favourite movie name : ')

    list_of_all_titles = moviedf['movie_title'].tolist()

    find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)

    close_match = find_close_match[0]

    index_of_the_movie = moviedf[moviedf.movie_title == close_match].index[0]

    similarity_score = list(enumerate(similarity[index_of_the_movie]))

    sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True)

    # print('Movies suggested for you : \n')

    i = 1
    movies = []

    for movie in sorted_similar_movies:
        if i == 21:
            break
        index = movie[0]
        title_from_index = moviedf[moviedf.index==index]['movie_title'].values[0]
        if (i<21):
            # print(i, '.',title_from_index)
            movies.append(title_from_index)
            i+=1
    return movies

# m = recommend_movies('Transformers')
# for i in m:
#     print(i)