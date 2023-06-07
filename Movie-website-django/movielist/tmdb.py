import requests

# discover

def get_movie_details(page=1):
    api_key = '678701dc7dc66aa11759f9b9a836fcb9'
    endpoint = f'https://api.themoviedb.org/3/discover/movie?api_key={api_key}&sort_by=popularity.desc&with_genres=28&page={page}'

    response = requests.get(endpoint)

    if response.status_code == 200:
        data = response.json()
        movies = data['results']
        movie_details = []
        for movie in movies:
            movie_detail = {
                'title': movie['title'],
                'poster': f"https://image.tmdb.org/t/p/w500{movie['poster_path']}"
            }
            movie_details.append(movie_detail)
        return movie_details

    return []
