.PHONY: help
help:
	@echo "Welcome to {{cookiecutter.project_slug}}"
	@echo "======================================================="
	@echo ""
	@echo "Here are some of the most convenient commands:"
	@echo ""
	@echo "- init                Prepares local dev environment for development"
	@echo "- check               Runs linter and type checker"
	@echo "- fix                 Formats and fixes imports in all Python files"
	@echo "- migrate             Runs migrations"
	@echo "- env                 Starts environment and seeds examples data, destroys current environment!"
	@echo "- test                Runs all tests, requires a database"
	@echo "- workers             Starts a cluster of worker processes"
	@echo "- run                 Starts the development web server on localhost:8000"
	@echo "- migrations          Creates migrations based on models.py change"
	@echo "- migrations.delete   Deletes all migrations from {{cookiecutter.project_slug}}/*"
	@echo "- graph               Renders a graph with all models in graph.png"
	@echo ""
	@echo "Here are some of the low-level convenient commands:"
	@echo ""
	@echo "- docker              Starts environment with Postgres and Redis using docker-compose, destroys current environment"
	@echo "- data                Runs migrations, creates default user, groups and data"
	@echo "- test.<app>          Runs only the <app> tests, requires a database"
	@echo "- check.lint          Runs linter"
	@echo "- check.types         Runs type checker"

.PHONY: init
init:
	( \
		python3 -m venv .venv; \
		source .venv/bin/activate; \
		pip install -r requirements.txt; \
		pip install flake8 black mypy django-stubs types-redis autoflake psycopg2-binary djhtml; \
		cp -u .env.sample .env; \
		git init .; \
		echo "Local environment ready, run 'source .venv/bin/activate' to start"; \
	)

.PHONY: check.lint
check.lint:
	flake8 . --count --show-source --statistics
	djhtml {{cookiecutter.project_slug}}/templates/*/** -c -t 2

.PHONY: check.types
check.types:
	mypy .

.PHONY: check
check: check.lint check.types

.PHONY: fix
fix:
	black . --experimental-string-processing
	autoflake --in-place --remove-unused-variables --remove-all-unused-imports --remove-duplicate-keys .
	djhtml {{cookiecutter.project_slug}}/templates/*/** -i -t 2

.PHONY: test.all
test.all:
	DJANGO_SETTINGS_MODULE=config.settings.test python manage.py test {{cookiecutter.project_slug}}

.PHONY: test
test:
	DJANGO_SETTINGS_MODULE=config.settings.test python manage.py test --failfast {{cookiecutter.project_slug}}

.PHONY: migrations
migrations:
	python manage.py makemigrations

.PHONY: migrate
migrate:
	python manage.py migrate

.PHONE: env
env: docker data

.PHONY: run
run:
	python manage.py runserver

.PHONY: workers
workers:
	python manage.py qcluster

.PHONY: graph
graph:
	python manage.py graph_models -a --pygraphviz --output models.png

.PHONY: docker
docker:
	docker-compose -f docker-compose.dev.yml down
	docker-compose -f docker-compose.dev.yml up -d

.PHONY: data
data:
	python manage.py migrate
	python manage.py loaddata {{cookiecutter.project_slug}}/fixtures/default/*
	python manage.py loaddata {{cookiecutter.project_slug}}/fixtures/example/*

.PHONE: migrations.delete
migrations.delete:
	find . -path "./{{cookiecutter.project_slug}}/*/migrations/*.py" -not -name "__init__.py" -delete
