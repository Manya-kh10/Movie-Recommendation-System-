import streamlit as st
import pickle
import pandas as pd
import requests

# FETCH THE POSTER (FIXED)
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=0ed5fa760f860a109210ee039464f53c&language=en-US"
    response = requests.get(url)

    # Convert response to JSON safely
    data = response.json()

    # CHECK if poster_path exists
    if data.get('poster_path') is None:
        return "https://via.placeholder.com/500x750?text=No+Image"

    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500" + poster_path
    return full_path


# FUNCTION TO SHOW THE RECOMMENDATIONS
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommanded_movies = []
    recommanded_movies_poster = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommanded_movies.append(movies.iloc[i[0]].title)
        recommanded_movies_poster.append(fetch_poster(movie_id))

    return recommanded_movies, recommanded_movies_poster


similarity = pickle.load(open('similarity.pkl', 'rb'))
movies_list1 = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies_list1)

movies_list = movies['title'].values

st.title('MOVIE RECOMMENDER SYSTEM')

selected_movie = st.selectbox(
    "Type or select a movie of your choice from the dropdown menu",
    movies_list
)

st.write("You selected:", selected_movie)

if st.button('Recommend'):
    names, poster = recommend(selected_movie)

    col1, col2, col3, col4, col5 = st.beta_columns(5)

    with col1:
        st.text(names[0])
        st.image(poster[0])

    with col2:
        st.text(names[1])
        st.image(poster[1])

    with col3:
        st.text(names[2])
        st.image(poster[2])

    with col4:
        st.text(names[3])
        st.image(poster[3])

    with col5:
        st.text(names[4])
        st.image(poster[4])
