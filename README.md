## PyOhio '22 Presentation

This repo demonstrates how "OpenAPI Driven Development". What I call using OpenAPI as a form of guardrail. My goal is to show how:

1. Generating OpenAPI from code can help avoid "doc drift". The uneasy case when the docs differ than what the backend does.
2. How including the OpenAPI schema inside can be a form of "checks and balances". Automated checks can verify that API changes are backward compatible.
3. Finally, we can cut down the toil with automated publishing of OpenAPI artifacts like pydantic models and typescript clients.

## Import Files

- `pyproject.toml` the version here is the version for the service and our OpenAPI schema. We choose [CalVer](https://calver.org/) but alternative schemes are doable. The intent is to mark changes to the API clearly.
- `bin/openapi` this is a simple bash script with `test`, `update`, and `packages` commands. The script is used by `Makefile` and `.gitlab-ci-yaml` as examples of how to setup a convenient experience for the developer. e.g. `bin/openapi update` updates your `openapi/schema.yaml` and `bin/openapi test compatibility` will check against `main` (the master branch of the repo) if there have been backward incompatible changes in your changes.
- `packages/books_pydantic/package.json` and `packages/typescript_client/package.json` both are examples of how a "package" can be added easily by ensuring you have a `package.json` with `update`, `setup`, and `publish` scripts. The `bin/openapi packages` hooks into these!
- `books` is an example (very contrite) FastAPI service.
