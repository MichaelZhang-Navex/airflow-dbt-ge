# initial launch

## build own image with extra package

```bash
docker build . -f Dockerfile --pull --tag my-image:0.0.1
```

## basic launch

```bash
mkdir -p ./dags ./logs ./plugins
echo -e "AIRFLOW_UID=$(id -u)" > .env

docker-compose up airflow-init
docker-compose up -d
```

Then put dags in ./dags


## enable encryption

I have put a key in file, but you can generate the key anywhere and put it in the docker-compose.yml

```bash
pip install cryptography
```

```python
from cryptography.fernet import Fernet

fernet_key = Fernet.generate_key()
print(fernet_key.decode())  # your fernet_key, keep it in secured place!
```

# Running the CLI commands

```bash
docker-compose run airflow-worker airflow info
```

## or a easier way

```bash
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.3.4/airflow.sh'
chmod +x airflow.sh
```

Then you can use the command like this:

```bash
./airflow.sh info

./airflow.sh bash

./airflow.sh python
```

# cleanning up

```bash
docker-compose down --volumes --rmi all
```

