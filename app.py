import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from flask import Flask, request, jsonify, render_template
import io
import base64
from PIL import Image

# Load the pre-trained model
model = load_model('pretrained_model.keras')

# Initialize the Flask app
app = Flask(__name__)

# Define a function to preprocess the user's image
def preprocess_image(image):
    image = image.resize((100, 100))
    image = np.array(image)
    image = image.reshape(1, 100, 100, 3)
    image = image / 255.0
    return image

# Define the route for the home page
@app.route('/')
def home():
    return render_template('index.html')  # Create an HTML file for the form

# Define the route for image upload and prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the uploaded image from the request
        uploaded_file = request.files['file']
        image = Image.open(uploaded_file)
        
        # Preprocess the image
        preprocessed_image = preprocess_image(image)
        
        # Make a prediction
        prediction = model.predict(preprocessed_image)
        prediction_label = "cat" if prediction > 0.5 else "dog"
        
        return jsonify({'prediction': prediction_label})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
