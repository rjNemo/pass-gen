import string
import random


def generate_password(seed: int, length: int = 8) -> str:
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits

    letters = lowercase + uppercase + digits

    random_generator = random.Random(seed)

    return "".join(random_generator.sample(letters, length))
