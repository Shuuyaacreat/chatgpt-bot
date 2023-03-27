from os import getenv
from dotenv import load_dotenv

load_dotenv("config.env")

API_ID = int(getenv("API_ID", "24427150"))
API_HASH = getenv("API_HASH", "9fcc60263a946ef550d11406667404fa")
BOT_TOKEN = getenv("BOT_TOKEN", "6248261161:AAGJPvJzwXgk5xRf9PqXqrU73zu-SZOuXng")
OPENAI_API = getenv("OPENAI_API", "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") # get api key : https://platform.openai.com/account/api-keys
