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

not_spam_email = "Subject: re : bei enron  gordian kemen on 03 / 15 / 2000 09 : 13 : 47 am  to : jens . gobel @ enron . com  cc :  subject : career opportunities @ enron  hi vince ,  following up to our chat on the phone .  gordian kemen will be arriving in austin on the 16 th . he will be staying in  austin for 2 weeks . he would very much appreciate to have the opportunity to  have a talk with you to find out if there is a place for him at enron . you  can reach him under ( 512 ) 301 - 9819 ( his parents in law ' s phone number ) .  thanks a lot for you help and attention ,  jens  - gordianresume . pdf"


print(spam_email_check(not_spam_email))

if __name__ == '__main__':
    app.run(debug = True)