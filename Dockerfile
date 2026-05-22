FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libglib2.0-0 libx11-6 libxcomposite1 libxdamage1 libxext6 \
    libxfixes3 libxrandr2 libxrender1 libxss1 libxtst6 \
    fonts-liberation libappindicator1 libatk-bridge2.0-0 \
    libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 \
    libfontconfig1 libfreetype6 libgbm1 libgcc1 libgconf-2-4 \
    libgdk-pixbuf1.0-0 libglvnd0 libgtk-3-0 libharfbuzz0b \
    libhttp-parser2.9 libice6 libnss3 libpango-1.0-0 \
    libpangocairo-1.0-0 libpixman-1-0 libsm6 libstdc++6 \
    libvulkan1 libx11-xcb1 libxcb-dri3-0 libxcb1 xdg-utils \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN playwright install --with-deps

COPY . .

CMD ["pytest"]
