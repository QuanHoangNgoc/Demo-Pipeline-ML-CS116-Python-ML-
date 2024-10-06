from sklearn.metrics import f1_score, recall_score, precision_score, accuracy_score
import os
import json
import ast
import argparse
import pandas as pd


def compute_score(y_true, y_pred):

    evaluation_results = {
        "main_metric": "F1 score",
        "overall_evaluation": {"F1 score": 100 * f1_score(y_true, y_pred),
                               "Accuracy": 100 * accuracy_score(y_true, y_pred)},
        "partial_evaluation": [],
    }

    return evaluation_results


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("true_path")
    parser.add_argument("pred_path")
    args = parser.parse_args()
    y_true = pd.read_json(os.path.join(args.true_path, "test.json"), lines=True)
    y_pred = pd.read_json(args.pred_path, lines=True)
    pd.DataFrame(y_pred, columns=['y']).to_json(os.path.splitext(args.pred_path)[0] + '_truncated.json', orient='records', lines=True)

    with open(os.path.splitext(args.pred_path)[0] + '_scores.json', 'w') as outfile:
        outfile.write(json.dumps(compute_score(y_true['y'], y_pred['y'])))
    
