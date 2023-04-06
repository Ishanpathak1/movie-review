FORK the repo, 
then clone it with using the code git clone
and then download the nltk and requests using pip or pip3 install
Download all the libraries listed in the code

## How to run the app in your desktop (For Mac)
```bash
git clone https://github.com/Ishanpathak1/movie-review.git
```
```bash
cd movie-review
```

```bash 
pip install flask
```

```bash
pip install nltk
```

#### if pip is not working use pip3 instead of pip

### make file name test.py and paste the below code and then after saving run it

```python
import nltk
nltk.download('vader_lexicon')
```

#### if getting error, run the below code in terminal

```bash
pip install --upgrade certifi
```

#### replace the code in test.py with and then run this after saving it

```python
import ssl
import nltk

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('vader_lexicon')
```
### now after saving all the files in your terminal

```bash
export FLASK_APP=app.py
```

```bash
flask run
```

Things remaining
- Making an attractive and usable AI
- Getting sentiment analysis in one line
- Getting total number of positive and negative reviews


Tasks Completed
- API access
- Getting data from API
- Posting URL and getting the results
- Getting Piechart created
- Merging all the reviews in one

As of Date 6th April 2023-Ishan, Vedant ,Dhara
