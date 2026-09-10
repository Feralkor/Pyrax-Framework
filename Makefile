install:
	python -m pip install -e ".[dev]"

lint:
	python -m ruff check src tests

test:
	python -m pytest -q

validate-example:
	pyrax validate tests/fixtures/minimal-domain-pack.yaml

assess-example:
	pyrax assess tests/fixtures/minimal-domain-pack.yaml

quality: lint test validate-example assess-example
