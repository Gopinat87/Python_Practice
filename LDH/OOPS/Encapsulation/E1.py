class car:
    def open_door_and_closed(self):
        print("door opened ")
        print("Start to drive")
        self._accelerate()

    def _accelerate(self) :
        print("Bikes starts Move")
        self.__engine_start()
    
    def __engine_start(self) :
        print("Engine started ")

my_car = car()
my_car.open_door_and_closed()
