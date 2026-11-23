import random
import string


def generate_registration_data(cohort: int = 15):
    random_digits = random.randint(100, 999)
    email = f"anastasiya_stepanova_{cohort}_{random_digits}@yandex.ru"
    password = "".join(random.choices(string.ascii_letters + string.digits, k=8))
    return "Nastya", email, password
