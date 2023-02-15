FROM tensorflow/tensorflow

WORKDIR /app

# Copy the necessary files into the container
COPY data .
COPY server.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENV MODEL_PATH=/app/model

CMD ["gunicorn", "-w 4", "-b", "0.0.0.0:8000", "--log-level", "debug", "server:app"]