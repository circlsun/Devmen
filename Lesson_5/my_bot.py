import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
TG_TOKEN = os.environ['TG_TOKEN']
TG_CHAT_ID = os.environ['TG_CHAT_ID']
print(TG_TOKEN)