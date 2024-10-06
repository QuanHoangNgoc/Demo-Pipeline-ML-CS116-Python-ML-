#!/bin/bash

# Assigns the first command-line argument passed to the script to a variable named 'public_dir'. This is expected to be the directory containing the public data for training.
public_dir=$1

# Assigns the second command-line argument passed to the script to a variable named 'model_dir'. This is where the trained model will be saved.
model_dir=$2

# Executes the Python script named 'main.py' with the 'train' command, passing 'public_dir' and 'model_dir' as named arguments to specify the directories for the public data and model output, respectively.
python main.py train --public_dir "$public_dir" --model_dir "$model_dir"
