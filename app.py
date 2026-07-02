from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("regmodel.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
poly = pickle.load(open("poly.pkl", "rb"))

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict", methods=["POST"])
def predict():

    features = [float(x) for x in request.form.values()]

    features = np.array(features).reshape(1, -1)

    # Step 1: Standardize
    features = scaler.transform(features)

    # Step 2: Polynomial transformation
    features = poly.transform(features)

    # Step 3: Prediction
    prediction = model.predict(features)

    return render_template(
        "home.html",
        prediction_text=f"Predicted House Price : {prediction[0]:.2f}"
    )

if __name__ == "__main__":
    app.run(debug=True)