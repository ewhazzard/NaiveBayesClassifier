# Naive Bayes classifier for IT 340 Project 2 by Evan Hazzard
# Ask user for input and meta data, create a Naive Bayes classifier, and predict the classification of test data

print("Welcome to my Naive Bayes Classifier! Select one of the following items to continue.")
selection = '1'
while(selection != '3'):
    print("1. Input your training data and metadata files")
    print("2. Classify testing data")
    print("3. Exit")
    selection = input()
    if selection == '1':
        train_data = input("Name of training data file: ")
        meta_data = input("Name of meta data file: ")
    elif selection == '2':
        test_data = input("Name of test data: ")




