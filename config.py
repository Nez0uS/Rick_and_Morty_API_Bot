from dotenv import load_dotenv
import os


class Config:
    def __init__(self):
        load_dotenv()
        self.TOKEN = os.getenv("TOKEN")
