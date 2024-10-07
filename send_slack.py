import glob
from slack_sdk import WebClient
import os
import argparse

def send_slack_output_file(exit_code:int):
    output_file_pattern = (
        "output*" 
    )
    output_files = glob.glob(output_file_pattern)
    if not output_files:
        return {"statusCode": 500, "body": "Error: No output file found."}
    
    output_file_path = output_files[0]
    
    client = WebClient(os.environ["SLACK_API_TOKEN"])
    
    res = client.files_upload_v2(
        channel=os.environ.get("SLACK_CHANNEL_ID"),
        title=f"Orion Output for payload job {os.environ.get('version')}",
        file=output_file_path,
        initial_comment=(':warning: Regression found' if exit_code==2 else  ":success: No Regression") + f"Orion Regression analysis for version {os.environ.get('version')}: ",
    )
    return res

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send Orion output to Slack")
    parser.add_argument("--exit_code", type=int, required=True, help="Exit code from Orion command")
    args = parser.parse_args()
    result = send_slack_output_file(args.exit_code)
    print(result)