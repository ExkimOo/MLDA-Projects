import joblib

class SentimentClassifier(object):
    def __init__(self):
        self.model = joblib.load('my_LR_classifier.pkl')
        self.classes_dict = {0: 'Негативный отзыв', 1: 'Позитивный отзыв', -1: 'Ошибка предсказания'}
        
    def predict_text(self, text):
        try:
            lst = []
            lst.append(text)
            return self.model.predict(lst)
        except:
            print("Ошибка предсказания")
            return -1
              
    def get_prediction_message(self, text):
        prediction = self.predict_text(text)
        return self.classes_dict[int(prediction[0])]