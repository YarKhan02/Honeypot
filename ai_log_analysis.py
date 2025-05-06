import google.generativeai as genai
from dotenv import load_dotenv
import time
import os

import utils

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in the environment or .env file.")

# Initialize Gemini API
genai.configure(api_key=api_key)

def extract_information_from_logs(log_data):
    prompt = f"""
        You are a cybersecurity analyst. Analyze the following Linux audit log entries.

        1. Identify and summarize the sequence of events.
        2. Determine if there is any suspicious or malicious behavior (e.g., privilege escalation, command execution, access to sensitive files).
        3. Extract and explain any indicators of compromise (IOCs).
        4. Identify the attacker's intent if possible.
        5. Mention the commands executed and the programs involved.
        6. Determine if this activity matches known attack techniques (e.g., MITRE ATT&CK).

        Audit Log Entries:
        {log_data}
    """

    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    print(response.text)

def main():
    LOG_FILE = "log_file.txt"
    position = utils.read_last_position()

    while True:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            f.seek(position)
            new_data = f.read()
            position = f.tell()

            if new_data.strip():
                extract_information_from_logs(new_data)
                utils.write_current_position(position)

        time.sleep(2)
    
    extract_information_from_logs(log_data)

if __name__ == "__main__":
    main()