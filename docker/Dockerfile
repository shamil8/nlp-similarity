FROM python:3.8

RUN pip install --no-cache-dir gensim nltk flask

COPY .. /app

WORKDIR /app

CMD python api.py
