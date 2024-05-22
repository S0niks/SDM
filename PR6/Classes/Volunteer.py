from dataclasses import dataclass


@dataclass(frozen=True)
class Volunteer:
    id: int
    fio: str
    phone_number: int


#v1 = Volunteer("Яковченко Софья Александровна", 89832957532)
#v2 = Volunteer("Жихарев Иван Аркадьевич", 89835568900)
#v3 = Volunteer("Николаев Павел Владимирович", 89833667834)
#v4 = Volunteer("Волонтёр", 89833667834)