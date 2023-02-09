import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "7414327"))
    API_HASH = os.environ.get("API_HASH", "a4502d77b8f99b722b8c167a7f5ac77c")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1970253860:AAG0alym1nvvy6bj-zk9Ekgemeb6rHKeT5I")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOJwBu7SI1eiOyd8nVQbmDbM3yknbX_EOouDw5rkuTWvQ-3zBid52SHMLkejDtUj1NwRftPtuiPosbRtFD74q3XE93boH9npKWa9vJvDWNqKFpA50HzjAEuPAx3rs44QeGs4bLRs0yHWDZW4ZIhXBpkPykHdf-MAFU9KBIlzHnizVJm0iqGVjg0eu-AXU5ELc-aawUPhchg8Os0ELTH2qsvcEJEpAkYXrMkuN4Mupp_8M45LvyNcExygiYYwqrjBmvirUpIZ01QW4meA5H-qaI8NKNhw3Z6vBGu0tsQJPGHePSmCURotdrI0hJO0y4XTca2ODnnp00Tub7OVJKAjNX5h0XXE=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "HYPERMEN_RBOT")
    SUPPORT = os.environ.get("SUPPORT", "Team_Bot_Support") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "Team_Bot_Update") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5714519888")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True"
