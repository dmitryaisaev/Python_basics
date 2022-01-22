from time import sleep

class TrafficLight:
    __color = 'red'
    def running(self):
        for i in range(20):
            print(self.__color)
            if self.__color == 'red':
                sleep(7)
                self.__color = 'yellow'
            elif self.__color == 'yellow':
                sleep(2)
                self.__color = 'green'
            elif self.__color == 'green':
                sleep(5)
                self.__color = 'red'

tl1 = TrafficLight()
tl1.running()
