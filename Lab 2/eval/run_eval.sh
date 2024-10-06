#!/bin/bash

true_path=$1
pred_path=$2

python compute_score.py "$true_path" "$pred_path"