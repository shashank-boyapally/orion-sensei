# Orion-Bot: Automated Regression Detection
Orion-Bot is designed to automate the detection of performance regressions, eliminating the need for manual execution of Orion by a Jedi. Previously, this task was performed atleast once a day. To streamline the process, Orion, in collaboration with Cloud Sensei, automates this workflow and sends a daily report to the #orion-channel on Slack, reducing manual intervention.

## Hosted Environment
Currently, this service is hosted in the ocp-intlab and executes automatically every morning, ensuring up-to-date regression analysis for the Jedi.

## Prerequisites
To run the Orion-Bot locally, ensure the following dependencies are installed:

- **Podman**
- **Python**

## How to Run the Service
Once the prerequisites are met, you can run the service using the command below:

```
>> ./run-orion-bot.sh
```
### Environment Variables
Before running the bot, make sure the following environment variables are properly configured to ensure seamless automation:

- `SLACK_CHANNEL_ID`: The ID of the Slack channel where the message will be sent.

- `version`: The OCP version to run Orion on.

- `es_metadata_index`: The Elasticsearch index for metadata.

- `es_benchmark_index`: The Elasticsearch index for benchmark data.

- `ES_SERVER`: The URL of your Elasticsearch server.

- `SLACK_API_TOKEN`: The API token for accessing Slack's messaging services.

These environment variables ensure the bot has the necessary information to retrieve data and send notifications

