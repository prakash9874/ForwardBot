import os

class Config:
    API_ID = os.environ.get("API_ID", "22528446")
    API_HASH = os.environ.get("API_HASH", "0d81bf18019c5f3839037d0ae737c358")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7988382678:AAF28iuo2taxdZL5J8FJvVDJVjxpy7T-6Ew") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "forward-bot") 
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://vikassonawale0:JWyQFas7vlG1bkaL@cluster0.beermge.mongodb.net/?retryWrites=true&w=majority")
    DB_NAME = os.environ.get("DB_NAME", "Cluster0")
    OWNER_ID = [int(id) for id in os.environ.get("OWNER_ID", '633111330').split()]


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    







    
    
    
    
    
    # vikas Developer 
