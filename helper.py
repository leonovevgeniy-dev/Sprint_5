from faker import Faker
import random
import string

faker = Faker()

def generate_registration_data():

    email = faker.email()
    password_length = random.randint(6, 20)
    password = faker.password(length=password_length)
    return email, password


def generate_incorrect_password():
  
    password_length = random.randint(1, 5)
    # Простые цифры - всегда работают
    return ''.join(random.choice(string.digits) for _ in range(password_length))