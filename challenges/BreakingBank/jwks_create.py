from flask import Flask, jsonify
from jwt.utils import base64url_encode
from Crypto.PublicKey import RSA
app = Flask(__name__)
# Generate RSA Key Pair
key_pair = RSA.generate(2048)
pub_key = key_pair.publickey()
priv_key = key_pair.export_key('PEM')
# Prepare JWKS data
jwks_data = {
'keys': [{
'alg': 'RS256',
'kty': 'RSA',
'use': 'sig',
'n': base64url_encode(int.to_bytes(pub_key.n, (pub_key.n.bit_length() + 7) // 8,
'big')).decode(),
'e': base64url_encode(int.to_bytes(pub_key.e, (pub_key.e.bit_length() + 7) // 8,
'big')).decode(),
'kid': '6a7fbf00-d514-46ff-a6b6-65684a775284' }]
}
print(priv_key)
@app.route('/.well-known/jwks.json', methods=['GET'])
def serve_jwks():
    return jsonify(jwks_data), 200
if __name__ == '__main__':
    app.run(port=9000)
