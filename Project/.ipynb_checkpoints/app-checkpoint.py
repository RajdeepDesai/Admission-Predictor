from flask import Flask, render_template, request
import numpy as np
import joblib

# Create Flask app
app = Flask(__name__)

# Load your trained model
model = joblib.load('admission_model.pkl')

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get form values
    gre = float(request.form['gre'])
    toefl = float(request.form['toefl'])
    rating = float(request.form['rating'])
    sop = float(request.form['sop'])
    lor = float(request.form['lor'])
    cgpa = float(request.form['cgpa'])
    research = int(request.form['research'])

    # Make prediction
    input_data = np.array([[gre, toefl, rating, sop, lor, cgpa, research]])
    prediction = model.predict(input_data)[0]
    prediction = round(prediction * 100, 2)

    return render_template('index.html', prediction=prediction)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
