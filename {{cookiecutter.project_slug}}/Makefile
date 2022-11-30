.PHONY: help
help:
	@echo "Welcome to {{cookiecutter.project_slug}}"
	@echo "======================================================="
	@echo ""
	@echo "Here are some of the most convenient commands:"
	@echo ""
	@echo "- init                Install the TailwindCSS CLI"
	@echo "- data                Applies migrations and creates default dev data"
	@echo "- dev                 Starts the development web server on localhost:8000 and compiles TailwindCSS"
	@echo "- check               Lints and fixes codebase"
	@echo "- migrate             Applies pending migrations"
	@echo "- test                Runs all tests, requires a database"
	@echo "- shell               Starts an interactive shell with all models imported"
	@echo "- migrations          Creates migrations based on models.py change"
	@echo "- webp                Compresses static images to webp (requires imagemagick)"
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
	python manage.py tailwind build
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
	python manage.py shell

.PHONY: migrations
migrations:
	python manage.py makemigrations

.PHONY: init
init:
	python manage.py tailwind installcli
	python manage.py tailwind init

.PHONY: migrate
migrate:
	python manage.py migrate

.PHONY: watch.css
watch.css:
	python manage.py tailwind watch

.PHONY: watch.server
watch.server:
	python manage.py runserver

.PHONY: dev
dev: ; ${MAKE} -j2 watch.css watch.server

.PHONY: graph
graph:
	python manage.py graph_models -a --pygraphviz --output models.png

.PHONY: data
data:
	python manage.py migrate

.PHONY: webp
webp:
	zsh -c 'mogrify -format webp performance90/static/images/**/*.(png|jpeg|jpg|svg)'
