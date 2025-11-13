FROM python:3.12-slim

WORKDIR /app

COPY consumer/kafkaConsumer.py .

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "-u", "kafkaConsumer.py"]