FROM python:3.11

RUN apt-get update && apt-get install -y imagemagick

WORKDIR /app

RUN chmod 777 -R /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "-m", "streamlit", "run", "app.py"]