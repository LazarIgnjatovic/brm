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

model_path = os.environ.get("MODEL_PATH", "/app/model")

@app.route("/test", methods=["POST"])
def test_model():
    model = tf.keras.models.load_model(model_path)
    csv = request.get_json()
    array = json.loads(csv)
    data = np.array(array, np.float64)
    result = model.predict(data)
    return str(result.tolist())
