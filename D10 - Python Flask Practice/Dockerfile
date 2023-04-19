# syntax=docker/dockerfile:1

# The image inherites from 'python' image
FROM python:latest

WORKDIR /app

# host: your PC, laptop, cloud server...
# Copy from host to container
COPY requirements.txt requirements.txt

# Run this command in the container
RUN pip install -r requirements.txt

COPY . .

#Run command in container
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]