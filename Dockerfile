FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Assuming your application code resides in a folder named "app" within the project directory
COPY app/ ./app

EXPOSE 5000
# Define Uvicorn command (assuming your main application file is main.py)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]
