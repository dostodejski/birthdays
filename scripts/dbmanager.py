import hashlib
import random
CREATE TABLE user (username CHAR(256), password CHAR(256));
CREATE TABLE profile (username CHAR(256), role CHAR(256));
INSERT INTO user VALUES("Alan", "123");
INSERT INTO profile VALUES("Alan", "admin");
INSERT INTO user VALUES("Albert", "1234");
INSERT INTO profile VALUES("Albert", "user");
password = "the password typed by the user"
salt=str(random.random())
digest = salt + password
for i in range (1000000):
  digest = hashlib.sha256(digest.encode(’utf-8’)).hexdigest()
print(digest)
