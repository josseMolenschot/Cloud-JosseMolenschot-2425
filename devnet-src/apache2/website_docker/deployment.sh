#!/bin/bash

# Exit on any error
set -e

# Variables
PROJECT_DIR="$(pwd)"
PROJECT_NAME="apache2-webserver"
CONTAINER_NAME="apache2-server"
HOST_PORT=8070
CONTAINER_PORT=80
INDEX_HTML_PATH="${PROJECT_DIR}/index.html"

# Check if the index.html file exists
if [ ! -f "${INDEX_HTML_PATH}" ]; then
    echo "Error: index.html not found in ${PROJECT_DIR}!"
    exit 1
fi

# Build the Docker image
echo "Building Docker image..."
docker build -t ${PROJECT_NAME} ${PROJECT_DIR}

# Stop and remove any existing container with the same name
if [ "$(docker ps -aq -f name=${CONTAINER_NAME})" ]; then
    echo "Stopping and removing existing container..."
    docker stop ${CONTAINER_NAME} && docker rm ${CONTAINER_NAME}
fi

# Run the Docker container with the mounted volume
echo "Running Docker container..."
docker run -d -p ${HOST_PORT}:${CONTAINER_PORT} \
  -v ${INDEX_HTML_PATH}:/usr/local/apache2/htdocs/index.html \
  --name ${CONTAINER_NAME} ${PROJECT_NAME}

# Print success message
echo "Deployment successful! Access your web server at http://localhost:${HOST_PORT}"
