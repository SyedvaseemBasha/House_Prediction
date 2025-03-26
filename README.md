# House_Prediction

House Price Prediction – Report & Documentation

This project is a machine learning application designed to predict house prices based on user inputs. It not only delivers robust prediction functionality but also incorporates MLflow for experiment tracking and model versioning, ensuring reproducibility and streamlined model updates.

---

## Project Structure

- **House_prediction.ipynb**  
  A Jupyter Notebook that documents the entire modeling workflow:
  - **Data Loading & EDA:** Load the dataset, explore data distributions, and visualize correlations.
  - **Data Preprocessing:** Handle missing values, perform scaling and encoding, and engineer features.
  - **Model Training & Evaluation:** Train regression models (e.g., Linear Regression, Decision Trees, Random Forest, XGBoost, CatBoost), evaluate using RMSE, MAE, and R² scores, and optimize using GridSearchCV or RandomizedSearchCV.
  - **Experiment Tracking:** Utilize MLflow for logging experiments and versioning models.
  - **Model Persistence:** Save the best-performing model using Pickle or Joblib.

- **app.py (Flask API)**  
  Implements a Flask-based API exposing a `/predict` endpoint:
  - Accepts POST requests with JSON data containing a `"features"` array.
  - Processes the input by removing an unused feature, applying log transformations to selected features, and scaling the data.
  - Returns the predicted house price as a JSON response.
  - Logs all input data and predictions in `api.log` for debugging and monitoring.  
  _See details in [app.py](House_prediction/app.py)._

- **api.log**  
  Maintains detailed runtime logs of the API, including incoming requests, prediction outputs, and error messages.

- **Dockerfile**  
  Provides the instructions to containerize the entire application for seamless deployment across different environments and provide local access to the `/predict` endpoint via Postman.

- **requirements.txt**  
  Lists all necessary Python dependencies, including Flask, NumPy, Pandas, scikit-learn, and MLflow for experiment tracking.

- **Streamlit_app.py**  
  Offers a user-friendly web interface built with Streamlit:
  - Users can input various house features using interactive sliders and number inputs.
  - The app processes these inputs in the same way as the Flask API and displays real-time predictions.

- **mlruns Folder**  
  Contains all the MLflow tracking logs and model version information for each experiment. This folder is crucial for monitoring experiments and retrieving historical model performance data.

---

## Approach

### 1. Data Exploration & Preprocessing
- **Data Loading & EDA:**  
  Loaded the dataset and performed exploratory data analysis (EDA) to understand feature distributions and correlations.
- **Data Cleaning:**  
  Handled missing values appropriately.
- **Feature Engineering:**  
  - **Feature Selection:** Removed redundant features (e.g., dropped `AveBedrms` due to high correlation with `AveRooms`).
  - **Transformations:** Applied log transformations to selected features (`AveOccup`, `Population`, `AveRooms`) to reduce skewness.
  - **Scaling:** Standardized features to ensure uniform scaling for model training.

### 2. Model Development & Optimization
- **Model Selection:**  
  Experimented with several regression models (Linear Regression, Decision Trees, Random Forest, XGBoost, CatBoost) to choose the best-performing model.
- **Hyperparameter Tuning:**  
  Optimized the selected model using GridSearchCV to identify the best hyperparameters.
- **Evaluation Metrics:**  
  Evaluated models using RMSE, MAE, and R² to determine performance.
- **Experiment Tracking:**  
  Integrated MLflow for logging parameters, metrics, and model versions, and stored experiment details in the `mlruns` folder.
- **Model Persistence:**  
  Saved the final model using Pickle for later use in the API.

### 3. API & Web Interface Implementation
- **Flask API (`app.py`):**  
  - Exposes a `/predict` endpoint.
  - Accepts POST requests with a JSON payload containing the `"features"` array.
  - Applies identical preprocessing (log transformation and scaling) as used during training.
  - Returns the prediction in JSON format.
- **Streamlit Web App (`Streamlit_app.py`):**  
  - Provides an interactive UI for non-technical users.
  - Collects feature inputs, applies preprocessing, and displays predictions.
- **Logging & Error Handling:**  
  Implemented logging in the Flask API (using Python’s `logging` module) to capture errors and request details.

### 4. Containerization & Deployment
- **Docker:**  
  A `Dockerfile` is provided to containerize the application, ensuring a consistent environment across deployments.
- **Deployment Options:**  
  The containerized application can be deployed locally or on cloud platforms like AWS, GCP, or Render.
- **Usage Guide:**  
  The API can be tested via Postman or CURL requests. For example, after deployment, send a POST request to `http://127.0.0.1:5000/predict` with the JSON body:
  ```json
  {
    "features": [8.3252, 41, 6.984127, 1.02381, 322, 2.555556, 37.88, -122.23]
  }


# Getting Started

## Prerequisites

- Python 3.9 or higher
- Docker (if deploying via container)
- Git

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/SyedvaseemBasha/House_Prediction.git 
   cd House_Prediction
   ```
2. **Install Requirements:**
   ```bash
   pip install -r requirements.txt
   ```
3. **MLflow for Experiment Tracking:** Start the MLflow UI to monitor experiments:
   ```bash
   mlflow ui
   ```
   Open [http://localhost:5000](http://localhost:5000) in your browser.

## Running the API Locally

1. **Running locally**

   - We have two ways :
      
      1. **Using Flask:**
         ```bash
         python app.py
         ```
         Your API will be accessible at: [http://127.0.0.1:5000](http://127.0.0.1:5000)
      
      2. **Using Docker:**
         - **Build the Docker Image:**
           ```bash
           docker build -t house-price-api .
           ```
         - **Run the Container:**
           ```bash
           docker run -p 5000:5000 house-price-api
           ```
         The Flask app will run inside a container and be accessible at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

2. **Testing the API via Postman:**
   - Set the method to **POST**.
   - URL: `http://127.0.0.1:5000/predict`
   - Body (raw JSON):
     ```json
     {
       "features": [8.3252, 41, 6.984127, 1.02381, 322, 2.555556, 37.88, -122.23]
     }
     ```
   - Expected Response:
     ```json
     {
       "predicted_price": <predicted_value>
     }
     ```

## Running the Streamlit Web App

Launch the interactive UI:
```bash
streamlit run Streamlit_app.py
```
Open the provided URL to access the web interface, input house features, and view predictions.

---

## Project Video Demo

https://github.com/user-attachments/assets/8d122b7d-f73e-4876-a5eb-a374174eb9cd


---------
## Final Notes

- **Model Versioning & Experiment Tracking:**  
  MLflow is integrated to keep track of experiments, parameters, and model performance. View the MLflow UI to compare different model versions.

- **Logging & Error Handling:**  
  The Flask API includes comprehensive logging and error handling to ensure smooth operation and easier debugging.

- **Deployment:**  
  The Dockerfile allows for seamless deployment in a production environment. The instructions above cover both local and containerized setups.

- **Code Quality & Reproducibility:**  
  All code is well-commented, ensuring clarity for future maintenance and reproducibility.




























