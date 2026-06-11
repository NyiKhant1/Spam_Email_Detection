import pickle
from flask import Flask
import re
app = Flask(__name__)

vectorize = pickle.load(open('Data/Model/Vector.pkl','rb'))
model = pickle.load(open('Data/Model/MODEL2.pkl','rb'))


def spam_email_check(email):
    email = email.lower()
    email = re.sub(r"http\S+", " url ", email)
    text = re.sub(r"[^a-zA-Z ]", " ", email)
    email_vector = vectorize.transform([email])

    prediction = model.predict (email_vector)[0]

    return "Spam" if prediction == 1 else "Not Spam"


email = "WINNER!! As a valued network customer you have been selected to receivea Â£900 prize reward! To claim call 09061701461. Claim code KL341. Valid 12 hours only."

not_spam_email = "I'm gonna be home soon and i don't want to talk about this stuff anymore tonight, k? I've cried enough today."


print(spam_email_check(not_spam_email))
if __name__ == '__main__':
    app.run(debug = True)