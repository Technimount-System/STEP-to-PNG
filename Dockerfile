FROM python:3.14-slim

RUN apt-get update && apt-get install -y \
    libosmesa6 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD ["gunicorn", "main:app", "--bind", "0.0.0.0:10000"]