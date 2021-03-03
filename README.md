# NLP text similarity with Word2Vec and Gensim


# Other NLP wordvectors models

RNC and Wiki models: https://disk.yandex.ru/d/yTSQk55lThf4og

Main NLP data website http://vectors.nlpl.eu/repository/

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
