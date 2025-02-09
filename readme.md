# backend_my_slot

A Django-based backend for managing slots, reservations, and availability.

This backend is for a Meeting Scheduler App
This web application allows users to publish their availability and let others book meetings with them seamlessly. It provides an intuitive interface for managing availabilities and reservations while ensuring secure email verification for reservation deletions.

The fronted code for this project is available in a separate repository. You can find it here:

[Frontend Repository](https://github.com/Abdarrahmane-NEINE/my_slot.git): https://github.com/Abdarrahmane-NEINE/my_slot.git

[Frontend Demo](https://slot.abdarrahmane.link): https://slot.abdarrahmane.link


---

## Features

- Manage **Availabilities** with start and end times.
- Create and manage **Reservations** with email and time slots.
- Simple REST API with Django REST Framework (DRF).

---

## Requirements

- Python 3.8+
- Django 4.0+
- Django REST Framework (DRF)
- pytest (for testing)
- SQLite 

---

## Installation

### 1. Clone the Repository:
```bash
git clone https://github.com/Abdarrahmane-NEINE/backend_my_slot.git
cd backend_my_slot
```


### 2. Install Dependencies:
```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables:
Create a `.env` file in the root directory and add:
```
SECRET_KEY=your_django_app_secret_key
ALLOWED_HOSTS=allower_host_url
# trusted origins for CSRF (comma-separated values)
CSRF_TRUSTED_ORIGINS=
```

### 4. Apply Migrations:
```bash
python manage.py migrate
```

### 5. Run the Development Server:
```bash
python manage.py runserver
```
Access the app at [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

# Docker Setup

This project includes a Docker configuration to simplify development and deployment.

## Dockerfile

The Dockerfile builds an image using Python 3.10, installs your dependencies, collects static files, and runs the Django development server:

```dockerfile
# Use an official Python image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project code
COPY . /app

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port 8000 for Django
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

## Docker Compose

The `docker-compose.yml` file defines the service configuration, including volume mounts and environment variables:

```yaml
version: "3.8"

services:
  web:
    build:
      context: .              # Use the current folder for Docker context
      dockerfile: Dockerfile  # Dockerfile is in the same folder
    ports:
      - "8000:8000"           # Map port 8000
    volumes:
      - .:/app                # Mount the entire project folder
      - ./staticfiles:/app/staticfiles # Map static files to host
      - ./db:/app/db          # Mount the SQLite database folder
    env_file:                 # Load environment variables from .env
      - .env

volumes:
  static_volume: # Define the volume for static files
```

---

## CI/CD with GitHub Actions

A GitHub Actions workflow is set up to build and deploy the application to an EC2 instance using Docker Hub.

### Deployment Workflow

```yaml
name: Build and Deploy to EC2 with Docker Hub

on:
  push:
    branches: [ main ]  # Trigger the workflow on pushes to the main branch

jobs:
  build-deploy:
    runs-on: ubuntu-latest

    steps:
      # Check out the repository code
      - name: Checkout Repository
        uses: actions/checkout@v3

      # Log in to Docker Hub using credentials stored in GitHub Secrets
      - name: Log in to Docker Hub
        uses: docker/login-action@v2
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}

      # Build the Docker image and push it to Docker Hub
      - name: Build and Push Docker Image
        uses: docker/build-push-action@v4
        with:
          context: .
          push: true
          tags: abdarrahmane/slot_calendar:latest

      # Deploy the updated image to your EC2 instance via SSH
      - name: Deploy on EC2
        uses: appleboy/ssh-action@v0.1.8
        with:
          host: ${{ secrets.EC2_HOST }}       # EC2 public IP or domain
          username: ${{ secrets.EC2_USER }}     # SSH username
          key: ${{ secrets.EC2_SSH_KEY }}       # private SSH key
          script: |
            # Pull the latest image from Docker Hub
            docker pull abdarrahmane/slot_calendar:latest
            
            # Directory of docker-compose.yml
            cd /var/www/python_project/backend_my_slot
            
            # Bring down the currently running containers
            docker-compose down
            
            # Start up containers using the updated image
            docker-compose up -d
```

----

## Running Tests

### 1. Run Unit Tests:
```bash
pytest
```

### 2. Run Specific Tests:
```bash
pytest api_my_slot/tests/test_models.py
```

### 3. Generate Test Coverage:
#### Install pytest-cov:
```bash
pip install pytest-cov
```

#### Run with coverage:
```bash
pytest --cov=api_my_slot
```

