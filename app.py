from flask import Flask, render_template, request
import pickle

# Create Flask app
app = Flask(__name__)

# Load ML model
with open("grievance_model.pkl", "rb") as file:
    model = pickle.load(file)

# Load vectorizer
with open("vectorizer.pkl", "rb") as file:
    vectorizer = pickle.load(file)

# Load encoder
with open("label_encoder.pkl", "rb") as file:
    encoder = pickle.load(file)


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Prediction route
@app.route("/predict", methods=["POST"])
def predict():

    # Get user complaint
    complaint = request.form["complaint"]

    # Convert text into vectors
    text_vector = vectorizer.transform([complaint])

    # Predict department
    prediction = model.predict(text_vector)

    # Convert label number to text
    department = encoder.inverse_transform(prediction)[0]

    return render_template(
        "index.html",
        prediction_text=f"Predicted Department: {department}"
    )


# Run app
if __name__ == "__main__":
    app.run(debug=True)