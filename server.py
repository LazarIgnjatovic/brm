from flask import Flask, request
import json
import tensorflow as tf
import numpy as np
import logging
import os

app = Flask(__name__)

if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

model = None
model_path = os.environ.get("MODEL_PATH", "/app/model")

def load_model(model_path):
    global model
    app.logger.info('Loading model...')
    model = tf.keras.models.load_model(model_path)
    app.logger.info('Model loaded!')

@app.route("/test", methods=["POST"])
def test_model():
    load_model(model_path)
    csv = request.get_json()
    array = json.loads(csv)
    data = np.array(array, np.float64)
    result = model.predict(data)
    return str(result.tolist())

# @app.route("/reload", methods=["POST"])
# def reload_model():
#     load_model(model_path)
#     return "Model reloaded successfully."

# if __name__ == "__main__":
#     load_model(model_path)
#     app.run(debug=True)