# Spam_Email_Detection

A Machine Learning project that classifies emails as Spam or Not Spam (Ham) using Natural Language Processing (NLP) techniques and supervised learning algorithms.

# Project Overview

Spam emails are unsolicited messages that often contain advertisements, phishing attempts, or malicious content. This project uses machine learning and text processing techniques to automatically detect whether an email is spam or not.

The model is trained on a labeled email dataset and can predict the class of new email messages through a Flask web application.

## Project Structure
<img width="563" height="666" alt="image" src="https://github.com/user-attachments/assets/7eef9977-be92-43ab-b294-cccaf9db1559" />

## Technology Used 

- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Flask
- Pickle
- TF-IDF Vectorization

## Dataset

Label   Description
0       Not Spam (Ham)
1       Spam

Dataset References : https://www.kaggle.com/datasets/jackksoncsie/spam-email-dataset

## Data Preprocessing

The following preprocessing steps were applied:

1. Convert text to lowercase
2. Remove missing values
3. Convert all text to string format
4. Strip leading and trailing whitespace
5. Remove punctuation
6. TF-IDF Vectorization

## Machine Learning Models

Model 1: Random Forest Classifier
- Ensemble learning algorithm
- Handles high-dimensional text features effectively

Model 2: Decision Tree Classifier
- Popular baseline for text classification
- Fast and Efficient 

Model 3: Logistic Regression
- Strong performance on NLP tasks
- Provide probablity outputs

## Model Evaluation
Evaluation metrics used:

- Accuracy
- Precision
- Recall
- F1-Score

## Running the Application

### Clone the Repository

git clone: https://github.com/yourusername/Spam_Email_Detection.git cd Spam_Email_Detection



## Author

Nyi Khant Zaw

Aspiring Data Scientist & Machine Learning Engineer

## License

This project is licensed under the MIT License.

Feel free to use, modify, and distribute this project for educational and research purposes.
