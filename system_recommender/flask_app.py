from datetime import datetime
from flask import Flask, request, render_template, Blueprint, flash, redirect, url_for
from flask_login import login_required, current_user
from flask_login import LoginManager
import requests
import pandas as pd
import pickle
from .forms import ProfileUpdateForm
from . import db




main = Blueprint('main', __name__)



# loading models

# movies = pd.read_csv('movies.csv')

movies = pickle.load(open('movies.pkl', 'rb'))

similarity = pickle.load(open('similarity.pkl', 'rb'))



# function to fetch movie poster

def fetch_poster(movie_id):

    url = "https://api.themoviedb.org/3/movie/{}?api_key=390e76286265f7638bb6b19d86474639&language=en-US".format(movie_id)

    data = requests.get(url)

    data = data.json()

    full_path = "https://image.tmdb.org/t/p/w500/" + data['poster_path']

    return full_path



# function to get recommended movies

def get_recommendations(movie):

    # get the index of the selected movie

    idx = movies[movies['title'] == movie].index[0]

    # get pairwise similarity scores of all movies with the selected movie

    sim_scores = list(enumerate(similarity[idx]))

    # sort the movies based on similarity scores in descending order

    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # get top 20 similar movies (excluding the selected movie)

    sim_scores = sim_scores[1:21]

    # get titles and posters of the recommended movies

    movie_indices = [i[0] for i in sim_scores]

    movie_titles = movies['title'].iloc[movie_indices].tolist()

    movie_posters = [fetch_poster(movies['movie_id'].iloc[i]) for i in movie_indices]

    return movie_titles, movie_posters


@main.route('/')
@login_required
def home():

    movie_list = movies['title'].tolist()

    return render_template('index.html', movie_list=movie_list)



# recommendation page

@main.route('/recommend', methods=['POST'])
@login_required
def recommend():

    movie_title = request.form['selected_movie']

    recommended_movie_titles, recommended_movie_posters = get_recommendations(movie_title)

    return render_template('index.html', movie_list=movies['title'].tolist(),

                           recommended_movie_titles=recommended_movie_titles,

                           recommended_movie_posters=recommended_movie_posters)

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

# @main.route('/update_profile')
# @login_required
# def update_profile():
#     return render_template('update_profile.html', name=current_user.name)

@main.route('/profile/update', methods=['GET', 'POST'])
@login_required
def update_profile():
    form = ProfileUpdateForm()

    # Load the current user's profile data into the form
    if request.method == 'GET':
        form.name.data = current_user.name
        form.username.data = current_user.username
        form.user_preferences.data = current_user.profile.user_preferences
        form.movies_watched.data = current_user.profile.movies_watched

    if form.validate_on_submit():
        # Update the profile with form data
        current_user.name = form.name.data
        current_user.username = form.username.data
        current_user.profile.user_preferences = form.user_preferences.data
        current_user.profile.movies_watched = form.movies_watched.data
        current_user.profile.updated_at = datetime.now()
        db.session.commit()
        flash('Your profile has been updated!', 'success')
        return redirect(url_for('main.update_profile'))

    return render_template('update_profile.html', form=form)
# if __name__ == '__main__':

#     app.run(debug=True)