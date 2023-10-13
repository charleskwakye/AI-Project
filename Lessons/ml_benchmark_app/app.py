import streamlit as st
import time
import pandas as pd
import numpy as np

st.title("🔬 Benchmarks of 3 machine learning models on a Bank notes dataset. ")

# subheader
st.header("📝 Dataset used is the bank notes dataset from UCI")

st.write("This dataset contains information about bank notes which was extracted from images that were taken for the evaluation of an authentication procedure for banknotes.The dataset contains 1372 rows and 5 columns. The columns are: variance, skewness, curtosis, entropy and class.")


st.subheader("Exploratory Data Analysis")
st.write("1. Before I could train the models, I had to do some exploratory data analysis. I loaded the data into a pandas dataframe.")
# use banknotes.csv file and show the first 5 rows
bank_notes_data = pd.read_csv("resources/bank_notes.csv")
bank_notes_data.head()
st.table(bank_notes_data.head())

st.write("I noticed a columm named 'Target' which was the Label showing whether a note is authentic or not. I renamed the column to 'Authentication' for my own understanding of the dataset")
bank_notes_data = bank_notes_data.rename(columns={"Target": "Authentication"})
st.table(bank_notes_data.head())

st.write("2. I checked for missing values in the dataset. I noticed that there were no missing values in the dataset. All the columns had 1372 non-null values.")
st.table(bank_notes_data.isnull().sum())

st.write("3. I checked the attributes and instances to make sure that the dataset meets the minimum requirements for the task given.")
st.metric(label="Attributes", value=bank_notes_data.shape[1])
st.metric(label="Instances", value=bank_notes_data.shape[0])

st.write("4. I checked the data types of the columns in the dataset. I noticed that all the columns were of type float64 except the Authentication column which was of type int64.")
st.table(bank_notes_data.dtypes)

st.write("5. I checked for outliers in the dataset. I noticed that there were outliers in the dataset. I used the boxplot to visualize the outliers.")
st.image("resources/output.png")
st.write("Since the outliers were due to natural variation in the data, I decided to leave them in the dataset.")

st.write("I decided to normalize my data since I would training this data on different models. I used the MinMaxScaler to normalize the data.")

bank_notes_data = pd.read_csv("resources/bank_notes_scaled.csv")
st.table(bank_notes_data.head())

st.write("6. I trained the models on Decision Tree Classifier, Gaussian Naive Bayes and Gradient Boosting algorithms. I used the train_test_split function to split the data into training and testing sets. I used 75% of the data for training and 25% for testing.")
st.write("The visualization below show the decision tree")
st.image("resources/tree_output.png")


st.subheader("Model Benchmarking and Performances")

st.write("I used a confusion matrix to evaluate the performance of the models. The confusion matrix shows the number of true positives, true negatives, false positives and false negatives. I changed the labels of these to Real and Fake to show how many real and fake notes which were predicted by the models are correct and incorrect.")
st.image("resources/tree_benchmark.png")
st.image("resources/gaussian_benchmark.png")
st.image("resources/gradient_benchmark.png")
st.write("*. Gradient boosting is the best model among the three, with an accuracy of 0.997 or 1 most of the time and only one error. It correctly classified all the real bank notes and almost all the fake bank notes. The Gradient boostong being accurate than the other two models is not surprising because it is an ensemble technique that combines multiple weak learners (such as decision trees) into a strong learner by iteratively adding new learners that correct the errors of the previous ones. In simple terms, a gradient boosting classifier learns from the mistakes of the previous classifiers and improves the accuracy of the final prediction.")
st.write("*. Decision tree is the second best model, with an accuracy of 0.988 and mostly behind Gradient boosting and four errors. It also correctly classified all the real bank notes, but misclassified four fake bank notes as real.")
st.write("*. Gaussian naive Bayes is the worst model, with an accuracy of 0.851 and always last and 51 errors. It misclassified 21 real bank notes as fake and 30 fake bank notes as real.")

st.write("I also used a simple bar chart to display the accuracy of the models.")
st.image("resources/bar.png")


# #load models using pickle resources/saved_models/decisionTreeClassifierCM.pkl","rb"
# import pickle

# # load the model from disk
# decision_tree_model = pickle.load(open("resources/saved_models/decisionTreeClassifierCM.pkl", 'rb'))
# gaussian_model = pickle.load(open("resources/saved_models/gaussianAlgoPredCM.pkl", 'rb'))
# gradient_boost_model = pickle.load(open("resources/saved_models/gradientBoostingAlgoPredCM.pkl", 'rb'))

# age = st.slider('How old are you?', 0, 1, 0)
# st.write("I'm ", age, 'years old')

#  #input variance, skewness, curtosis, entropy
# variance = st.number_input("Enter variance")
# skewness = st.number_input("Enter skewness")
# curtosis = st.number_input("Enter curtosis")
# entropy = st.number_input("Enter entropy")

# model = st.radio(
#     "What's your favorite movie genre",
#     [ "Gradient Boosting", "Decision Tree", "Gaussian Naieve Bayes"],
#     captions = ["Best", "Second Best", "Third Best"])


# if model == 'Gradient Boosting':
#     st.write('You selected Gradient Boosting')
# elif model == 'Decision Tree':
#     st.write("You selected Decision Tree")
# else:
#     st.write("You selected Gaussian Naieve Bayes")