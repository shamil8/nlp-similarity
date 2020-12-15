# NLP text similarity with Word2Vec and Gensim


# Data for this NLP

Reddit world news dataset: https://www.kaggle.com/rootuser/worldnews-on-reddit/tasks

Pretrain Word2vec model by Google
https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit

(you can find information about this model here: https://youtu.be/U0LOSHY7U5Q?t=2194)

# Docker and docker-compose
```docker
docker build -t intr_py:latest .

docker run --name intr_py -d -p 5000:5000 intr_py:latest

docker exec -it intr_py bash
```
For docker-compose
```docker
docker-compose build py

docker-compose up py
```