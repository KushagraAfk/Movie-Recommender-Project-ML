import streamlit as st
import pickle
import pandas as pd
import requests

movies_list = pickle.load(open('movies.pkl', 'rb'))
movies_list = pd.DataFrame(movies_list)
similarity = pickle.load(open('similarity.pkl', 'rb'))
st.title('Movie Recommender System')

selected_movie_name = st.selectbox("What movie did you just watch?", movies_list['title'].values)


def fetch_poster(movie_id):
    requests.get()
    


def recommend(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    movie_list = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])[1:6]
    movie_names = []

    for a in movie_list:
        movie_id = a[0]
        movie_names.append(movies_list.iloc[a[0]].title)
    return movie_names


if st.button("Recommend"):
    b = recommend(selected_movie_name)
    for i in b:
        st.write(i)
