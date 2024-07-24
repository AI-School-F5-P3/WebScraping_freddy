FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Instalar el cliente MySQL
RUN apt-get update && apt-get install -y default-mysql-client

CMD ["python", "src/main.py"]