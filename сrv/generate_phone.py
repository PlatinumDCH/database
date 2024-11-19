from faker import Faker
from phone_gen import PhoneNumber

faker = Faker()

def generate_phone_number(country:str=''):
    if country:
        gen_phone = PhoneNumber(country)
        return gen_phone.get_number(full=True)
    return
