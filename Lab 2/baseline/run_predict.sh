#!/bin/bash

# Assigns the first command-line argument passed to the script to a variable named model_dir.
model_dir=$1

# Assigns the second command-line argument passed to the script to a variable named public_dir.
public_dir=$2

# Assigns the third command-line argument passed to the script to a variable named output_path.
output_path=$3

# Executes the Python script 'main.py' with the 'predict' command, passing the model_dir, public_dir, and output_path as arguments.
python main.py predict --model_dir "$model_dir" --public_dir "$public_dir" --output_path "$output_path"
