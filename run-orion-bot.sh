#!/bin/bash

versions=("4.15" "4.16" "4.17" "4.18")

IMAGE="quay.io/rh-ee-sboyapal/orion-bot:latest"

TIMEOUT_DURATION="5m"

terminate_all_containers() {
    echo "Checking for running containers with image $IMAGE"

    # List all running containers with the specified image
    container_ids=$(podman ps -a -q --filter "ancestor=$IMAGE")

    # Terminate each running container
    if [ -n "$container_ids" ]; then
        echo "Terminating running containers with image $IMAGE"
        podman rm -f $container_ids
    else
        echo "No running containers found with image $IMAGE"
    fi
}

terminate_all_containers

for version in "${versions[@]}"; do
    echo "Running container for version $version"

    timeout $TIMEOUT_DURATION podman run -e SLACK_CHANNEL_ID="$SLACK_CHANNEL_ID" \
               -e version="$version" \
               -e es_metadata_index="$es_metadata_index" \
               -e es_benchmark_index="$es_benchmark_index" \
               -e ES_SERVER="$ES_SERVER" \
               -e SLACK_API_TOKEN="$SLACK_API_TOKEN" \
               --rm $IMAGE

    sleep 10
done