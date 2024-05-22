import sys

#sys.path.append('C:\Users\Софья\Desktop\6 семак\Методологии разработки ПО\PR3')
from Classes.Volunteer import Volunteer


class VolunteerRepository:

    def __init__(self):
        self.volunteers = []

    def add_volunteer(self, volunteer: Volunteer):
        self.volunteers.append(volunteer)

    def del_volunteer(self, volunteer: Volunteer):
        self.volunteers.remove(volunteer)

    def find_volunteer(self, volunteer_id):
        for a in self.volunteers:
            if (a.id == volunteer_id):
                return a

    def show_volunteers(self):
        for a in self.volunteers:
            print(a)
