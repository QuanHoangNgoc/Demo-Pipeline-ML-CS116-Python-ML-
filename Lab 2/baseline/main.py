import argparse
import sys
import os
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from joblib import dump, load
from sklearn.pipeline import Pipeline  
from sklearn.decomposition import PCA
from sklearn.compose import ColumnTransformer  
from sklearn.linear_model import LogisticRegression  
from sklearn.neighbors import KNeighborsClassifier  
from sklearn.svm import SVC  
from sklearn.ensemble import RandomForestClassifier  
from sklearn.metrics import classification_report 
from sklearn.model_selection import train_test_split, GridSearchCV  
from sklearn.neural_network import MLPClassifier  


final_IF = [0, 2, 5, 6, 8, 9, 10, 11, 12, 13, 15, 18, 19, 22, 
        28, 30, 32, 33, 35, 39, 41, 42, 44, 45, 50, 51, 52, 53, 
        54, 56, 58, 65, 68, 74, 77, 82, 83, 84, 85, 86, 87, 88, 
        89, 91, 92, 94, 96, 97]
    

# Defines a function for training the model.
def run_train(public_dir, model_dir):
    # Ensures the model directory exists, creates it if it doesn't.
    os.makedirs(model_dir, exist_ok=True)

    # Constructs the path to the training data file.
    train_file = os.path.join(public_dir, 'train.npz')

    # Loads the training data from the .npz file.
    train_data = np.load(train_file)

    # Extracts the features from the training data.
    X_train = train_data['X_train'][:-250]

    # Extracts the labels from the training data.
    y_train = train_data['y_train'][:-250] 



    # Instantiates the logistic regression model.
    X_train = X_train[:, :] #!!!
    mlp = MLPClassifier(
        # shuffle=True, 
        # learning_rate_init=0.001, 
        # batch_size=32,
        # alpha=0.0001, 
        hidden_layer_sizes=(100, 100),  # Two hidden layers with 100 neurons each
        activation='relu',             # ReLU activation function  
        solver='adam',                 # Adam optimizer  
        # max_iter=500, early_stopping=True,                  # Max iterations for training  
        random_state=42,               # Seed for reproducibility  
        verbose=True)
    pipeline = Pipeline([  
        ('pca', PCA(random_state=42, n_components=30)),  # Preprocessing step  
        ('classifier', mlp)  # The classifier  
    ])  

    # Fits the model to the training data.
    pipeline.fit(X_train, y_train)

    # Defines the path for saving the trained model.
    model_path = os.path.join(model_dir, 'trained_model.joblib')

    # Saves the trained model to the specified path.
    dump(pipeline, model_path)


# Defines a function for making predictions.
def run_predict(model_dir, public_dir, output_path):
    # Specifies the path to the trained model.
    model_path = os.path.join(model_dir, 'trained_model.joblib')

    # Constructs the path to the test data file.
    test_file = os.path.join(public_dir, 'test.npz')

    # Loads the trained model from file.
    model = load(model_path)

    # Loads the test data from the .npz file.
    test_data = np.load(test_file)

    # Extracts the features from the test data.
    X_test = test_data['X_test']
    X_test = X_test[:, :] #!!!

    # Predicts and saves results.
    pd.DataFrame({'y': model.predict(X_test)}).to_json(output_path, orient='records', lines=True)


# Defines the main function that parses commands and arguments.
def main():
    # Initializes a parser for command-line arguments.
    parser = argparse.ArgumentParser()

    # Creates subparsers for different commands.
    subparsers = parser.add_subparsers(dest='command')

    # Adds a subparser for the 'train' command.
    parser_train = subparsers.add_parser('train')

    # Adds an argument for the directory containing public data.
    parser_train.add_argument('--public_dir', type=str)

    # Adds an argument for the directory to save the model.
    parser_train.add_argument('--model_dir', type=str)

    # Adds a subparser for the 'predict' command.
    parser_predict = subparsers.add_parser('predict')

    # Adds an argument for the directory containing the model.
    parser_predict.add_argument('--model_dir', type=str)

    # Adds an argument for the directory containing public data.
    parser_predict.add_argument('--public_dir', type=str)

    # Adds an argument for the path to save prediction results.
    parser_predict.add_argument('--output_path', type=str)

    # Parses the command-line arguments.
    args = parser.parse_args()

    if args.command == 'train':
        # Checks if the 'train' command was given.
        # Calls the function to train the model.
        run_train(args.public_dir, args.model_dir)
    elif args.command == 'predict':
        # Checks if the 'predict' command was given.
        # Calls the function to make predictions.
        run_predict(args.model_dir, args.public_dir, args.output_path) 
    else:
        # If no valid command was given, prints the help message.
        # Displays help message for the CLI.
        parser.print_help()

        # Exits the script with a status code indicating an error.
        sys.exit(1)


# Checks if the script is being run as the main program.
if __name__ == "__main__":
    # Calls the main function if the script is executed directly.
    main()
