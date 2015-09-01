from abilities.wikipedia import Wikipedia
from abilities.flow import Flow
from abilities.jokes import Jokes
from abilities.general import General
from abilities.wolfram import Wolfram

TELEGRAM_TOKEN = ""

SLEEP_BETWEEN_REQUESTS = 1  # seconds
SLEEP_BETWEEN_UPDATES = 1  # seconds
SLEEP_BETWEEN_EXCEPTIONS = 600  # seconds


BOT_ADDRESS_SET = {'^j ', '^yo j ', '^jj ', '^jb ', }
abilities = (General, Wikipedia, Flow, Jokes, Wolfram)

