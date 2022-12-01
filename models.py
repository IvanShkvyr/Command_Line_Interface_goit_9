from sqlalchemy import Column, Integer, String, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property


Base = declarative_base()


class AddressBook(Base):
    __tablename__ = "addressbook"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(120), nullable=False)
    last_name = Column(String(120), default="-")
    phone = Column(String(25), nullable=False)
    email = Column(String(50), default="-")
    address = Column(String(200), default="-")
    birthday = Column(Date)
    black_list = Column(Boolean, default=False)

    @hybrid_property
    def fullname(self):
        last_name_ = self.last_name
        if self.last_name == '-':
            last_name_ = ''

        return self.first_name + ' ' + last_name_


# alembic init alembic
# sqlalchemy.url = sqlite:///addressbook.db
# from models import Base
# target_metadata = Base.metadata

# alembic revision --autogenerate -m 'last_name_'
# alembic upgrade head

