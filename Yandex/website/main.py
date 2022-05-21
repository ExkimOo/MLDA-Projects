from flask import Flask, render_template, request

from sentiment_classifier import SentimentClassifier

app = Flask(__name__)
classifier = SentimentClassifier()


@app.route("/", methods=["POST", "GET"])
def index_page(text="", prediction_message=""):
    if request.method == "POST":
        text = request.form["text"]
        prediction_message = classifier.get_prediction_message(text)
    return render_template('predict.html', text=text, prediction_message=prediction_message)


if __name__ == '__main__':
    app.run(debug=False, port=8080)
