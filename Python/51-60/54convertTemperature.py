def fahrenheitToCelsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * (5 / 9)

def celsiusToFahrenheit(celsius: float) -> float:
    return (celsius * (9/ 5)) + 32

def main():
    choice = int(input("1.Fahrenheit To Celsius\n2.Celsius To Fahrenheit\nWhat do you want to do : "))
    if choice == 1:
        temperature = float(input("Enter fahrengeit to convert: "))
        result = fahrenheitToCelsius(temperature)
        print(result)

    elif choice == 2:
        temperature = float(input("Enter celsius to convert: "))
        result = celsiusToFahrenheit(temperature)
        print(result)

    else:
        print("Unknown choice")
main()