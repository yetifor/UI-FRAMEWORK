FROM mcr.microsoft.com/playwright/python:v1.50.1-noble

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN playwright install

COPY . .

CMD ["pytest"]
