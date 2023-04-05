.PHONY: help
help:
	@echo "Welcome to {{cookiecutter.project_slug}}"
	@echo "======================================================="
	@echo ""
	@echo "Here are some of the most convenient commands:"
	@echo ""
	@echo "- dev                 Starts the development web server on localhost:8000"
	@echo "- check               Lints and fixes codebase"
	@echo "- work                Run huey worker process"
	@echo "- migrate             Applies pending migrations"
	@echo "- test                Runs all tests"
	@echo "- shell               Starts an interactive shell with all models imported"
	@echo "- migrations          Creates migrations based on models.py change"
	@echo "- webp                Compresses static images to webp (requires imagemagick)"
	@echo ""
	@echo "Here are some of less used commands:"
	@echo ""
	@echo "- coverage            Runs tests and prints coverage in terminal"
	@echo "- check.lint          Runs linter"
	@echo "- check.types         Runs type checker"
	@echo "- watch.server        Runs web server on localhost:8000"

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
	python manage.py shell

.PHONY: migrations
migrations:
	python manage.py makemigrations

.PHONY: migrate
migrate:
	python manage.py migrate

.PHONY: watch.server
watch.server:
	python manage.py runserver

.PHONY: work
work:
	python manage.py run_huey

.PHONY: dev
dev: ; ${MAKE} -j2 migrate watch.server

.PHONY: webp
webp:
	zsh -c 'mogrify -format webp {{cookiecutter.project_slug}}/static/images/**/*.(png|jpeg|jpg|svg)'
