#!/bin/bash

# Define variables
IMAGE_NAME="josse-nginx-image"
CONTAINER_NAME="josse-nginx-container"
HOST_PORT=8080
CONTAINER_PORT=80

# Ensure the script is executed from the project directory
PROJECT_DIR=$(dirname "$0")
cd "$PROJECT_DIR" || exit

# Check if Docker is installed
if ! command -v docker &>/dev/null; then
    echo "Docker is not installed. Please install Docker and try again."
    exit 1
fi

# Build the Docker image
echo "Building the Docker image..."
docker build -t $IMAGE_NAME .

# Check if a container with the same name is running, and stop it
if docker ps -q -f name=$CONTAINER_NAME; then
    echo "Stopping the existing container..."
    docker stop $CONTAINER_NAME
    echo "Removing the existing container..."
    docker rm $CONTAINER_NAME
fi

# Run the Docker container
echo "Starting the Docker container..."
docker run -d --name $CONTAINER_NAME -v $(pwd)/templates/index.html:/usr/share/nginx/html/index.html -p $HOST_PORT:$CONTAINER_PORT $IMAGE_NAME

# Verify deployment
if docker ps -q -f name=$CONTAINER_NAME; then
    echo "Container deployed successfully! Access the site at http://localhost:$HOST_PORT"
else
    echo "Failed to start the container. Check the Docker logs for more information."
fi
