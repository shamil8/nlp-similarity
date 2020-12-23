FROM python:3.8

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir gensim nltk flask numpy pandas
RUN pip install mysql-connector-python
RUN pip install xlsxwriter

COPY ./ ./app

WORKDIR /app

CMD python api.py
