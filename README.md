
# Spam Mail Prediction with FastAPI

This project demonstrates a simple web application using FastAPI to predict whether an email is spam or ham (non-spam). It utilizes a machine learning model trained on email content data to make predictions.

## Setup

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Selva73582/spam-mail-prediction.git
   cd spam-mail-prediction
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```
   The `--reload` flag enables auto-reloading when code changes are detected.

2. Open your web browser and go to `http://localhost:8000` to access the application.

3. Enter email content into the form and click "Predict" to see the prediction result.

## Project Structure

- **`main.py`**: Contains the FastAPI application setup, endpoints, and logic for handling predictions.
- **`templates/form.html`**: HTML template for the web form where users enter email content.
- **`transformModel.pkl`**: Pre-trained transformer model (if applicable) for text preprocessing.
- **`logistic.pkl`**: Pre-trained logistic regression model for spam classification.
- **`requirements.txt`**: List of Python dependencies.

## Dependencies

- `fastapi==0.68.0`: Web framework for building APIs with Python.
- `uvicorn==0.15.0`: ASGI server implementation used to run FastAPI applications.
- `joblib==1.1.0`: Library for serialization and deserialization of Python objects (used for model loading).
- `scikit-learn==0.24.2`: Machine learning library for Python.

## Notes

- Ensure that Python 3.7 or higher is installed.
- Models (`transformModel.pkl` and `logistic.pkl`) should be trained and saved separately.
- Customize the HTML template (`form.html`) and FastAPI logic (`main.py`) as per your application's requirements.

