import hashlib
import random, string

def hash(password):
    return hashlib.sha512(password.encode()).hexdigest()

def auth_string(n = 6):
   return ''.join(random.choices(string.ascii_letters + string.digits, k=n))

if __name__=="__main__":
    text = "test"
    hashed = hash(text)
    print(hashed)
    a = input()
    if hash(a) == hashed:
        print("ok")