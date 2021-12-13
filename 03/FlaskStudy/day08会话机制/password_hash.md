`from werkzeug.security import generate_password_hash, check_password_hash`

# generate_password_hash()

generate_password_hash(password, method, salt_length)   

- password: 未加密字符串
- method="pbkdf2:sha256": 加密方法
- salt_length: 盐的长度
- return: 加密后的字符串

```python
# 密码格式 pbkdf2:sha256$salt$hash
user.password = generate_password_hash(password=password, method="pbkdf2:sha256", salt_length=8)
# return user.password # pbkdf2:sha256:260000$0mNOkiQR$f4d7d4bfcd2059faec0a0b4274470b73981b471e40f94adba841dcf6203fd7dd
```



# check_password_hash()

check_password_hash(pwhash, password)

- pwhash: 加密过的字符串

- password: 未加密的字符串
- return: True/False

```python
# user就是每一个用户对象
# 参数1: 经过加密的密码
# 参数2: 字符串
# return: True/False
res = check_password_hash(pwhash=user.password, password=password)
```

