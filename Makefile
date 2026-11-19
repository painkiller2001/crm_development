lint:
	uv run ruff check .

start-server:
	uvicorn main:app --reload
	
test:
	pytest tests

venv:
	source .venv/bin/activate
