.PHONY: help
help:
	@echo "Welcome to {{cookiecutter.project_name}}"
	@echo "======================================================="
	@echo ""
	@echo "Here are some of the most convenient commands:"
	@echo ""
	@echo "- docker              Starts environment with Postgres and Redis using docker-compose, destroys current environment"
	@echo "- data                Runs migrations, creates default user, groups and data"
	@echo "- check               Runs linter and type checker"
	@echo "- fix                 Formats all files and fixes imports"
	@echo "- migrate             Runs migrations"
	@echo "- env                 Starts environment and seeds examples data, destroys current environment!"
	@echo "- test                Runs all tests, requires a database"
	@echo "- shell               Starts an interactive shell with all models imported"
	@echo "- workers             Starts a cluster of worker processes"
	@echo "- run                 Starts the development web server on localhost:8000"
	@echo "- migrations          Creates migrations based on models.py change"
	@echo ""
	@echo "Here are some of less used commands:"
	@echo ""
	@echo "- graph               Renders a graph with all models in graph.png"
	@echo "- check.lint          Runs linter"
	@echo "- check.types         Runs type checker"

.PHONY: check.lint
check.lint:
	pre-commit run --show-diff-on-failure -a

.PHONY: check.types
check.types:
	pyright

.PHONY: check
check: check.lint check.types

.PHONY: fix
fix:
	isort --profile black .
	black . --preview
	autoflake --in-place --remove-unused-variables --remove-all-unused-imports --remove-duplicate-keys .
	djhtml {{cookiecutter.project_slug}}/templates/**/*.html -i -t 2

.PHONY: test
test:
	DJANGO_READ_DOT_ENV_FILE=True pytest

.PHONY: shell
shell:
	DJANGO_READ_DOT_ENV_FILE=True python manage.py shell_plus

.PHONY: migrations
migrations:
	DJANGO_READ_DOT_ENV_FILE=True python manage.py makemigrations

.PHONY: migrate
migrate:
	DJANGO_READ_DOT_ENV_FILE=True python manage.py migrate

.PHONY: run
run:
	DJANGO_READ_DOT_ENV_FILE=True python manage.py runserver_plus

.PHONY: workers
workers:
	DJANGO_READ_DOT_ENV_FILE=True celery -A config.celery_app worker --loglevel=info

.PHONY: beat
beat:
	DJANGO_READ_DOT_ENV_FILE=True celery -A config.celery_app beat --loglevel=info

.PHONY: graph
graph:
	DJANGO_READ_DOT_ENV_FILE=True python manage.py graph_models -a --pygraphviz --output models.png

.PHONY: docker
docker:
	docker-compose -f docker-compose.dev.yml down
	docker-compose -f docker-compose.dev.yml up -d

.PHONY: data
data:
	DJANGO_READ_DOT_ENV_FILE=True python manage.py migrate
