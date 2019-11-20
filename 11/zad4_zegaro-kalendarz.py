import time
import datetime


class Watch:
    def __init__(self):
        czas = time.strftime("%H:%M")
        print('Aktualna godzina to: ', czas)


class Calendar:
    def __init__(self):
        data = datetime.datetime.now().date()
        print('Aktualna data to: ', data)


class WatchCalendar(Watch, Calendar):
    def current_date_time(self):
        print(Calendar.__init__(self))
        print(Watch.__init__(self))


wc = WatchCalendar()