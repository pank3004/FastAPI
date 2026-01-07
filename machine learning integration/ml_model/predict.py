import joblib
import pandas as pd
from pathlib import Path
import numpy as np
from typing import List



# ----------------------------
# Load Artifacts
# ----------------------------
ARTIFACT_DIR = Path("artifacts")

preprocessor = joblib.load(ARTIFACT_DIR / "preprocessor.joblib")
model = joblib.load(ARTIFACT_DIR / "model.joblib")

print("Preprocessor and Model loaded successfully.")


# ----------------------------
# Prediction Function
# ----------------------------
def make_prediction(data: dict) -> float:
    """
    data: dictionary with raw input features
    returns: predicted median house value
    """

    input_df = pd.DataFrame([data])

    # Apply preprocessing
    processed_data = preprocessor.transform(input_df)

    # Predict
    prediction = model.predict(processed_data)

    return float(prediction[0])  # model by default return prediction in numpy array


def batch_prediction(data: List[dict])-> np.array: 
    input_df = pd.DataFrame(data)

    # Apply preprocessing
    processed_data = preprocessor.transform(input_df)

    # Predict
    predictions = model.predict(processed_data)

    return predictions
