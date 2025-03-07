weight = float(input("Enter your weight: "))
if weight <= 0:
    print("Error: Weight must be a positive number.")
else:
    unit = input("Convert the weight to (kg or lb): ").strip().lower()

    if unit == "lb":
        converted_weight = weight * 2.205
        print(f"The weight = {round(converted_weight, 3)} lbs")
    elif unit == "kg":
        converted_weight = weight / 2.205
        print(f"The weight = {round(converted_weight, 3)} kg")
    else:
        print("Invalid conversion type. Please enter 'kg' or 'lb'.")