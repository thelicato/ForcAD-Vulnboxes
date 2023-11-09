from dotenv import load_dotenv
import os

load_dotenv()


class ApplicationConfig:
    SECRET_KEY = os.environ["FLASK_SECRET_KEY"]
    SESSION_TYPE = 'filesystem'
