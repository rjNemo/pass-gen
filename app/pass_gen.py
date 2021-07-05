import string
import random


def generate_password(seed: int, length: int = 8, symbols: bool = False) -> str:
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation

    letters = lowercase + uppercase + digits
    if symbols:
        letters += punctuation

    random_generator = random.Random(seed)

    return "".join(random_generator.sample(letters, length))
