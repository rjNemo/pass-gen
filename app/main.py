import random
import string


def generate_password(seed: int) -> str:
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits

    letters = lowercase + uppercase + digits

    random_generator = random.Random(seed)

    return "".join(random_generator.sample(letters, 8))
