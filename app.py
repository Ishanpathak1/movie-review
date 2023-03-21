import requests
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Make a request to the NYTimes API to get movie reviews
api_key = "5q6Hxy62fAysqZQlMX8DazIoAqJG7lnR"
url = f"https://api.nytimes.com/svc/movies/v2/reviews/search.json?query=godfather&api-key={api_key}"
response = requests.get(url)
data = response.json()

# Get the reviews and perform sentiment analysis on each review
sid = SentimentIntensityAnalyzer()
for review in data["results"]:
    review_text = review["summary_short"]
    scores = sid.polarity_scores(review_text)
    
    # Print the sentiment scores for each review
    print(f"Review: {review_text}")
    print(f"Positive sentiment: {scores['pos']}")
    print(f"Negative sentiment: {scores['neg']}")
    print(f"Neutral sentiment: {scores['neu']}")
    print(f"Overall sentiment score: {scores['compound']}")
    print("--------------------------------------------------")
