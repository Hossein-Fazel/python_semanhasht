from Time import Time
class machine:
    def __init__(self, name : str):
        try:
            file = open("vBus.txt")
        except FileNotFoundError:
            raise ValueError(f"{name} file does not exist")
        self.speed = int(file.readline())
        self.traffic_speed = int(file.readline())

        self.price = int(file.readline())
        self.traffic_price = int(file.readline())

        self.get_in = int(file.readline())
        self.traffic_get_in = int(file.readline())

        self.start_time = Time(file.readline().replace("\n", ""))
        self.end_time = Time(file.readline().replace("\n", ""))

        file.close()
    
    def get_in_time(self,t1:Time):
        if t1.get_hour() >= self.start_time.get_hour() and t1.get_hour() <= self.end_time.get_hour() and t1.get_noon() == self.start_time.get_noon() :
            return self.traffic_get_in
        else :
            return self.get_in
    
    def get_pass_time(self, t1:Time):
        if t1.get_hour() >= self.start_time.get_hour() and t1.get_hour() <= self.end_time.get_hour() and t1.get_noon() == self.start_time.get_noon() :
            return self.traffic_speed
        else :
            return self.speed
    
    def get_price(self, t1:Time):
        if t1.get_hour() >= self.start_time.get_hour() and t1.get_hour() <= self.end_time.get_hour() and t1.get_noon() == self.start_time.get_noon() :
            return self.traffic_price
        else :
            return self.price