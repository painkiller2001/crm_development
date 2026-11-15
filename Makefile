lint:
	uv run ruff check .

start-server:
	uvicorn main:app --reload
