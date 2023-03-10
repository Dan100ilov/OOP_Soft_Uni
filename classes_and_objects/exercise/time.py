class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return f"{self.hours}:{self.minutes}:{self.seconds}"

    def next_second(self):
        if int(self.seconds) + 1 > self.max_seconds:
            self.seconds = '00'
            self.minutes = int(self.minutes) + 1
            if int(self.minutes) > self.max_minutes:
                self.minutes = "00"
                self.hours = int(self.hours) + 1
                already_changed = True
                if int(self.hours) > self.max_hours:
                    self.hours = "00"
                elif 0 < int(self.hours) < 10:
                    self.hours = "0" + str(self.hours)
            elif 0 < int(self.minutes) < 10:
                self.minutes = "0" + str(self.minutes)
                self.hours = "0" + str(self.hours)
            elif 9 < int(self.minutes) <= self.max_minutes:
                self.hours = "0" + str(self.hours)

        elif 0 <= int(self.seconds) + 1 < 10:
            self.seconds = "0" + str(int(self.seconds) + 1)
            if 0 <= int(self.minutes) < 9:
                self.minutes = "0" + str(self.minutes)
            if 0 <= int(self.hours) < 9:
                self.hours = "0" + str(self.hours)

        elif 9 < int(self.seconds) + 1 <= self.max_seconds:
            self.seconds = int(self.seconds) + 1
            if 0 <= self.minutes < 9:
                self.minutes = "0" + self.minutes
            if 0 <= self.hours < 9:
                self.hours = "0" + str(self.hours)


        return self.get_time()


# time = Time(9, 30, 59)
# print(time.next_second())

# time = Time(10, 59, 59)
# print(time.next_second())

# time = Time(23, 59, 59)
# print(time.next_second())

# time = Time(1, 20, 30)
# print(time.next_second())

time = Time(1, 20, 29)
print(time.next_second())
'''
00:00:00
00:00:001

09:10:12
09:10:13

09:58:59
09:59:00

09:59:59
10:00:00

23:59:59
00:00:00


'''
