dev:
	python3 manage.py runserver
	
install:
	poetry install

new_app:
	#django-admin startapp app_name

PORT ?= 8000
start:
	gunicorn task_manager.wsgi

lint:
	poetry run flake8

# тесты
test:
	python3 manage.py test

pytest:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=task_manager --cov-report xml

# миграции
create_model:
	python manage.py makemigrations

migration:
	python manage.py sqlmigrate {app_name} 0001

commit_migration:
	python manage.py migrate

# создание пакетов для различных языков
trans:
	django-admin makemessages -l en_us

compile:
	django-admin compilemessages

# деплой на railway.app
railway:
	python manage.py migrate
	gunicorn task_manager.wsgi

# стандартная директория установки поетри
do_poetry:
	export PATH="$HOME/.local/bin:$PATH"

# старт серверов базы данных
dbstart:
	sudo service postgresql start