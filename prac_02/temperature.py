"""def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def main():
    celsius_temperature = float(input("Enter temperature in Celsius: "))
    fahrenheit_result = celsius_to_fahrenheit(celsius_temperature)
    display (f"{celsius_temperature} degrees Celsius is equal to {fahrenheit_result:.2f} degrees Fahrenheit")

    fahrenheit_temperature = float(input("Enter temperature in Fahrenheit: "))
    celsius_result = fahrenheit_to_celsius(fahrenheit_temperature)
    display (f"{fahrenheit_temperature} degrees Fahrenheit is equal to {celsius_result:.2f} degrees Celsius")

if __name__ == "__main__":
    main()"""


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def main():
    celsius_temperature = float(input("Enter temperature in Celsius: "))
    fahrenheit_result = celsius_to_fahrenheit(celsius_temperature)
    print(f"{celsius_temperature} degrees Celsius is equal to {fahrenheit_result:.2f} degrees Fahrenheit")

    fahrenheit_temperature = float(input("Enter temperature in Fahrenheit: "))
    celsius_result = fahrenheit_to_celsius(fahrenheit_temperature)
    print(f"{fahrenheit_temperature} degrees Fahrenheit is equal to {celsius_result:.2f} degrees Celsius")

if __name__ == "__main__":
    main()
