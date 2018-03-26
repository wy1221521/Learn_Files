
import hashlib

pwd=hashlib.sha256()
pwd.update('WZwz123456'.encode('UTF-8'))

print(pwd.hexdigest())