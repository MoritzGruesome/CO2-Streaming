FROM python:3.12-slim

ENV DEBUG=True

WORKDIR /app

COPY kafkaProducer.py .

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "-u", "kafkaProducer.py"]