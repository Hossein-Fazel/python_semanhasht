from multidispatch import *
class Time(metaclass=MultipleMeta):
    def __init__(self, got_time : str):
        self.hour = 0
        self.minute = 0
        self.type = ""

        size = len(got_time)
        thour = ""
        tminute = ""
        ttype = got_time[size-2: size]

        self.set_type(ttype)

        is_check = 0
        for i in range(0, size - 2):
            if got_time[i] == ':' or got_time[i] == ' ':
                is_check = 1
                continue

            if is_check :
                tminute += got_time[i]
            else :
                thour += got_time[i]

        self.set_hour(int(thour))
        self.set_minute(int(tminute))

    def __init__(self):
        self.hour = 0
        self.minute = 0
        self.type = "AM"

    def __init__(self, hour:int, minute:int, type:str):
        self.hour = 0
        self.minute = 0
        self.type = ""

        self.set_type(type)
        self.set_hour(hour)
        self.set_minute(minute)

    def set_hour(self,hour : int):
        if hour <= 12 and hour >= 0 :
            self.hour = hour;
        else :
            raise ValueError("Invalid hour value")
    
    def set_minute(self, minute : int):
        if minute <= 60 and minute >= 0 :
            self.minute = minute;
        else :
            raise ValueError("Invalid minute value")
    
    def set_type(self, type : str):
        if type.lower() == "am" or type.lower() == "pm":
            self.type = type;
        else :
            raise ValueError(f"{type} Invalid Type value")

    def __iadd__(self, number : int):
        if(not isinstance(number, int)):
            raise ValueError("not an int")
        self.minute += number
        if self.minute >= 60 :
            count = int(self.minute / 60)
            self.minute %= 60
            self.hour += count

            if self.hour == 12 :
                if self.type.lower() == "am":
                    self.type = "PM"
                elif self.type.lower() == "pm":
                    self.type = "AM"
            
            elif self.hour > 12 :
                self.hour %= 12
        
        return self
    
    def __add__(self, min:int):
        t1 = Time()
        t1.set_hour(self.get_hour())
        t1.set_minute(self.get_minute())
        t1.set_type(self.get_type())

        t1 += min
        return t1

    def __str__(self):
        time = f"{self.hour}"
        if self.minute != 0 :
            time = time + f":{self.minute} "
        time = time  + f" {self.type}"

        return time
    
    def get_hour(self) :
        return self.hour
    
    def get_minute(self) :
        return self.minute
    
    def get_type(self):
        return self.type
