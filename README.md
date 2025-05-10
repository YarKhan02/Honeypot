# Honeypot Log Analysis and Discord Integration

This project provides a streamlined solution for monitoring Linux audit logs, sending them to a Discord channel, and performing AI-based log analysis for cybersecurity insights. It combines real-time log monitoring, Discord bot integration, and AI-powered analysis to detect and analyze suspicious activities effectively.

---

## Features

### 1. **Real-Time Log Monitoring**
- Reads Linux audit logs (`/var/log/audit/audit.log`) and tracks the last processed position to avoid duplicate processing.

### 2. **Discord Integration**
- Sends log entries to a specified Discord channel using a bot.
- Handles Discord's message size limits by chunking large log entries.

### 3. **AI-Powered Log Analysis**
- Uses the Gemini AI API to analyze logs for:
  - Suspicious behavior and Indicators of Compromise (IOCs).
  - Attack techniques and attacker intent.
  - Executed commands and potential vulnerabilities.

### 4. **Systemd Timer for Automation**
- Automates periodic execution of the log monitoring script using a systemd timer.

---

## Setup Instructions

### Prerequisites
1. **Python 3.8+** installed on your system.
2. **Discord Bot**:
   - Create a bot in the [Discord Developer Portal](https://discord.com/developers/applications).
   - Copy the bot token and invite the bot to your server.
3. **Gemini AI API Key**:
   - Obtain an API key from Gemini AI.
   - Add it to the `.env` file as `GEMINI_API_KEY`.

### Steps to Set Up

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Honeypot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure environment variables:
   - Create a `.env` file:
     ```
     GEMINI_API_KEY=your_gemini_api_key
     DISCORD_BOT_TOKEN=your_discord_bot_token
     DISCORD_CHANNEL_ID=your_channel_id
     ```

4. Set up the Discord bot:
   - Follow these steps:
     - Go to [Discord Developer Portal](https://discord.com/developers/applications).
     - Create a new application and add a bot.
     - Copy the bot token and invite the bot to your server using the OAuth2 URL Generator.
     - Enable Developer Mode in Discord to copy the channel ID.

5. Configure systemd service and timer:
   - Copy `audit_to_discord.py` to `/usr/local/bin/` and make it executable:
     ```bash
     sudo chmod +x /usr/local/bin/audit_to_discord.py
     ```
   - Create and enable the systemd service and timer:
     ```bash
     sudo nano /etc/systemd/system/audit-discord.service
     sudo systemctl daemon-reload
     sudo systemctl enable --now audit-discord.timer
     ```

---

## Usage

### 1. **Run the Discord Bot**
Start the bot to monitor a specific Discord channel:
```bash
python main.py
```

### 2. **Send Audit Logs to Discord**
The `audit_to_discord.py` script reads new entries from `/var/log/audit/audit.log` and sends them to Discord. This script is automated using the systemd timer.

### 3. **Analyze Logs with AI**
Run the AI log analysis script to extract cybersecurity insights:
```bash
python ai_log_analysis.py
```

---

## Security Considerations

- **Environment Variables**:
  - Sensitive information like API keys and bot tokens are stored in the `.env` file and excluded from version control using `.gitignore`.
- **Discord Bot Permissions**:
  - The bot requires minimal permissions (`Read Message History` and `Read Messages/View Channels`) to function.

---

## Future Enhancements

- Add support for additional log formats.
- Implement advanced AI models for deeper log analysis.
- Integrate with other communication platforms (e.g., Slack, Teams).

---

## Acknowledgments

- [Discord API](https://discord.com/developers/docs/intro)
- [Gemini AI](https://gemini.ai/)
- Linux Audit Framework

Feel free to contribute to this project by submitting issues or pull requests!
