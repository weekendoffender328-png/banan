.PHONY: install VD-games build package-install clean reinstall lint

install:
	uv sync

VD-games:
	uv run vd-main

build:
	uv build

package-install:
	uv tool install --force dist/games_project_pisyapopa-*.whl

reinstall: build
	  uv tool install --force dist/games_project_pisyapopa-$(shell grep -oP 'version = "\K[^"]+' pyproject.toml)-*.whl

clean:
	rm -rf dist/ build/ *.egg-info/

lint:
	uv run ruff check games_project_pisyapopa/
	uv run ruff format --check games_project_pisyapopa/

lint-fix:
	uv run ruff check --fix games_project_pisyapopa/
	uv run ruff format games_project_pisyapopa/
