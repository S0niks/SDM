from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base, AnimalShelter, Volunteer, Aviary, Pet

DATABASE_URL = "sqlite:///animal_shelter.db"

# Setup the database and session
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Create instances of Volunteer
volunteer1 = Volunteer(fio="John Doe", phone_number="123456789")
volunteer2 = Volunteer(fio="Jane Smith", phone_number="987654321")

# Create instances of Pet
pet1 = Pet(kind="Dog", name="Buddy", animal_species="Golden Retriever", gender="Male", size="Large")
pet2 = Pet(kind="Cat", name="Whiskers", animal_species="Siamese", gender="Female", size="Small")

# Create instances of Aviary
aviary1 = Aviary(size="Large", availability_of_walking=True, places=5)
aviary2 = Aviary(size="Small", availability_of_walking=False, places=2)

# Associate pets with aviaries
aviary1.pets.append(pet1)
aviary2.pets.append(pet2)

# Create instance of AnimalShelter
shelter = AnimalShelter(name="Happy Paws Shelter", volunteers=[volunteer1, volunteer2], aviaries=[aviary1, aviary2])

# Add all instances to the session and commit
session.add(shelter)
session.commit()

# Query the database and print results
shelters = session.query(AnimalShelter).all()
for shelter in shelters:
    print(shelter)
    for volunteer in shelter.volunteers:
        print(f"  {volunteer}")
    for aviary in shelter.aviaries:
        print(f"  {aviary}")
        for pet in aviary.pets:
            print(f"    {pet}")

# Close the session
session.close()