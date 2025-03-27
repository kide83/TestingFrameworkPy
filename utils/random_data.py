import random
import string

def random_string(length=8):
    return ''.join(random.choices(string.ascii_letters, k=length))

def random_email():
    return f"{random_string()}@testmail.com"

def random_password():
    return random_string(12)
