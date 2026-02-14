<<<<<<< HEAD
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sia=SentimentIntensityAnalyzer()
#polarity scores in sia
#positive,negative,neutraland compound
reviews="this app is amazing"
sentiment_score=sia.polarity_scores(reviews)
print(sentiment_score)
reviews="the app is very bad"
sentiment_score=sia.polarity_scores(reviews)
print(sentiment_score)

=======
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sia=SentimentIntensityAnalyzer()
#polarity scores in sia
#positive,negative,neutraland compound
reviews="this app is amazing"
sentiment_score=sia.polarity_scores(reviews)
print(sentiment_score)
reviews="the app is very bad"
sentiment_score=sia.polarity_scores(reviews)
print(sentiment_score)

>>>>>>> db2cd396b59138cbc9a672533df52ddf30607c64
