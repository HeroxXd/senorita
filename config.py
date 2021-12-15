import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "senorita")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "Herox_xd")
ALIVE_NAME = getenv("ALIVE_NAME", "Senorita")
BOT_USERNAME = getenv("BOT_USERNAME", "Miss_senorita_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Miss_Senorita_Assistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Friendship_Foreverx")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Friendship_Foreverx")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/8ab017424864b8084fa32.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/HeroxXd/senorita")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/fefdc713e20ba0900da4f.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/065436368bb489cda5181.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/3a493d503c9fa1d5c22ab.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/85c29672b53cbc89c2a98.jpg")
