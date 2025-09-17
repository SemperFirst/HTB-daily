import requests

USERNAME = "normal"
PASSWORD = "normal"
ARCHIVE_PATH = "payload.tar"
BASE_URL = "REDACTED"

def main():
    session = requests.Session()
    create_account(session)
    assert(login(session))
    assert(upload(session))
