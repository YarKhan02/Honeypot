import requests
import time
import os

AUDIT_LOG_PATH = "/var/log/audit/audit.log"
STATE_FILE = "/var/log/audit/last_audit_pos"
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/your_webhook_url"

def read_last_position():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            return int(f.read().strip())
    return 0

def write_last_position(pos):
    with open(STATE_FILE, "w") as f:
        f.write(str(pos))

def send_to_discord(message):
    data = {
        "content": message
    }
    response = requests.post(DISCORD_WEBHOOK_URL, json=data)
    return response.status_code == 204 or response.status_code == 200

def process_new_logs():
    last_pos = read_last_position()
    with open(AUDIT_LOG_PATH, "r") as f:
        f.seek(last_pos)
        lines = f.readlines()
        current_pos = f.tell()
        write_last_position(current_pos)

    if not lines:
        return

    # Discord has a 2000 character message limit
    chunk = ""
    for line in lines:
        if len(chunk) + len(line) >= 1900:
            send_to_discord(f"```{chunk}```")
            chunk = ""
        chunk += line

    if chunk:
        send_to_discord(f"```{chunk}```")

if __name__ == "__main__":
    process_new_logs()
