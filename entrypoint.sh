#!/bin/bash


# Run the orion command with the configuration file
set +e
orion cmd --hunter-analyze --config /app/label-small-scale-cluster-density.yaml
EXIT_CODE=$?
set -e


# Check if orion command was successful
if [ $EXIT_CODE -eq 0 ] || [ $EXIT_CODE -eq 2 ] || [ $EXIT_CODE -eq 3 ]; then
    echo "Orion command completed successfully (or with allowed exit codes: 2 or 3). Sending Slack message..."
    # Run the Python script to send the Slack message
    python3 /usr/local/bin/send_slack.py --exit_code=$EXIT_CODE
else
    echo "Orion command failed with exit code $EXIT_CODE. Not sending Slack message."
    exit 1
fi