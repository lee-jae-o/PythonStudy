# 단어 입력 받고 감정 출력
import sys

def sentiment_analysis(text):
    positive_words = ["good", "great", "awesome", "excellent"]
    negative_words = ["bad", "awful", "terrible", "horrible"]

    positive_count = sum(text.lower().count(word) for word in positive_words)
    negative_count = sum(text.lower().count(word) for word in negative_words)

    if positive_count > negative_count:
        return "Positive"
    elif negative_count > positive_count:
        return "Negative"
    else:
        return "Neutral"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        text = sys.argv[1]
    else:
        text = input("Enter text for sentiment analysis: ")

    result = sentiment_analysis(text)
    print(result)