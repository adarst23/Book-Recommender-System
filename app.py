import streamlit as st
import pickle
import numpy as np
import pandas as pd
import requests

def recommend(name):
    
    index = df[df['Book-Title'] == name].index[0]
    similar_items = sorted(list(enumerate(similarity[index])), key=lambda x: x[1], reverse=True)[1:7]
    recommended_books = []
    book_poster = []

    for i in similar_items:
        recommended_books.append(df.loc[i[0]]['Book-Title'])
        poster_result = books[books['Book-Title'] == df.loc[i[0]]['Book-Title']]['Image-URL-L']
        book_poster.append(poster_result.iloc[0])

    return recommended_books, book_poster


df_dict = pickle.load(open('book_recommendation.pkl','rb'))
books_dict = pickle.load(open('books.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
book_index = pickle.load(open('book_index.pkl','rb'))

books = pd.DataFrame(books_dict)
df = pd.read_pickle('df_pickle.pkl')
df = df.reset_index()


st.title('Book Recommender System')

selected_books = st.selectbox(
    'Search the Book', df['Book-Title'])


if st.button('Recommend'):
    names, posters = recommend(selected_books)

    col1, col2, col3 = st.columns(3)
   
    with col1:
        st.image(posters[0])
        st.text(names[0])
    with col2:
        st.image(posters[1])
        st.text(names[1])
    with col3:
        st.image(posters[2])
        st.text(names[2])

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(posters[3])
        st.text(names[3])
    with col2:
        st.image(posters[4])
        st.text(names[4])
    with col3:
        st.image(posters[5])
        st.text(names[5])

# footer_html = """
# <div style="position: fixed; bottom: 0; left: 0; right: 0; background-color: grey; padding: 10px; text-align: center;">
#     <p>Adarsh Tiwari - © 2023</p>
# </div>
# """
# st.markdown(footer_html, unsafe_allow_html=True)