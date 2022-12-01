from faker import Faker

from conn import session
from models import AddressBook

NUMBER_OF_RECORDS = 30

fake = Faker(['uk_UA'])


def create_record() -> None:
    for _ in range(NUMBER_OF_RECORDS):
        record = AddressBook(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            phone=fake.phone_number(),
            email=fake.email(),
            address=fake.address(),
            birthday=fake.date_between(start_date='-10y'),
            black_list=False
        )
        session.add(record)
    session.commit()


if __name__ == '__main__':
    create_record()