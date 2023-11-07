from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_session import Session

CORS_ORIGINS = "*"

cors = CORS(resources={r"/api/*": {"origins": CORS_ORIGINS}})
bcrypt = Bcrypt()
server_session = Session()
