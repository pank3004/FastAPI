from pathlib import Path
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
import joblib


ARTIFACT_DIR = Path("artifacts")
ARTIFACT_DIR.mkdir(exist_ok=True)


# ----------------------------
# 1. Load Data
# ----------------------------
def load_data(csv_path: str) -> pd.DataFrame:
    return pd.read_csv(csv_path)


# ----------------------------
# 2. Split Features & Target
# ----------------------------
def split_features_target(df: pd.DataFrame):
    X = df.drop(columns="median_house_value")
    y = df["median_house_value"]
    return X, y


# ----------------------------
# 3. Build Preprocessor
# ----------------------------
def build_preprocessor(X: pd.DataFrame) -> ColumnTransformer:
    num_cols = X.select_dtypes(include=[np.number]).columns.tolist()
    cat_cols = X.select_dtypes(include=["object", "category"]).columns.tolist()

    num_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
        ]
    )

    cat_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("encoder", OneHotEncoder(drop="first", handle_unknown="ignore")),
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", num_pipeline, num_cols),
            ("cat", cat_pipeline, cat_cols),
        ]
    )

    return preprocessor


# ----------------------------
# 4. Train Model
# ----------------------------
def train_model(X_train, y_train):
    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42,
        n_jobs=-1
    )
    model.fit(X_train, y_train)
    return model


# ----------------------------
# 5. Save Artifacts
# ----------------------------
def save_artifacts(preprocessor, model):
    joblib.dump(preprocessor, ARTIFACT_DIR / "preprocessor.joblib")
    joblib.dump(model, ARTIFACT_DIR / "model.joblib")
    print("Artifacts saved successfully.")


# ----------------------------
# 6. Main Pipeline
# ----------------------------
def main():
    df = load_data("housing.csv")
    X, y = split_features_target(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    preprocessor = build_preprocessor(X)

    # Fit preprocessor ONLY on training data
    X_train_processed = preprocessor.fit_transform(X_train)
    X_test_processed = preprocessor.transform(X_test)

    model = train_model(X_train_processed, y_train)

    save_artifacts(preprocessor, model)

if __name__ == "__main__":
    main()
