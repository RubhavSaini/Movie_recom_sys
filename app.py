from http.client import responses
import gdown
import streamlit as st
import pickle
import requests


# //////////////////////////////////////
file_id = '1-DPjOmKhGWrgV_apRcPvyZdMXN2IN1-D'
url = f'https://drive.google.com/uc?export=download&id={file_id}'

# Output file path
output = 'downloaded_model.pkl'  # You can change the name as needed

# Download the file
gdown.download(url, output, quiet=False)
with open('downloaded_model.pkl', 'rb') as file:
    similarity = pickle.load(file)

# /////////////////////////////////////////////
movies = pickle.load(open('movie.pkl','rb'))
# similarity = pickle.load(open('similarity.pkl','rb'))

def fetch_poster(movie_id):
    url="https://api.themoviedb.org/3/movie/{}?api_key=b7de2485ff29eb54db073335bdcbe1f1&language=en-US".format(movie_id)
    data=requests.get(url)
    data=data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w300/" + poster_path
    return full_path


# fetch_poster(272)
def recommend(movie):
    index=movies[movies['title']==movie].index[0]
    distances=sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])

    recom_movies_name=[]
    recom_movies_poster=[]
    for i in distances[1:6]:
        movie_id=movies.iloc[i[0]]['movie_id']
        # print(movies.iloc[i[0]]['ti'])

        recom_movies_name.append(movies.iloc[i[0]]['title'])
        recom_movies_poster.append(fetch_poster(movie_id))

        # st.write(movies.iloc[i[0]]['title'])
    return recom_movies_name,recom_movies_poster

movie_list=movies['title'].values
st.title("Movie Recommender System")
option = st.selectbox(
    "Search for movies",
    movie_list,
)

st.write("You selected:", option)

if st.button("Similar movies"):
    x,y=recommend(option)
    cols=st.columns(5)
    for i in range(5):
        with cols[i]:
            # try commenting the upper line
            st.write(x[i])
            st.image(y[i], caption=x[i])









