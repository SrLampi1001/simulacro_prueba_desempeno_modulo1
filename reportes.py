import asyncio
class Time:
    _current_time : list[int, int, int]
    _current_date: list[int, int, int]
    _time_interval = 10 #Normal time interval, can be aumented
    _simulate:bool

    async def run_time(self):
        """
        starts the simulation time for the program
        executes async from the main flow each second
        MUST NOT be called befor set_date and set_time class methods
        """
        while self._simulate:
            await asyncio.sleep(1)
            self._current_time[2] += self._time_interval
            if self._current_time[2] > 60: # Seconds
                time_skip = self._current_time[2]%60
                self._current_time[2] += -time_skip*60
                self._current_time[1] += time_skip #A minute passed
            if self._current_time[1] > 60: # Minutes
                time_skip = self._current_time[1]%60
                self._current_time[1] += -time_skip*60
                self._current_time[0] += time_skip #An hour passed
            if self._current_time[0]>24: #Hours
                time_skip = self._current_time[0]%24
                self._current_time[0] += -time_skip*24
                self._current_date[0] += time_skip #A day passed
            if self._current_date[0] > 30: #Days (Only 30 days months)
                time_skip = self._current_date[2]%30 
                self._current_date[0] += -time_skip*30
                self._current_date[1] += time_skip #A month passed
            if self._current_date[1]>12: # Months
                time_skip = self._current_date[1]%12
                self._current_date[1] += -time_skip*12
                self._current_date[2] += time_skip #A year passed

    def set_date(self, day, month, year):
        """
        sets date on class attribute __current_date
        [day, month, year] -> all must be integers
        """
        try:
            day = int(day)
            month = int(month)
            year = int(year)
        except:
            print(f"All of the values must be an integer number, day: {day}, month: {month} oy year: {year} are/is an invalid value")
            return
        self._current_date = [day, month, year]

    def set_time(self, hour, minute, second):
        try:
            hour = int(hour)
            minute = int(minute)
            second = int(second)
        except:
            print(f"All of the values must be Integers, there's one or multiple invalid values in the entries: hour: {hour}, minute: {minute}, second: {second}")
            return
        self._current_time = [hour, minute, second]

    def change_time_flow(self, value):
        """
        Changes the time, the value represents the amount of seconds the simulated time moves forward each real time second
        """
        try:
            value = int(value)
        except:
            print(f"the value {value} is invalid, must be an integer number")

    def stop_time(self):
        self._simulate = False

    def start_time(self):
        self._simulate = True
        asyncio.run(self.run_time)

#reports
from prestamos import Borrow
from usuarios import User
class Report:
    _most_used_equipment :list
    _most_used_equipment_category : list
    _most_damaged_equipment : list
    _most_delayed_equipment : list
    _delayments_to_aprove : list
    _most_demanding_user : list
    _most_delayed_users : list
    #Normal users reports:
    equipments_borrowed : list
    equipments_damaged : list
    equipments_delayed : list
    equipments_in_borrow : list

    def __init__(self, user:User, time_frame):
        self.user = user
        self.time_frame = time_frame

    
    def make_report(self, time_frame):
        if self.user.get_rol() == "admin":
            pass
        report = [["Borrow", "Equipment borrowed", "state borrow"], ]
        for borrow in self.borrows_list:
            if borrow.returned_date == None:
                pass
    