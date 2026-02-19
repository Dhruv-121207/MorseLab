import os
import secrets

class Config:

    SECRET_KEY = os.environ.get("SECRET_KEY")

    if not SECRET_KEY:
        SECRET_KEY = secrets.token_hex(32)
