POETRY := poetry

.PHONY: install
install: $(BACKEND_INSTALL_FLAG) ## Install project requirements

$(BACKEND_INSTALL_FLAG): backend/poetry.lock
	$(POETRY) install
	@ touch $@

backend/poetry.lock: backend/pyproject.toml
	$(POETRY) lock --no-update
	@ touch $@

.PHONY: runserver
runserver: install  ## Run server
	$(POETRY) run uvicorn books.app:app --reload

.PHONY: openapi
openapi: ## Update schema and packages
	@ npx nodemon --watch books -e py --exec "bin/openapi update & bin/openapi packages update"

.PHONY: help
help:
	@ grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
