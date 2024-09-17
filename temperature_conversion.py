unit  = input("Is this temperature measurement taken if Celsius or Fahrenheit (C / F): ")
temperature = float(input("Enter the measured temperature: "))

if unit == "C":
    temperature = round((9 * temperature) / 5 + 32, 1)
    print(f"The temperature converted to Fahrenheit is : {temperature}° F")
elif unit == "F":
    temperature = round((temperature - 32) * 5 / 9, 1)
    print(f"The temperature converted to Celsius is : {temperature}° C")
else:
    print(f"{unit} is not valid unit of temperature measurement.")
