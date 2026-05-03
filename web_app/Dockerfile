FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

ADD . .

EXPOSE 5004

CMD ["python", "app.py"]