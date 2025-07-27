#!/bin/bash

# API'yi başlat
cd /app/API
uvicorn main:app --host 0.0.0.0 --port 8000 &

# Streamlit (Arayüz) başlat
cd /app/ARAYUZ
streamlit run arayuz.py --server.port=8501 --server.address=0.0.0.0 &

# Processleri bekle
wait
