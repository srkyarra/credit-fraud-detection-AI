import json
import boto3
import pickle
import os
import numpy as np

s3 = boto3.client("s3")

MODEL_PATH = "/tmp/model.pkl"
BUCKET = os.environ["MODEL_BUCKET"]
KEY = os.environ["MODEL_KEY"]

# Load model on cold start
def load_model():
    if not os.path.exists(MODEL_PATH):
        s3.download_file(BUCKET, KEY, MODEL_PATH)
    with open(MODEL_PATH, "rb") as f:
        return pickle.load(f)

model = load_model()

def lambda_handler(event, context):
    body = json.loads(event["body"])

    features = np.array(body["features"]).reshape(1, -1)
    pred = model.predict(features)

    return {
        "statusCode": 200,
        "body": json.dumps({"fraud_prediction": int(pred[0])})
    }
