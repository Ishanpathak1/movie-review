from flask import Flask, request, render_template
import requests


app = Flask(__name__)
api_key = "e0a0015ede8a824fab642d5d1660255e"


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        movie_name = request.form['movie_name']

        # Make a request to the TMDb API to search for the movie by name
        search_url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={movie_name}"
        search_response = requests.get(search_url)
        search_results = search_response.json()

        # Get the ID of the first result from the search
        movie_id = search_results["results"][0]["id"]

        # Make a request to the TMDb API to get movie details and reviews
        movie_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&append_to_response=reviews"
        movie_response = requests.get(movie_url)
        movie_data = movie_response.json()

        # Extract the reviews from the movie data
        reviews = []
        for review in movie_data["reviews"]["results"]:
            review_text = review["content"]
            reviews.append(review_text)

        return render_template('reviews.html', movie_name=movie_name, reviews=reviews)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)


