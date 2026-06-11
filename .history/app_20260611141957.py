import pickle
from flask import Flask
import re
app = Flask(__name__)

vectorize = pickle.load(open('Data/Model/Vector.pkl','rb'))
model = pickle.load(open('Data/Model/MODEL2.pkl','rb'))


def spam_email_check(email):
    email = email.lower()
    email = re.sub(r"http\S+", " url ", email)
    email = re.sub(r"[^a-zA-Z ]", " ", email)
    email_vector = vectorize.transform([email])

    prediction = model.predict (email_vector)[0]

    return "Spam" if prediction == 1 else "Ham"


# email = "XXXMobileMovieClub: To use your credit, click the WAP link in the next txt message or click here>> http://wap. xxxmobilemovieclub.com?n=QJKGIGHJJGCBL"

not_spam_email = "Go until jurong point, crazy.. Available only in bugis n great world la e buffet... Cine there got amore wat..."


print(spam_email_check(not_spam_email))

if __name__ == '__main__':
    app.run(debug = True)