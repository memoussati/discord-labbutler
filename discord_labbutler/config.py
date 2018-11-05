"""LabBot configuration parameters."""
import os
import re

TOKEN = os.getenv('BOT_TOKEN')
PREFIX = './lb'
SPLIT = re.compile("\s+")
