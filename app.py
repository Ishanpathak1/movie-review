import requests
from flask import Flask, render_template, request
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/sentiment_analysis', methods=['POST'])
def sentiment_analysis():
    # Get the movie name from the form
    movie_name = request.form['movie_name']

    # Make a request to the TMDb API to search for the movie by name
    api_key = "e0a0015ede8a824fab642d5d1660255e"
    search_url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={movie_name}"
    search_response = requests.get(search_url)
    search_results = search_response.json()

    # Get the ID of the first result from the search
    movie_id = search_results["results"][0]["id"]

    # Make a request to the TMDb API to get movie details and reviews
    movie_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&append_to_response=reviews"
    movie_response = requests.get(movie_url)
    movie_data = movie_response.json()

    # Get the reviews and perform sentiment analysis on each review
    sid = SentimentIntensityAnalyzer()
    positive_reviews = []
    negative_reviews = []
    for review in movie_data["reviews"]["results"]:
        review_text = review["content"]
        scores = sid.polarity_scores(review_text)

        # Check if the review is positive or negative
        if scores["compound"] >= 0.05:
            positive_reviews.append(review_text)
        elif scores["compound"] <= -0.05:
            negative_reviews.append(review_text)

    # Summarize the positive and negative reviews
    positive_summary = " ".join(positive_reviews)
    negative_summary = " ".join(negative_reviews)

    # Plot the pie chart
    labels = ['Positive', 'Negative']
    sizes = [len(positive_reviews), len(negative_reviews)]
    colors = ['#33cc33', '#ff3333']

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title(f"Sentiment Analysis of Reviews for {movie_name}")
    plt.savefig('templates/images/sentiment.png')

    return render_template('results.html', positive_summary=positive_summary, negative_summary=negative_summary, movie_name=movie_name)

if __name__ == '__main__':
    app.run(debug=True)



