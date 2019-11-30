import datetime
import holidays


class Student:
    min_avg = 4.5
    university = 'New York Academy'

    def __init__(self, name, last, age, student_avg):
        self.name = name
        self.last = last
        self.age = age
        self.student_avg = student_avg

    def __repr__(self):
        return self.name.capitalize() + " " + self.last.capitalize()

    @property # sprawia ze traktujemy funkcje jak atrybut
    def email(self):
        return '{}.{}.university.com'.format(self.name, self.last)

    def grant_scholarship(self):
        if self.student_avg > self.min_avg:
            print('Przyznano stypendium')
        else:
            print('Odmowa przyznania stypendium')

    @classmethod  # sprawia ze set_min_avg dziala dla kazdej klasy, ze jest metoda klasowa
    def set_min_avg(cls, new_avg):
        """ this method sets min avg for scholarship """
        cls.min_avg = new_avg

    @staticmethod
    def academic_football_cheer(nr):
        return 'Go go NYA! ' * nr

    @staticmethod
    def academic_day(day):
        if day.weekday() == 5 or day.weekday() == 6: # or day.weekday() == holidays(): ??
            return False
        else:
            return True


obj_anna = Student('anna', 'kowalska', 23, 4.7)
obj_arek = Student('arkadiusz', 'nowak', 21, 3.9)

print(obj_anna.email)
print(Student.min_avg)

# obj_anna.set_min_avg(3.0)
# print(obj_anna.min_avg)
# print(obj_arek.min_avg)
# print(Student.academic_football_cheer(5))

today = datetime.date.today()
print('Czy dzisiaj są zajęcia? ', Student.academic_day(today))

