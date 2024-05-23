from pydantic import BaseModel
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from unit_of_work import UnitOfWork
from Repositories import VolunteerRepository, AviaryRepository, PetRepository, AnimalShelterRepository
from db_setup import Volunteer, Aviary, Pet, AnimalShelter
import json

def write_to_json(data, file_path):
    with open(file_path, 'a') as file:
        json.dump(data, file)
        file.write('\n')

class VolunteerCreate(BaseModel):
    fio: str
    phone_number: str

class VolunteerResponse(BaseModel):
    id: int
    fio: str
    phone_number: str

class AviaryCreate(BaseModel):
    size: str
    availability_of_walking: bool
    places: int

class AviaryResponse(BaseModel):
    id: int
    size: str
    availability_of_walking: bool
    places: int

class PetCreate(BaseModel):
    kind: str
    name: str
    animal_species: str
    gender: str
    size: str

class PetResponse(BaseModel):
    id: int
    kind: str
    name: str
    animal_species: str
    gender: str
    size: str

class AnimalShelterCreate(BaseModel):
    name: str

class AnimalShelterResponse(BaseModel):
    id: int
    name: str

app = FastAPI()

def get_db():
    with UnitOfWork() as session:
        yield session



@app.post("/volunteers/", response_model=VolunteerResponse)
def create_volunteer(volunteer: VolunteerCreate, db: Session = Depends(get_db)):
    db_volunteer = Volunteer(**volunteer.dict())
    db.add(db_volunteer)
    db.commit()
    db.refresh(db_volunteer)

    # Запись действия в JSON файл
    data = {"action": "create_volunteer", "volunteer_id": db_volunteer.id, "volunteer_data": volunteer.dict()}
    write_to_json(data, "actions.json")

    return db_volunteer

@app.post("/aviaries/", response_model=AviaryResponse)
def create_aviary(aviary: AviaryCreate, db: Session = Depends(get_db)):
    db_aviary = Aviary(**aviary.dict())
    db.add(db_aviary)
    db.commit()
    db.refresh(db_aviary)

    # Запись действия в JSON файл
    data = {"action": "create_aviary", "aviary_id": db_aviary.id, "aviary_data": aviary.dict()}
    write_to_json(data, "actions.json")

    return db_aviary

@app.post("/pets/", response_model=PetResponse)
def create_pet(pet: PetCreate, db: Session = Depends(get_db)):
    db_pet = Pet(**pet.dict())
    db.add(db_pet)
    db.commit()
    db.refresh(db_pet)

    # Запись действия в JSON файл
    data = {"action": "create_pet", "pet_id": db_pet.id, "pet_data": pet.dict()}
    write_to_json(data, "actions.json")

    return db_pet

@app.post("/shelters/", response_model=AnimalShelterResponse)
def create_animal_shelter(shelter: AnimalShelterCreate, db: Session = Depends(get_db)):
    db_shelter = AnimalShelter(**shelter.dict())
    db.add(db_shelter)
    db.commit()
    db.refresh(db_shelter)

    # Запись действия в JSON файл
    data = {"action": "create_animal_shelter", "shelter_id": db_shelter.id, "shelter_data": shelter.dict()}
    write_to_json(data, "actions.json")

    return db_shelter



@app.get("/volunteers/{volunteer_id}", response_model=VolunteerResponse)
def get_volunteer(volunteer_id: int, db: Session = Depends(get_db)):
    volunteer = db.query(Volunteer).filter(Volunteer.id == volunteer_id).first()
    if volunteer is None:
        raise HTTPException(status_code=404, detail="Volunteer not found")
    return volunteer

@app.get("/aviaries/{aviary_id}", response_model=AviaryResponse)
def get_aviary(aviary_id: int, db: Session = Depends(get_db)):
    aviary = db.query(Aviary).filter(Aviary.id == aviary_id).first()
    if aviary is None:
        raise HTTPException(status_code=404, detail="Aviary not found")
    return aviary

@app.get("/pets/{pet_id}", response_model=PetResponse)
def get_pet(pet_id: int, db: Session = Depends(get_db)):
    pet = db.query(Pet).filter(Pet.id == pet_id).first()
    if pet is None:
        raise HTTPException(status_code=404, detail="Pet not found")
    return pet

@app.get("/shelters/{shelter_id}", response_model=AnimalShelterResponse)
def get_animal_shelter(shelter_id: int, db: Session = Depends(get_db)):
    shelter = db.query(AnimalShelter).filter(AnimalShelter.id == shelter_id).first()
    if shelter is None:
        raise HTTPException(status_code=404, detail="Animal shelter not found")
    return shelter



if __name__ == '__main__':

    from uvicorn import run
    run("api:app", host="127.0.0.1", port=8000, reload=True)