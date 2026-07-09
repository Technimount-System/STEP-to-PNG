FROM python:3.14-slim

RUN apt-get update && apt-get install -y \
    libgl1 \
    libglx-mesa0 \
    libosmesa6 \
    libosmesa6-dev \
    libglu1-mesa \
    libxrender1 \
    libxext6 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD ["gunicorn", "main:app", "--bind", "0.0.0.0:10000"]