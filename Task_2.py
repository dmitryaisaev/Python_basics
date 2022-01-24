from abc import ABC, abstractmethod

class Clothes(ABC):

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def cloth(self):
        pass

    @abstractmethod
    def calc_cloth(self, value):
        pass

class Coat(Clothes):

    @property
    def name(self):
        return 'Пальто'

    @property
    def cloth(self):
        return self.__cloth

    def calc_cloth(self, value):
        self.__cloth = round(value / 6.5 + 0.5, 2)

class Suit(Clothes):

    @property
    def name(self):
        return 'Костюм'

    @property
    def cloth(self):
        return self.__cloth

    def calc_cloth(self, value):
        self.__cloth = round(2 * value / 100 + 0.3, 2)


v = int(input('Введите размер (для пальто) = '))
h = int(input('Введите рост (для костюма) в см. = '))

coat = Coat()
suit = Suit()

coat.calc_cloth(v)
print(f'{coat.name}, для размера {v} необходимо ткани = {coat.cloth} пог.м.')

suit.calc_cloth(h)
print(f'{suit.name}, для роста {h} см. необходимо ткани = {suit.cloth} пог.м.')
