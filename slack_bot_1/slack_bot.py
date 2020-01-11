#import flask
import os
import time
import re
from slack import WebClient

slack_client = WebClient("xoxb-902513358661-902503861696-6d8YdqtzYjzSjUKPm6s92hZW")
if __name__ == "__main__":
    if slack_client.rtm_connect():
        print("started")
    else:
        print("not connected")
