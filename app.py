from flask import Flask, render_template, request
import pandas as pd
from pathlib import Path

from src.house_price_prediction.utils.common import load_bin

app = Flask(__name__)

# Load trained model
MODEL_PATH = Path("artifacts/model_trainer/model.joblib")
model = load_bin(MODEL_PATH)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Collect inputs from form
        data = {
            "bedrooms": int(request.form["bedrooms"]),
            "bathrooms": float(request.form["bathrooms"]),
            "sqft_living": int(request.form["sqft_living"]),
            "sqft_lot": int(request.form["sqft_lot"]),
            "floors": float(request.form["floors"]),
            "waterfront": int(request.form["waterfront"]),
            "view": int(request.form["view"]),
            "condition": int(request.form["condition"]),
            "sqft_above": int(request.form["sqft_above"]),
            "sqft_basement": int(request.form["sqft_basement"]),
            "yr_built": int(request.form["yr_built"]),
            "yr_renovated": int(request.form["yr_renovated"]),
        }

        # Convert to DataFrame
        input_df = pd.DataFrame([data])

        # Predict
        prediction = model.predict(input_df)[0]

        return render_template(
            "result.html",
            prediction=round(prediction, 2)
        )

    except Exception as e:
        return render_template(
            "result.html",
            error="Error occurred during prediction"
        )


if __name__ == "__main__":
    app.run(debug=True)