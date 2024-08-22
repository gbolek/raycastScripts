
#!/Users/gbolek/.pyenv/shims/python python

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title post-url-to-endpoint
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 🤖

# old shebang /Users/gbolek/.pyenv/versions/raycastenv/bin/pythons python

import requests
import json
import os
import sys
import subprocess

# Function to get the copied URL from the clipboard
def get_copied_url():
    try:
        result = subprocess.run(['pbpaste'], stdout=subprocess.PIPE)
        return result.stdout.decode('utf-8').strip()
    except Exception as e:
        print(f"Error getting copied URL: {e}")
        sys.exit(1)

# Function to read the configuration file
def read_config():
    config_path = os.path.expanduser('../config/config.json')
    if not os.path.exists(config_path):
        print(f"Configuration file not found at {config_path}")
        sys.exit(1)
    
    with open(config_path, 'r') as config_file:
        config = json.load(config_file)
    
    return config

# Function to send the URL to the specified endpoint
def send_url(url, endpoint):
    try:
        response = requests.post(endpoint, json={"url": url})
        response.raise_for_status()
        print(f"Successfully sent URL to {endpoint}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending URL: {e}")
        sys.exit(1)

def main():
    # Get the copied URL
    url = get_copied_url()
    if not url:
        print("No URL found in the clipboard.")
        sys.exit(1)
    
    # Read the configuration
    config = read_config()
    endpoint = config.get("endpoint_url")

    if not endpoint:
        print("Endpoint URL is not defined in the configuration.")
        sys.exit(1)

    # Send the URL to the endpoint
    send_url(url, endpoint)

if __name__ == "__main__":
    main()
