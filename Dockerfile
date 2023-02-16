FROM tensorflow/tensorflow

WORKDIR /app

COPY server.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "-w 4", "-b", "0.0.0.0:8000", "--log-level", "debug", "server:app"]