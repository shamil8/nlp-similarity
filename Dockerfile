FROM python:3.8

ENV MYSQL_HOST=0.0.0.0
ENV MYSQL_PORT=3306
ENV MYSQL_USER=root
ENV MYSQL_PASS=root
ENV MYSQL_DB=initiator

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir gensim nltk flask numpy pandas
RUN pip install mysql-connector-python
RUN pip install xlsxwriter

# FOR CORS
RUN pip install -U flask-cors

COPY ./ ./app

WORKDIR /app

CMD python api.py

# docker cp intr_dev_py:/app/data/tasks.csv ./data/file.tasks