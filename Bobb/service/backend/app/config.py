from dotenv import load_dotenv
from app.utils import get_uuid

load_dotenv()


class ApplicationConfig:
    SECRET_KEY = get_uuid()
    SESSION_TYPE = 'filesystem'
