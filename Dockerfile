FROM quay.io/cloud-bulldozer/orion:latest

USER root
RUN apt-get update && \
    apt-get install -y python3 python3-pip

RUN pip3 install slack-sdk

COPY send_slack.py /usr/local/bin/send_slack.py
RUN chmod +x /usr/local/bin/send_slack.py

WORKDIR /app

COPY label-small-scale-cluster-density.yaml /app/label-small-scale-cluster-density.yaml
COPY entrypoint.sh /app/entrypoint.sh

ENV SLACK_CHANNEL_ID="PLACEHOLDER"
ENV SLACK_API_TOKEN='PLACEHOLDER'
ENV version='4.17'
ENV es_metadata_index='ospst-perf-scale-ci-*'
ENV es_benchmark_index='ospst-ripsaw-kube-burner*'
ENV ES_SERVER='placeholder'

CMD ./entrypoint.sh


