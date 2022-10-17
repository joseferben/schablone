.PHONY: help
help:
	@echo "Welcome to {{cookiecutter.project_slug}}"
	@echo "======================================================="
	@echo ""
	@echo "Here are some of the most convenient commands:"
	@echo ""
	@echo "- docker              Starts environment with Postgres and Redis using docker-compose, destroys current environment"
	@echo "- data                Runs migrations, creates default user, groups and data"
	@echo "- check               Runs linter and type checker and fixes found issues"
	@echo "- fix                 Fixes issues like formatting and imports"
	@echo "- migrate             Runs migrations"
	@echo "- env                 Starts environment and seeds examples data, destroys current environment!"
	@echo "- test                Runs all tests, requires a database"
	@echo "- shell               Starts an interactive shell with all models imported"
	@echo "- workers             Starts a cluster of worker processes"
	@echo "- beat								 Starts a beat process for scheduled tasks"
	@echo "- run                 Starts the development web server on localhost:8000 and compiles TailwindCSS"
	@echo "- migrations          Creates migrations based on models.py change"
	@echo ""
	@echo "Here are some of less used commands:"
	@echo ""
	@echo "- graph               Renders a graph with all models in graph.png"
	@echo "- coverage            Runs tests and prints coverage in terminal"
	@echo "- check.lint          Runs linter"
	@echo "- check.types         Runs type checker"
	@echo "- watch.server        Runs web server on localhost:8000"
	@echo "- watch.css           Runs the TailwindCSS compiler"

.PHONY: check
check:
	pre-commit run --show-diff-on-failure -a

.PHONY: test
test:
	pytest

.PHONY: coverage
coverage:
	coverage run -m pytest
	coverage report

.PHONY: shell
shell:
	IPYTHONDIR=.ipython python manage.py shell_plus

.PHONY: migrations
migrations:
	python manage.py makemigrations

.PHONY: migrate
migrate:
	python manage.py migrate

.PHONY: watch.css
watch.css:
	tailwindcss --watch -i {{cookiecutter.project_slug}}/static/css/project.css -o {{cookiecutter.project_slug}}/static/css/dist/styles.css

.PHONY: watch.server
watch.server:
	python manage.py runserver

.PHONY: run
run: ; ${MAKE} -j2 watch.css watch.server

.PHONY: workers
workers:
	celery -A config.celery_app worker --loglevel=info

.PHONY: beat
beat:
	celery -A config.celery_app beat --loglevel=info

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
