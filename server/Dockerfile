# 1. Use a lightweight Python 3.14 base image
FROM astral-sh/uv:python3.14-bookworm-slim AS builder

# 2. Set the working directory
WORKDIR /app

# 3. Enable bytecode compilation for faster startup
ENV UV_COMPILE_BYTECODE=1

# 4. Copy only dependency files first (to leverage Docker caching)
COPY pyproject.toml uv.lock ./

# 5. Install dependencies without the project itself
RUN uv sync --frozen --no-install-project --no-dev

# 6. Copy the rest of your application code
COPY . .

# 7. Install the project
RUN uv sync --frozen --no-dev

# 8. Final Stage: Runtime
FROM python:3.14-slim-bookworm

WORKDIR /app

# Copy the virtual environment from the builder
COPY --from=builder /app/.venv /app/.venv

# Ensure the virtual environment is used
ENV PATH="/app/.venv/bin:$PATH"

# Copy the application code
COPY . .

# 9. Expose the API port defined in your openenv.yaml
EXPOSE 8000

# 10. Start the FastAPI server using Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]