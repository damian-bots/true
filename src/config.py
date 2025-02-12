import os
import sys
from src.utils import resource_path
import logging

logger = logging.getLogger("Mafia Bot Config")

def read_tokens():
    try:
        with open(resource_path(os.path.join('data','token.txt')), 'r') as file:
            lines = [line.strip() for line in file.readlines()]
            if len(lines) < 3:
                logger.error("token.txt must contain at least three lines: Telegram token, Random.org API key, and Maintainer Telegram ID.")
                exit(1)
            TOKEN = "7470264967:AAHTssrBhJ2IyNOpzdCGMTlaANqf8B2Je-k"
            RANDOM_ORG_API_KEY = "478ea3fb-9b67-492e-ac72-961cf70b5650"
            MAINTAINER_ID = "6848223695"
            return TOKEN, RANDOM_ORG_API_KEY, MAINTAINER_ID
    except FileNotFoundError:
        logger.error("token.txt not found.")
        exit(1)

TOKEN, RANDOM_ORG_API_KEY, MAINTAINER_ID = read_tokens()
