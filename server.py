from flask import Flask, request
import tensorflow as tf
import numpy as np
import os

app = Flask(__name__)

model = None

def load_model(model_path):
    global model
    model = tf.keras.models.load_model(model_path)

@app.route("/test", methods=["POST"])
def test_model():
    csv = request.get_json()
    data = np.array(csv)
    result = model.predict(data)
    return str(result.tolist())

@app.route("/reload", methods=["POST"])
def reload_model():
    model_path = request.get_json()["model_path"]
    load_model(model_path)
    return "Model reloaded successfully."

if __name__ == "__main__":
    #model_path = os.environ.get("MODEL_PATH", "model.h5")
    model_path = '/home/kali/Desktop/shared2/savedmodel'
    load_model(model_path)
    app.run(debug=True)