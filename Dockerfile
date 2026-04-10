# Use a standard Python environment
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy all your files into the container
COPY . /app

# Install the dependencies from your pyproject.toml
RUN pip install --no-cache-dir .

# Explicitly install fastapi and uvicorn for the dummy app
RUN pip install fastapi uvicorn

# Expose the port Hugging Face expects
EXPOSE 7860

# Start the dummy app to keep the Space green and Running
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
