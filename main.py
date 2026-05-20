import random
import string

def create_password(size=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(size))
    return password

if __name__ == "__main__":
    print(create_password())
