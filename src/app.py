"""Send a notification message to Microsoft Teams"""
import os
import pymsteams

# Set variables from env vars

teams_uri = os.environ.get("INPUT_TEAMS_URI")
teams_msg_title = os.environ.get("INPUT_TEAMS_MSG_TITLE")
teams_msg_summary = os.environ.get("INPUT_TEAMS_MSG_SUMMARY")
teams_msg_type = os.environ.get("INPUT_TEAMS_MSG_TYPE")
github_run_url = os.environ.get("INPUT_GITHUB_RUN_URL")

# Create the connector card

teams_msg = pymsteams.connectorcard(teams_uri)

# Set the content

teams_msg.title(teams_msg_title)

teams_msg.text(teams_msg_summary)

teams_msg.addLinkButton("View Run", github_run_url)

if teams_msg_type == "info":
    COLOR_HEX = "3A81B6"
elif teams_msg_type == "success":
    COLOR_HEX = "3AB660"
elif teams_msg_type == "failure":
    COLOR_HEX = "CC0000"
else:
    COLOR_HEX = "B63A50"

teams_msg.color(COLOR_HEX)

# Send the notification

teams_msg.send()
