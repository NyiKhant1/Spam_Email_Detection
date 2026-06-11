import pickle
from flask import Flask
import re
app = Flask(__name__)

vectorize = pickle.load(open('Data/Model/Vector.pkl','rb'))
model = pickle.load(open('Data/Model/MODEL1.pkl','rb'))


def spam_email_check(email):
    email = email.lower()
    email = re.
    email_vector = vectorize.transform([email])

    prediction = model.predict (email_vector)[0]

    return "Spam" if prediction == 1 else "Not Spam"


email = "Subject: 🚨 FINAL NOTICE: Your account will be suspended TODAY Body: Dear User, We have detected unusual activity on your account. To prevent permanent suspension, you must verify your identity immediately. Click the link below to confirm your account details: http://secure-verify-account-now-login.com If you do not complete verification within 24 hours, your account will be permanently locked and all data will be lost. Thank you, Account Security Team"
print (spam_email_check(email))



if __name__ == '__main__':
    app.run(debug = True)