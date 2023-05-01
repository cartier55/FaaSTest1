import os
from slack_sdk import WebClient
# from refParts import mainParts4 as mp4
# from refParts import mainParts3 as mp3
# from refParts import mainParts2 as mp2

client = WebClient(token=os.getenv("APP_OAUTH"))


def update_slack(channel, msg):
    client.chat_postMessage(channel=channel, text=msg)


def main(args):
    if args.get('command') == '/read':
        text = 'test read'
        update_slack('#random', str(text))
        return {"statusCode": 200, "body": 'read'}
