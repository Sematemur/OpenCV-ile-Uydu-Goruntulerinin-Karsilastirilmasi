FROM python:3.9-slim

WORKDIR /app

# API requirements
COPY API/requirements.txt ./api_requirements.txt
RUN pip install --no-cache-dir -r api_requirements.txt

# ARAYUZ requirements
COPY ARAYUZ/requirements.txt ./arayuz_requirements.txt
RUN pip install --no-cache-dir -r arayuz_requirements.txt

# API dosyaları
COPY API/ ./API/

# ARAYUZ dosyaları
COPY ARAYUZ/ ./ARAYUZ/

# Start script
COPY start.sh .
RUN chmod +x start.sh

EXPOSE 8000 8501
CMD ["./start.sh"]
