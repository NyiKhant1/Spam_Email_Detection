import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

vectorize = TfidfVectorizer()

model = pickle.load(open('Data/Model/MODEL1.pkl','rb'))


def spam_email_check(email):
    email_vector = vectorize.transform([email])

    prediction = email.predict (email_vector) [0]

    return "Spam" if prediction == 1 else 
