# Celsius ↔ Fahrenheit Converter

print("Temperature Converter")
choice = input("Convert to (C)elsius or (F)ahrenheit? ").lower()

if choice == "c":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F = {celsius:.2f}°C")
elif choice == "f":
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C = {fahrenheit:.2f}°F")
else:
    print("Invalid choice! Please enter C or F.")
