from dotenv import load_dotenv
import os
from app.utils import get_uuid

load_dotenv()


class ApplicationConfig:
    SECRET_KEY = get_uuid()
    SESSION_TYPE = 'filesystem'
