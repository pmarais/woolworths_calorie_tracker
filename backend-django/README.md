# Django CRUD backend

1. Create a virtualenvironment `mkdir _venv` and `virtualenv --python=python3 _venv/`
2. Activate the virtualenv with `source _venv/bin/activate`
3. `cd t57/`
4. `./manage.py makemigrations`
5. `./manage.py migrate`
6. `./manage.py runserver`

## Install RabbitMQ

1. `brew intall rabbitmq`
2. `rabbitmq-server start -detached`

## Run celery

1. Installation should be sorted with above setup
2. `cwd to t57/` where `manage.py` can be found
3. `celery -A t57 worker -l INFO`