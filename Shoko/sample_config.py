if __name__.endswith("sample_config"):
    import sys

    print(
        "The README is there to be read. Extend this sample config to a config file, don't just rename and change "
        "values here. Doing that WILL backfire on you.\nBot quitting.",
        file=sys.stderr,
    )
    quit(1)


# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    BOT_TOKEN = "1759657835:AAGWVkTUsdJnKLNicVgCh3WF4r1eNYIcumE"
    OWNER_ID = (
        "1490922001"  # If you dont know, run the bot and do /id in your private chat with it
    )
    OWNER_USERNAME = "Toxiczayn"
    TELETHON_HASH =  'acc81ae6fe9e6d7045f436f79adbc7b8' 
    TELETHON_ID = 1347630

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = ""  # needed for any database modules
    REDIS_URI = "redis-17978.c261.us-east-1-4.ec2.cloud.redislabs.com:17978"
    MESSAGE_DUMP = -100  # needed to make sure 'save from' messages persist
    GBAN_DUMP = -100
    ERROR_DUMP = -100
    LOAD = []
    NO_LOAD = []
    WEBHOOK = False
    URL = None

    # OPTIONAL
    SUDO_USERS = (
    )  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = (
    )  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = (
    )  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    WHITELIST_CHATS = []
    BLACKLIST_CHATS = []
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = True
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = None  
    ALLOW_EXCL = False  # DEPRECATED, USE BELOW INSTEAD! Allow ! commands as well as /
    CUSTOM_CMD = ('/', '!')   # Set to ('/', '!') or whatever to enable it, like ALLOW_EXCL but with more custom handler!
    API_OPENWEATHER = None  # OpenWeather API
    SPAMWATCH_API = '' # Your SpamWatch token
    
    
class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True


