class TemperatureConverter:
    @staticmethod
    def celsiusToFahrenheit(celsius):
        return (celsius * 9 / 5) + 32

    @staticmethod
    def fahrenheitToCelsius(fahrenheit):
        return (fahrenheit - 32) * 5 / 9


if __name__ == "__main__":
    print("25°C =", TemperatureConverter.celsiusToFahrenheit(25), "°F")
    print("77°F =", TemperatureConverter.fahrenheitToCelsius(77), "°C")
