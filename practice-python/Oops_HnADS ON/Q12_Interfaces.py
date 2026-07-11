from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class ElectricVehicle(ABC):
    @abstractmethod
    def charge(self):
        pass


class GasVehicle(ABC):
    @abstractmethod
    def refuel(self):
        pass


class ElectricCar(Vehicle, ElectricVehicle):
    def start(self):
        print("Electric car started")

    def stop(self):
        print("Electric car stopped")

    def charge(self):
        print("Electric car charging")


class GasMotorcycle(Vehicle, GasVehicle):
    def start(self):
        print("Gas motorcycle started")

    def stop(self):
        print("Gas motorcycle stopped")

    def refuel(self):
        print("Gas motorcycle refueled")


if __name__ == "__main__":
    electric_car = ElectricCar()
    gas_motorcycle = GasMotorcycle()

    electric_car.start()
    electric_car.stop()
    electric_car.charge()

    gas_motorcycle.start()
    gas_motorcycle.stop()
    gas_motorcycle.refuel()
