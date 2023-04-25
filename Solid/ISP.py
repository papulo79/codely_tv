import abc


class Run(abc.ABC):
    @abc.abstractmethod
    def run(self):
        pass


class Bark(abc.ABC):
    @abc.abstractmethod
    def bark(self):
        pass


class Fly(abc.ABC):
    @abc.abstractmethod
    def fly(self):
        pass


class Dog(Run, Bark):
    def run(self):
        print('Dog is running')

    def bark(self):
        print('Dog is barking')


class Bird(Run, Fly):
    def run(self):
        print('Bird is running')

    def fly(self):
        print('Bird is flying')
