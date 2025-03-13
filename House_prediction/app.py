from flask import Flask, request, jsonify
import pickle
import numpy as np
import logging


app = Flask(__name__)



# Configure logging
logging.basicConfig(filename='api.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')


# Load the saved models
with open('scaler.pkl', 'rb') as f:
    scaled = pickle.load(f)

with open('best_model_.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from request
        data = request.get_json(force=True)
        if 'features' not in data:
            raise ValueError("Missing 'features' key in request JSON")
        
        # Convert to NumPy array
        features = np.array(data['features'])
        
        #input data by user 
        logging.info(f"Input Data: {features}")
        

        # Remove index 3 value
        features = np.delete(features, 3) # AvgBedrms value which is not used in model
        
        # Apply log transformation on new indices 2, 3, and 4 (after re-indexing)
        indices_to_transform = [2, 3, 4]
        for idx in indices_to_transform:
            if idx < len(features):  # Check to avoid out-of-bounds errors
                features[idx] = np.log1p(features[idx])
        
        # Reshape for scaler
        features = features.reshape(1, -1)
        # Scale the transformed features
        scaled_features = scaled.transform(features)
        
        # Make prediction
        prediction = model.predict(scaled_features)

        # Log the prediction
        logging.info(f"Prediction: {prediction[0]}")
        
        return jsonify({'predicted_price': prediction[0]})
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)


   
