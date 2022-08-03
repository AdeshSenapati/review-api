from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def sentiment_scores(sentence):
    sentiment = SentimentIntensityAnalyzer()
    sentiment_dict = sentiment.polarity_scores(sentence)
    # print(sentiment_dict)
    negative = f"Product Reviews were rated as {sentiment_dict['neg'] * 100}% Negative"
    neutral = f"Product Reviews were rated as {sentiment_dict['neu'] * 100}% Neutral"
    positive = f"Product Reviews were rated as {sentiment_dict['pos'] * 100}% Positive"

    results = {
        'negative': negative,
        'neutral': neutral,
        'positive': positive
    }
    return results

    # print("Sentence Overall Rated As", end=" ")

    # decide sentiment as positive, negative and neutral
    # if sentiment_dict['compound'] >= 0.05:
    #     print("Positive")
    #
    # elif sentiment_dict['compound'] <= - 0.05:
    #     print("Negative")
    #
    # else:
    #     print("Neutral")



