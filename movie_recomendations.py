import requests
import json
from PIL import Image


def get_movies_from_tastedive(movie_name):

    url = 'https://tastedive.com/api/similar'
    param_dict = {"q": movie_name, "type": "movies", "limit": 9}
    response = requests.get(url, params=param_dict)

    return response.json()


def extract_movie_titles(json_file):
    suggestions =  [y['Name'] for y in json_file['Similar']['Results']]

    return suggestions


def get_related_titles(movie_lst):

    multiple_movies  = { y for movie in movie_lst for y in extract_movie_titles(get_movies_from_tastedive(movie)) }
    return multiple_movies


def get_movie_data(movie_title):
    url = 'http://www.omdbapi.com/?apikey=995e507c&'
    param_dict = {"t": movie_title, "r": "json"}
    response = requests.get(url, params=param_dict)

    return response.json()


def get_movie_rating(json_file):
    ratings = json_file['Ratings']
    for rating in ratings:
        if rating['Source'] == 'Rotten Tomatoes':
            user_rating = int(rating['Value'].rstrip("%"))
            return user_rating
        else:
            user_rating = 0

    return user_rating


def get_movie_poster(movie):
    movie_poster = get_movie_data(movie)
    response = requests.get(movie_poster['Poster'])
    img_path = f"img/{movie_poster['Title']}"
    with open(img_path, "wb") as file:
        file.write(response.content)

    return img_path


def get_sorted_recommendations(movie_lst):
    movie_recomendations = get_related_titles(movie_lst)

    movies_posters = [ get_movie_poster(movie) for movie in movie_recomendations]

    movie_and_ratings= {movie: get_movie_rating(get_movie_data(movie)) for movie in movie_recomendations}

    sorted_movies = [x for x in sorted(movie_and_ratings.keys(), key=lambda k: (movie_and_ratings[k], k), reverse=True)]

    return sorted_movies


def get_pic():
    posters = ["Gladiator", "Inception" , "Terminator 2 Judgment Day", "The Dark Knight Rises", "The Prestige", "V for Vendetta", "Inglourious Basterds", "The Dark Knight", "Shutter Island"]

    # img_path = "img/The Dark Knight Rises"

    all_pictures = [Image.open(r"img/{}".format(x)).convert('RGB') for x in posters]

    img_w, img_h = 300, 444

    canvas = Image.new('RGB', (img_w*3, img_h*3))

    x = 0
    y = 0

    for item in all_pictures:
        canvas.paste(item, (x,y))
        if x + item.width == canvas.width:
            x = 0
            y = int(y + item.height)
        else:
            x = int(x + item.width)

    canvas = canvas.resize((int(canvas.width/2), int(canvas.height/2)))

    canvas.save("img/movie_recomendations2.jpg")
    canvas.show()


user_input = "Batman Begins"

# print(get_sorted_recommendations([user_input]))

get_pic()


