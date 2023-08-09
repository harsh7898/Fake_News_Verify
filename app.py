from flask import Flask, render_template, request
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import one_hot
from tensorflow.keras.preprocessing.sequence import pad_sequences

app = Flask(__name__)

# Load the model
model = load_model('fake_news_model.h5')

# Initialize nltk components
ps = PorterStemmer()
voc_size = 10000
sent_length = 5000

def review_cleaning(text):
    text = str(text).lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text

stop_words = set(stopwords.words("english"))

@app.route('/', methods=['GET', 'POST'])
def index():
    predicted_class = None
    predicted_proba = None

    if request.method == 'POST':
        user_input = request.form['user_input']

        # Preprocess the user input
        cleaned_input = review_cleaning(user_input)
        stemmed_input = [ps.stem(word) for word in cleaned_input.split() if not word in stop_words]
        input_corpus = ' '.join(stemmed_input)
        input_onehot_repr = [one_hot(input_corpus, voc_size)]
        input_padded = pad_sequences(input_onehot_repr, padding='pre', maxlen=sent_length)

        # Predict using the trained model
        prediction = model.predict(input_padded)

        # Classify and calculate probability
        predicted_class = "It's True" if prediction[0][0] >= 0.2 else "Seems a Fake News"

    return render_template('index.html', predicted_class=predicted_class)

if __name__ == '__main__':
    app.run(debug=True)
