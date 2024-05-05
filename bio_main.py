from flask import Flask, request, jsonify
from sklearn.linear_model import LinearRegression
import joblib

# Load pre-trained machine learning model
model = joblib.load('abw_model.joblib')

app = Flask(__name__)

@app.route('/predict_abw', methods=['POST'])
def predict():
    # Get input data from request
    data = request.get_json()

    # Perform prediction using the loaded model
    prediction = model.predict([[data['bd_daya','sum_sample_g']]])

    # Return prediction as JSON response
    return jsonify({'sr%': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
