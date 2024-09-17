import glob
from slack_operations import SlackOperations
import subprocess

def create_blocks_from_file_content(file_content, lines_per_block=1):
    # Split the file content into lines
    lines = file_content.splitlines()
    
    # Split lines into chunks of the specified size
    chunks = [lines[i:i + lines_per_block] for i in range(0, len(lines), lines_per_block)]
    
    # Create a list of blocks
    blocks = []
    for chunk in chunks:
        block_content = "\n".join(chunk)
        block = {
            "type": "rich_text",
            "elements": [
                {
                    "type": "rich_text_preformatted",
                    "elements": [
                        {"type": "text", "text": block_content},
                    ],
                    "border": 0,
                }
            ],
        }
        blocks.append(block)
    
    return blocks

def lambda_handler(event, context):
    config_file_path = "lambda-cli-package/orion/examples/label-small-scale-cluster-density.yaml"

    cli_command = f"orion cmd --hunter-analyze --config {config_file_path}"

    
    result = subprocess.run(
        cli_command, shell=True, check=False, capture_output=True, text=True
    )
   
    output_file_pattern = (
        "output*" 
    )
    output_files = glob.glob(output_file_pattern)
    if not output_files:
        return {"statusCode": 500, "body": "Error: No output file found."}

    output_file_path = output_files[0]
    with open(output_file_path, "r") as file:
        file_content = file.read()
    # file_content = file_content[:30]
    blocks = create_blocks_from_file_content(file_content=file_content)
    so = SlackOperations()
    res=so.post_message(blocks=blocks)
    print(res)
    return {
        "statusCode": 200,
        "body": file_content, 
    }

    # except subprocess.CalledProcessError as e:
    #     return {"statusCode": 500, "body": f"Error running command: {e.stderr}"}
    # except Exception as e:
    #     return {"statusCode": 500, "body": f"Unexpected error: {str(e)}"}

lambda_handler("hi","hi")

