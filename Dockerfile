FROM python:3.8

RUN pip install --no-cache-dir gensim

ENV PYRO_SERIALIZERS_ACCEPTED=pickle
ENV PYRO_SERIALIZER=pickle

ENV NS_HOST=9101

COPY main.py /main.py

EXPOSE 9100

CMD python /main.py --ns-host $NS_HOST
