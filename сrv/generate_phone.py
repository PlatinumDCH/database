from faker import Faker
import phonenumbers
from phonenumbers import PhoneNumberType, PhoneNumberFormat, national_significant_number
from phone_gen import PhoneNumber
faker = Faker()


def generate_number():
    country_code = faker.country_code(representation='alpha-2').upper()

    sample_number_obj = phonenumbers.example_number_for_type(country_code, PhoneNumberType.MOBILE)
    national_number_length = len(national_significant_number(sample_number_obj))

    number_obj = phonenumbers.parse(str(Faker().random_number(national_number_length)), country_code)
    number = phonenumbers.format_number(number_obj, phonenumbers.PhoneNumberFormat.E164)
    return number


def generate_phone_number(country:str=''):
    if country:
        gen_phone = PhoneNumber(country)
        return gen_phone.get_number(full=True)
    return
