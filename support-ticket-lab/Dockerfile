FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ticket_classifier.py .

EXPOSE 8080

CMD ["uvicorn", "ticket_classifier:app", "--host", "0.0.0.0", "--port", "8080"]
