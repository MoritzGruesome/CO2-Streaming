FROM python:3.12-slim

WORKDIR /app

COPY producer/kafkaProducer.py .

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "kafkaProducer.py"]