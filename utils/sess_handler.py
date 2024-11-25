import os
import time
import json
import logging
from filelock import FileLock
from utils.login_caller import LoginInit

SESSION_FILE = ".auth/session.json"
SESSION_DIR = os.path.dirname(SESSION_FILE)
SESSION_LOCK_FILE = f"{SESSION_FILE}.lock"


class SessionHandler:
    def __init__(self, browser, is_headless):
        self.browser = browser
        self.is_headless = is_headless

    def is_session_expired(self, session_file):
        if not os.path.exists(session_file):
            return True

        with open(session_file, "r") as file:
            session_data = json.load(file)

        current_time = time.time()
        for cookie in session_data.get("cookies", []):
            if cookie.get("expires", 0) <= current_time:
                return True

        return False

    def load_credentials(self, user_type):
        credentials = "data/credentials.json"
        if not os.path.exists(credentials):
            raise FileNotFoundError(f"Credentials file not found: {credentials}")

        with open(credentials, 'r') as file:
            credentials = json.load(file)

        for cred in credentials:
            if user_type in cred:
                return cred[user_type]["username"], cred[user_type]["password"]

        raise ValueError(f"User type '{user_type}' not found in credentials file")

    async def create_session(self, user_type: str):
        if not os.path.exists(SESSION_DIR):
            os.makedirs(SESSION_DIR)

        with FileLock(SESSION_LOCK_FILE):
            if not os.path.exists(SESSION_FILE) or self.is_session_expired(SESSION_FILE):
                context_options = {
                    "viewport": {"width": 1920, "height": 1080} if self.is_headless else None,
                    "no_viewport": not self.is_headless}

                context = await self.browser.new_context(**context_options)
                page = await context.new_page()

                if user_type:
                    email, password = self.load_credentials(user_type)
                    sess = LoginInit(page)
                    await sess.create_session(email, password)
                    logging.info(f"Login Success for {user_type}, Creating the session file . . .")
                    await context.storage_state(path=SESSION_FILE)
                    await context.close()

        return SESSION_FILE
