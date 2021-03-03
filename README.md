# NLP text similarity with Word2Vec and Gensim


# Data for this NLP

Reddit world news dataset: https://www.kaggle.com/rootuser/worldnews-on-reddit/tasks

Pretrain Word2vec model by Google
https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit

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

#Upgrade data
For updating tasks: `python -c 'from connector.tasks_to_csv import upgrade_tasks; upgrade_tasks()'`

You also can update the `tasks.csv` file so: `http://localhost:5001/upgrade-tasks`
