.PHONY: build start stop restart logs shell migrate makemigrations createsuperuser test clean help

# Variables
CONTAINER_NAME = casebuddy
DOCKER_COMPOSE = docker-compose

help:
	@echo "Available commands:"
	@echo "build         - Build Docker images"
	@echo "start         - Start Docker containers"
	@echo "stop          - Stop Docker containers"
	@echo "restart       - Restart Docker containers"
	@echo "logs          - View Docker container logs"
	@echo "shell         - Open Django shell in container"
	@echo "migrate       - Run Django migrations"
	@echo "makemigrations- Create new Django migrations"
	@echo "createsuperuser- Create Django superuser"
	@echo "test          - Run Django tests"
	@echo "clean         - Remove Docker containers and volumes"
	@echo "collectstatic - Collect static files"

build:
	$(DOCKER_COMPOSE) build

up:
	$(DOCKER_COMPOSE) up -d

stop:
	$(DOCKER_COMPOSE) down

restart: stop start

logs:
	$(DOCKER_COMPOSE) logs -f

shell:
	$(DOCKER_COMPOSE) exec web python manage.py shell

migrate:
	$(DOCKER_COMPOSE) exec web python manage.py migrate

makemigrations:
	$(DOCKER_COMPOSE) exec web python manage.py makemigrations

createsuperuser:
	$(DOCKER_COMPOSE) exec web python manage.py createsuperuser

test:
	$(DOCKER_COMPOSE) exec web python manage.py test

clean:
	$(DOCKER_COMPOSE) down -v
	rm -rf data/db/*
	rm -rf data/logs/*
	rm -rf static/*
	rm -rf media/*

collectstatic:
	$(DOCKER_COMPOSE) exec web python manage.py collectstatic --noinput

status:
	$(DOCKER_COMPOSE) ps

# Development commands
dev-build:
	$(DOCKER_COMPOSE) -f docker-compose.dev.yml build

dev-start:
	$(DOCKER_COMPOSE) -f docker-compose.dev.yml up

dev-stop:
	$(DOCKER_COMPOSE) -f docker-compose.dev.yml down

# Database backup and restore
backup:
	@echo "Creating database backup..."
	@mkdir -p backups
	$(DOCKER_COMPOSE) exec web python manage.py dumpdata --indent 2 > backups/backup_$$(date +%Y%m%d_%H%M%S).json

restore:
	@if [ -z "$(FILE)" ]; then \
		echo "Please specify the backup file with FILE=backups/your_backup.json"; \
		exit 1; \
	fi
	$(DOCKER_COMPOSE) exec web python manage.py loaddata $(FILE) 