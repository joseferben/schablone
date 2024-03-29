.PHONY: help
help:
	@echo "Welcome"
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
	@echo "- sync                Downloads DB and media files from production" (requires litestream)
	@echo "- webp                Compresses static images to webp (requires imagemagick)"
	@echo "- stripe              Forward webhook events to local endpoint"
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
	python manage.py shell_plus

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

.PHONY: watch.css
watch.css:
	python manage.py tailwind watch

.PHONY: dev
dev: migrate
	$(MAKE) -j 2 watch.css watch.server

.PHONY: webp
webp:
	zsh -c 'mogrify -format webp project/static/images/**/*.(png|jpeg|jpg|svg)'

.PHONY: sync
sync:
	./manage.py sync_data
	./manage.py sync_local_site

.PHONE: stripe
stripe:
	stripe listen --forward-to localhost:8000/stripe/webhook/
