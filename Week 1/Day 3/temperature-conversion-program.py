temperature = float(input("Enter the temperature: "))
unit = input("Convert temperature to (C or F): ").strip().upper()

if unit == "F":
    fahrenheit = (temperature * (9/5)) + 32
    print(f"The temperature = {round(fahrenheit, 3)} °F")
elif unit == "C":
    celsius = (temperature - 32) * (5/9)
    print(f"The temperature = {round(celsius, 3)} °C")
else:
    print("Invalid unit. Please enter 'C' or 'F'.")