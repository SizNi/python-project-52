dev:
	python3 manage.py runserver
	
install:
	poetry install

pytest:
	poetry run pytest

server:
	sudo service postgresql start

new_app:
	#django-admin startapp app_name

create_model: # Миграция (сообщаем джанго, что создали новую модель в models.py)
	python manage.py makemigrations

migration: # заводим модель в базу данных (название модели и ее номер)
	python manage.py sqlmigrate {app_name} 0001

commit_migration: # подтверждаем миграцию (как push в гите после коммита)
	python manage.py migrate

PORT ?= 8000
start:
	gunicorn task_manager.wsgi

trans:
	django-admin makemessages -l ru

compile:
	django-admin compilemessages

dbstart:
	sudo service postgresql start

do_poetry:
	export PATH="$HOME/.local/bin:$PATH"