# Simon Dutton
# Due April 11th, 2023 
# Week 5, Day 1 Flask Assignment
# Favorite 5
from flask import render_template
from app import app

# keep this global so it is accessible to all
top5_dict = {
    'artists' : ['Sammy Rae & The Friends', 'Ripe', 'Paramore', 'The Weeknd', 'Remi Wolf'], 
    'food' : ['Vietnamese Spring Rolls', 'Sushi', 'Thai Red Curry', 'Fruit Salad', 'Chana Masala'],
    'tv shows' : ['Ted Lasso', 'Schitt\'s Creek', 'Only Murders In The Building', 'White Lotus', 'Survivor'],
    'movies' : ['Brigsby Bear', 'Eighth Grade', 'Wakanda Forever', 'Rear Window', 'Yesterday'],
    'pokemon' : ['Squirtle', 'Charizard', 'Caterpie', 'Turtwig', 'Sudowoodo']
}

@app.route('/')
def home_page():
    categories = [item for item in top5_dict] 
    return render_template('index.html', len = len(categories), cat=categories)

@app.route('/artists', methods=["GET"])
def artists_page():
    return render_template('artists.html', len = len(top5_dict['artists']), artists=top5_dict['artists'])

@app.route('/food', methods=["GET"])
def food_page():
    return render_template('food.html', len = len(top5_dict['food']), food=top5_dict['food'])

@app.route('/tv shows', methods=["GET"])
def tv_shows_page():
    return render_template('tv shows.html', len = len(top5_dict['tv shows']), tv_shows=top5_dict['tv shows'])

@app.route('/movies', methods=["GET"])
def movies_page():
    return render_template('movies.html', len = len(top5_dict['movies']), movies=top5_dict['movies'])

@app.route('/pokemon', methods=["GET"])
def pokemon_page():
    return render_template('pokemon.html', len = len(top5_dict['pokemon']), pokemon=top5_dict['pokemon'])
