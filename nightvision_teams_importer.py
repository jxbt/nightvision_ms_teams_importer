import json
import requests
import sys
import getopt
import re

# Microsoft Teams webhook URL.
webhook_url = ''

# Path of the SARIF file to parse.
sarif_file_path = ''

opts, args = getopt.getopt(sys.argv[1:], 'w:s:', ['webhook=', 'sarif='])
for opt, arg in opts:
    if opt in ('-w', '--webhook'):
        webhook_url = arg
    elif opt in ('-s', '--sarif'):
        sarif_file_path = arg

def send_message_to_teams(message):
    """Send a message to Microsoft Teams channel via webhook."""
    headers = {'Content-Type': 'application/json'}
    payload = {
        "@type": "MessageCard",
        "@context": "http://schema.org/extensions",
        "markdown": True,
        "text": message
    }
    response = requests.post(webhook_url, headers=headers, data=json.dumps(payload))
    if not response.ok:
        print(f"Failed to send message to Teams: {response.text}")

def generate_and_send_report():
    """Generate a report from SARIF and send it to Microsoft Teams."""

    i = 1
    with open(sarif_file_path, 'r') as file:
        sarif_data = json.load(file)
    for run in sarif_data.get('runs', []):
        for result in run.get('results', []):
            title = result['message']['text']
            severity = result["properties"]["nightvision-risk"]
            rule_id = result['ruleId']
            id = re.match(re.compile(r"[a-z0-9]+-[a-z0-9]+-[a-z0-9]+-[a-z0-9]+-[a-z0-9]+"),rule_id)[0]
            description = next((rule['fullDescription']['text'] for rule in run['tool']['driver']['rules'] if rule['id'] == rule_id), "No description available.")
            message = f"""
            
# {str(i)}. { title}:\n
{description}
            
            """
            print(message)
            i+=1

            send_message_to_teams(message)

if __name__ == "__main__":
    generate_and_send_report()
