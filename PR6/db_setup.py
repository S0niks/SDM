from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base, sessionmaker, backref

Base = declarative_base()

# Таблица связей для определения соотношения "многие ко многим" между вольером и домашним животным
aviary_pet_association = Table('aviary_pet', Base.metadata,
    Column('aviary_id', Integer, ForeignKey('aviaries.id')),
    Column('pet_id', Integer, ForeignKey('pets.id'))
)

class Volunteer(Base):
    __tablename__ = 'volunteers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    fio = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)

    def __repr__(self):
        return f"<Volunteer(fio='{self.fio}', phone_number='{self.phone_number}')>"

class Aviary(Base):
    __tablename__ = 'aviaries'

    id = Column(Integer, primary_key=True, autoincrement=True)
    size = Column(String, nullable=False)
    availability_of_walking = Column(Boolean, nullable=False)
    places = Column(Integer, nullable=False)
    pets = relationship('Pet', secondary=aviary_pet_association, back_populates='aviaries')

    def __repr__(self):
        return f"<Aviary(id={self.id}, size='{self.size}', availability_of_walking={self.availability_of_walking}, places={self.places})>"

class Pet(Base):
    __tablename__ = 'pets'

    id = Column(Integer, primary_key=True, autoincrement=True)
    kind = Column(String, nullable=False)
    name = Column(String, nullable=False)
    animal_species = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    size = Column(String, nullable=False)
    aviaries = relationship('Aviary', secondary=aviary_pet_association, back_populates='pets')

    def __repr__(self):
        return f"<Pet(id={self.id}, kind='{self.kind}', name='{self.name}', animal_species='{self.animal_species}', gender='{self.gender}', size='{self.size}')>"

class AnimalShelter(Base):
    __tablename__ = 'animal_shelters'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    # Establish relationships
    volunteers = relationship('Volunteer', back_populates='animal_shelter')
    aviaries = relationship('Aviary', back_populates='animal_shelter')

    def __repr__(self):
        return f"<AnimalShelter(id={self.id}, name='{self.name}')>"

Volunteer.animal_shelter_id = Column(Integer, ForeignKey('animal_shelters.id'))
Volunteer.animal_shelter = relationship('AnimalShelter', back_populates='volunteers')

Aviary.animal_shelter_id = Column(Integer, ForeignKey('animal_shelters.id'))
Aviary.animal_shelter = relationship('AnimalShelter', back_populates='aviaries')

DATABASE_URL = "sqlite:///animal_shelter.db"  # or any other database URL

def setup_database():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()



    print("Database setup complete.")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    setup_database()