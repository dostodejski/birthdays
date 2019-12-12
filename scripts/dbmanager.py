import hashlib
import random
password = "the password typed by the user"
salt=str(random.random())
digest = salt + password
for i in range (1000000):
  digest = hashlib.sha256(digest.encode(’utf-8’)).hexdigest()
print(digest)
