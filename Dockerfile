FROM python:3.8

RUN pip install --upgrade pip
RUN pip install --no-cache-dir gensim nltk flask numpy

COPY ./ ./app

WORKDIR /app

CMD python api.py
